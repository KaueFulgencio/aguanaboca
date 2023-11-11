from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'projeto_aguanaboca'

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome

class RegistroAtividade(models.Model):
    ACAO_CHOICES = (
        ('adicao', 'Adição'),
        ('edicao', 'Edição'),
        ('remocao', 'Remoção'),
    )

    acao = models.CharField(max_length=10, choices=ACAO_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.PositiveIntegerField()
    tipo_item = models.CharField(max_length=50)  
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.get_acao_display()} por {self.usuario.username} em {self.timestamp}'
