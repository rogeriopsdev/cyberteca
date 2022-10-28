from django.db import models

# Create your models here.
from django.db import models

# Create your models here.



class Categorias(models.Model):
    categoria = models.CharField(max_length=255, null=True)


class Autores(models.Model):
    nome = models.CharField(max_length=255, null=True)



class Livros(models.Model):
    material = models.CharField(max_length=255)
    chamada = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    ano = models.CharField (max_length=255)
    data_cadastro = models.CharField (max_length=255)
    imagem = models.ImageField(blank=True,null=True,)
    categoriaid = models.ForeignKey(
        'Categorias', on_delete=models.SET_NULL, null=True)
    autoresid = models.ForeignKey(
        'Autores', on_delete=models.SET_NULL, null=True)