from django.urls import path
from galeria.views import index, imagem

# ROTAS DA GALERIA
urlpatterns = [
  path('', index, name='index'),
  path('imagem/<int:foto_id>', imagem, name='imagem')
]