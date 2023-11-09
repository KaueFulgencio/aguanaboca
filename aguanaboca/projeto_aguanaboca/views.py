from django.shortcuts import render, redirect

# Create your views here.

from .models import Produto
from .forms import ProdutoForm, CategoriaForm

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'admin/lista_produtos.html', {'produtos': produtos})

def adiciona_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'admin/form_produto.html', {'form': form})

def adiciona_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')  
    else:
        form = CategoriaForm()

    return render(request, 'admin/adiciona_categoria.html', {'form': form})

