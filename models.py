from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    qtd = models.IntegerField()
    preco = models.DecimalField(decimal_places=2, max_digits=100)


    def __str__(self):
        return self.nome

    def preco_total(self):
        return self.preco * self.qtd
