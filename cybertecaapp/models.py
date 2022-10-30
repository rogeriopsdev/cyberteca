import datetime
from datetime import date

from django.db import models

# Create your models here.
from django.db import models
from PIL import Image
# Create your models here.



class Categorias(models.Model):
    categoria = models.CharField(max_length=255, null=True)



    def __str__(self):
        return self.categoria


class Autores(models.Model):
    nome = models.CharField(max_length=255, null=True)


    def __str__(self):
        return self.nome

class Material(models.Model):
    nome = models.CharField(max_length=255,null=True)
    imagem =models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome



class Livros(models.Model):
    materialid = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
    chamada = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    ano = models.CharField (max_length=255)
    data_cadastro = models.DateTimeField()
    imagem = models.ImageField(blank=True,null=True,)
    categoriaid = models.ForeignKey(
        'Categorias', on_delete=models.SET_NULL, null=True)
    autoresid = models.ForeignKey(
        'Autores', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

    def save(self):
        super().save()
        im = Image.open(self.imagem.path)
        novo_tamanho = (100, 100)
        im.thumbnail(novo_tamanho)
        im.save(self.imagem.path)

    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url
        else:
            return self.titulo

