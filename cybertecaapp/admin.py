from django.contrib import admin
from cybertecaapp.models import Livros,Autores,Categorias

# Register your models here.

admin.site.register(Livros)
admin.site.register(Autores)
admin.site.register(Categorias)

