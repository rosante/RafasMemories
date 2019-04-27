from django.db import models


# Create your models here.
class Memoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    datacriacao = models.DateTimeField()
    alerta = models.BooleanField()
    dataevento = models.DateTimeField()

    def __str__(self):
        return self.nome