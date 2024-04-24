from django.shortcuts import render, redirect

# IMPORT FORMS
from usuarios.forms import LoginForms, CadastroForms

# IMPORT TABELA
from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib import auth
# Create your views here.
def login(request):

  #INSTANCIA
  form = LoginForms()

  if request.method == 'POST':
    # Pega as informações do formulário e coloca dentro de um formulario novo
    form = LoginForms(request.POST)

    # VERIFICA SE O FORMULARIO ESTÁ VALIDO
    if form.is_valid():
      # BUSCAR INFORMAÇÕES DO FORMULARIO (NOME E SENHA)
      nome = form['nome_login'].value()
      senha = form['senha'].value()

    usuario = auth.authenticate(
      request,
      username=nome,
      password=senha
    )

    if usuario is not None:
      auth.login(request, usuario)
      
      messages.success(request, f"{nome} logado com sucesso!")

      return redirect('index')
    else:
      messages.error(request, f"Erro ao efetuar login!")

      return redirect('login') 

  return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):

  form = CadastroForms()
  
  if request.method == 'POST':
    # Pega as informações do formulário e coloca dentro de um formulario novo
    form = CadastroForms(request.POST)

    # VERIFICA SE O FORMULARIO ESTÁ VALIDO
    if form.is_valid():
      # VERIFICA SE SENHA 1 É IGUAL A SENHA 2
      

      nome = form["nome_cadastro"].value()
      email = form["email"].value()
      senha = form["senha_1"].value()

      # VERIFICA SE USUÁRIO JÁ EXISTE
      if User.objects.filter(username=nome).exists():
        messages.error(request, "Usuário já existente")
        return redirect('cadastro')

      usuario = User.objects.create_user(
        username=nome,
        email=email,
        password=senha
      )

      usuario.save()

      messages.success(request, "Cadastrado com")

      return redirect('login')

  return render(request, "usuarios/cadastro.html", {"form": form})


def logout(request):


  auth.logout(request)

  messages.success(request, "Logout efetuado com sucesso!")

  return redirect('index')


