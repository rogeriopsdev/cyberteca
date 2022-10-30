from django.contrib import admin
from cybertecaapp.models import Livros,Autores,Categorias,Material

# Register your models here.

admin.site.register(Livros)
admin.site.register(Autores)
admin.site.register(Categorias)
admin.site.register(Material)

