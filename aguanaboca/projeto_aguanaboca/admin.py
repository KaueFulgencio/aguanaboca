from django.contrib import admin

# Register your models here.
from .models import Categoria, Produto, RegistroAtividade

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(RegistroAtividade)