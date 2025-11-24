from rest_framework import serializers
from .models import Produto, MovimentacaoEstoque, Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "nome", "email"]


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


class MovimentacaoEstoqueSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = MovimentacaoEstoque
        fields = "__all__"
