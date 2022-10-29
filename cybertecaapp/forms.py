from django import forms
from cybertecaapp.models import Livros,Autores,Categorias


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields= '__all__'