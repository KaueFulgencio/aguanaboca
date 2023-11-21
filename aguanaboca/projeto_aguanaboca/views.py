from django.shortcuts import get_object_or_404, render, redirect
#from django.contrib.auth.decorators import login_required  
from django.db import IntegrityError, transaction
from django.contrib import messages
from .models import Categoria, Produto, RegistroAtividade
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
    
    historico = RegistroAtividade.objects.all()  

    return render(request, 'admin/lista_produtos.html', {
        'produtos': produtos,
        'termo_de_pesquisa': termo_de_pesquisa,
        'categorias': categorias,
        'categoria_selecionada': int(categoria_id) if categoria_id else None,
        'preco_maximo': preco_maximo,
        'historico': historico, 
    })


def adiciona_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save()

            RegistroAtividade.objects.create(
                acao='adicao',
                usuario=request.user,
                item_id=produto.id,
                tipo_item='Produto',
            )

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
            RegistroAtividade.objects.create(
                acao='edicao',
                usuario=request.user,
                item_id=produto.id,
                tipo_item='Produto',
            )
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'admin/edita_produto.html', {'form': form, 'produto': produto})

def remove_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        with transaction.atomic():
            RegistroAtividade.objects.create(
                acao='remocao',
                usuario=request.user,
                item_id=produto.id,
                tipo_item='Produto',
            )
            produto.delete()

        return redirect('lista_produtos')

    return render(request, 'admin/confirma_remove_produto.html', {'produto': produto})

def historico_atividades(request):
    logs = RegistroAtividade.objects.all()
    return render(request, 'historico_atividades.html', {'logs': logs})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'admin/lista_categorias.html', {'categorias': categorias})

def produtos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'admin/produtos_por_categoria.html', {'categoria': categoria, 'produtos': produtos})

def edita_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'admin/edita_categoria.html', {'form': form, 'categoria': categoria})

def remove_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')

    return render(request, 'admin/confirma_remove_categoria.html', {'categoria': categoria})