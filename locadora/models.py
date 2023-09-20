from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    nome = models.CharField(max_length = 100)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome

class Locacao(models.Model):
    nome = models.CharField(max_length = 100)
    data = models.DateField()
    filme = models.ManyToManyField(Filme)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome