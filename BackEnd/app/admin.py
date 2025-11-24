from django.contrib import admin
from .models import Produto, MovimentacaoEstoque, Usuario
@admin.register(Usuario)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha')
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade_estoque', 'estoque_minimo', 'preco')

@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data', 'usuario')
