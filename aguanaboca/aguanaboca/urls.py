"""
URL configuration for aguanaboca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from projeto_aguanaboca.views import edita_categoria, edita_produto, lista_categorias, lista_produtos, adiciona_produto, adiciona_categoria, produtos_por_categoria, remove_categoria, remove_produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('produtos/adicionar/', adiciona_produto, name='adiciona_produto'),
    path('', lista_produtos, name='raiz'),  
    path('categorias/adicionar/', adiciona_categoria, name='adiciona_categoria'),
    path('edita_produto/<int:produto_id>/', edita_produto, name='edita_produto'),
    path('remove_produto/<int:produto_id>/', remove_produto, name='remove_produto'),
    path('categorias/', lista_categorias, name="lista_categorias"),
    path('produtos_por_categoria/<int:categoria_id>', produtos_por_categoria, name="produtos_por_categoria"),
    path('categorias/editar/<int:categoria_id>/', edita_categoria, name='edita_categoria'),
    path('categorias/remover/<int:categoria_id>/', remove_categoria, name='remove_categoria'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)