from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django.contrib.auth.hashers import check_password

from .models import Produto, MovimentacaoEstoque, Usuario
from .serializers import ProdutoSerializer, MovimentacaoEstoqueSerializer

# Login (no auth)
@method_decorator(csrf_exempt, name="dispatch")
class LoginView(APIView):
    # Allow any here; login must be open
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        # debug prints (remova em produção)
        print("raw body:", request.body)
        print("content type:", request.content_type)
        print("parsed data:", request.data)

        email = request.data.get("email")
        senha = request.data.get("senha")

        if not email or not senha:
            return Response({"erro": "Informe email e senha"}, status=400)

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return Response({"erro": "Usuário não encontrado"}, status=404)

        if not check_password(senha, usuario.senha):
            return Response({"erro": "Senha incorreta"}, status=401)

        # Gerar token manualmente com payload que inclui user_id
        refresh = RefreshToken()  # token manual
        refresh["user_id"] = usuario.id
        refresh["nome"] = usuario.nome

        access = refresh.access_token

        return Response(
            {
                "mensagem": "Login realizado",
                "usuario": usuario.nome,
                "access": str(access),
                "refresh": str(refresh),
            }
        )


# PRODUTOS (protegido)
class ProdutoListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Produto.objects.all().order_by("nome")
    serializer_class = ProdutoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["nome"]


class ProdutoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


# MOVIMENTAÇÃO (protegida)
class MovimentacaoCreateView(generics.CreateAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MovimentacaoEstoqueSerializer

    def perform_create(self, serializer):
        auth = JWTTokenUserAuthentication()
        auth_result = auth.authenticate(self.request)
        # auth_result is (user, token_or_payload) or None; our custom token returns (None, payload)
        if not auth_result:
            raise PermissionError("Token inválido")
        payload = auth_result[1]
        user_id = payload.get("user_id")

        usuario = Usuario.objects.get(id=user_id)

        movimentacao = serializer.save(usuario=usuario)
        produto = movimentacao.produto

        if movimentacao.tipo == "entrada":
            produto.quantidade_estoque += movimentacao.quantidade
        else:
            if produto.quantidade_estoque - movimentacao.quantidade < produto.estoque_minimo:
                print("ALERTA: Estoque abaixo do mínimo!")
            produto.quantidade_estoque -= movimentacao.quantidade

        produto.save()
