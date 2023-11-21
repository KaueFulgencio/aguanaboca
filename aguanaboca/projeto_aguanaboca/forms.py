from django import forms
from .models import Produto, Categoria

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        help_texts = {
            'nome': 'Informe o nome do produto.',
            'preco': 'Informe o preço do produto em reais.',
            'descricao': 'Preencha a descrição',
            'categoria': 'Escolha uma categoria'
        }

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco < 0:
            raise forms.ValidationError("O preço não pode ser negativo.")
        return preco

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']