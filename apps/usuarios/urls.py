from django.urls import path
from apps.usuarios.views import login, cadastro, logout

# ROTAS DA USUARIOS
urlpatterns = [
  path('login', login, name='login'),
  path('cadastro', cadastro, name='cadastro'),
  path('logout', logout, name='logout'),
]