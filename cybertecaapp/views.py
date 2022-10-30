from django.shortcuts import render
from cybertecaapp.forms import LivroForm

# Create your views here.

def index(request):
    return render(request, 'cyberteca/index.html')


def base(request):
    return render(request, 'cyberteca/base.html')


def new_book(request):
    form = LivroForm(request.POST)
    if request.method=="POST":
        form =LivroForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form= LivroForm()
    return render(request, 'cyberteca/new_book.html',{'form':form})