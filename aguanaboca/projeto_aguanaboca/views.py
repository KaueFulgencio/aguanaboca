from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

from .models import Categoria, Produto
from .forms import ProdutoForm, CategoriaForm

def lista_produtos(request):
    termo_de_pesquisa = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    preco_maximo = request.GET.get('preco', '')

    produtos = Produto.objects.filter(nome__icontains=termo_de_pesquisa)

    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)

    if preco_maximo:
        preco_maximo = float(preco_maximo)
        produtos = produtos.filter(preco__lte=preco_maximo)

    categorias = Categoria.objects.all()

    return render(request, 'admin/lista_produtos.html', {
        'produtos': produtos,
        'termo_de_pesquisa': termo_de_pesquisa,
        'categorias': categorias,
        'categoria_selecionada': int(categoria_id) if categoria_id else None,
        'preco_maximo': preco_maximo,
    })

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

def edita_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'admin/edita_produto.html', {'form': form, 'produto': produto})

def remove_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')

    return render(request, 'admin/confirma_remove_produto.html', {'produto': produto})