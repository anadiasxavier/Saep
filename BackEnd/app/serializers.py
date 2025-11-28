from rest_framework import serializers
from .models import Produto, MovimentacaoEstoque

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "descricao", "preco", "quantidade_estoque", "estoque_minimo"]


class MovimentacaoEstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimentacaoEstoque
        fields = ["id", "produto", "tipo", "quantidade", "data"]
