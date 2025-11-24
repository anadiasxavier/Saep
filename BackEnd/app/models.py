from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    id = models.AutoField(primary_key=True, db_column="ID_USUARIO")
    nome = models.CharField(max_length=255, db_column="NOME")
    email = models.EmailField(unique=True, db_column="EMAIL")
    senha = models.CharField(max_length=255, db_column="SENHA")

    class Meta:
        db_table = "USUARIO"

    def save(self, *args, **kwargs):
        if not self.senha.startswith("pbkdf2_"):
            self.senha = make_password(self.senha)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    id = models.AutoField(primary_key=True, db_column="ID_PRODUTO")
    nome = models.CharField(max_length=120, db_column="NOME_PRODUTO")
    descricao = models.TextField(db_column="DESCRICAO")
    preco = models.DecimalField(max_digits=10, decimal_places=2, db_column="PRECO")
    quantidade_estoque = models.IntegerField(db_column="QUANTIDADE_ESTOQUE")
    estoque_minimo = models.IntegerField(db_column="ESTOQUE_MINIMO")

    class Meta:
        db_table = "PRODUTO"
    
    def __str__(self):
        return self.nome 


class MovimentacaoEstoque(models.Model):
    id = models.AutoField(primary_key=True, db_column="ID_MOVIMENTACAO")

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        db_column="ID_PRODUTO",
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column="ID_USUARIO",
    )

    tipo = models.CharField(
        max_length=10,
        choices=(("entrada", "Entrada"), ("saida", "Saída")),
        db_column="TIPO_MOVIMENTACAO",
    )

    quantidade = models.IntegerField(db_column="QUANTIDADE")
    data = models.DateField(db_column="DATA_MOVIMENTACAO")

    class Meta:
        db_table = "MOVIMENTACAO_ESTOQUE"

    def __str__(self):
        return self.nome
