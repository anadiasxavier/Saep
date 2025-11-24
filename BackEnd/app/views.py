from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from .models import Produto, MovimentacaoEstoque , Usuario
from .serializers import ProdutoSerializer, MovimentacaoEstoqueSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


#login

class LoginView(APIView):
    def post(self, request):
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

        # Criar JWT manualmente
        refresh = RefreshToken()
        refresh["user_id"] = usuario.id
        refresh["nome"] = usuario.nome

        access_token = refresh.access_token

        return Response({
            "mensagem": "Login realizado",
            "usuario": usuario.nome,
            "access": str(access_token),
            "refresh": str(refresh)
        })
    
# LISTAR, BUSCAR, CRIAR, EDITAR, EXCLUIR PRODUTO
class ProdutoListCreateView(generics.ListCreateAPIView):
    queryset = Produto.objects.all().order_by("nome")
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']


class ProdutoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]


# MOVIMENTAÇÃO DE ESTOQUE COM VERIFICAÇÃO

class MovimentacaoCreateView(generics.CreateAPIView):
    serializer_class = MovimentacaoEstoqueSerializer
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        token = JWTAuthentication().authenticate(self.request)
        user_id = token[0].payload.get("user_id")

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