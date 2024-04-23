from django.shortcuts import render, get_object_or_404

# Import Models
from galeria.models import Fotografia

# Create your views here.
def index(request):
  
  fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

  return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
  # Puxa o objeto ou não encontrado
  fotografia = get_object_or_404(Fotografia, pk=foto_id)

  return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):

  fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

  # FILTRAR POR PALAVRA
  if "buscar" in request.GET:
    nome_a_buscar = request.GET['buscar']
    
    if nome_a_buscar:
      fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

  return render(request, "galeria/buscar.html", {"cards": fotografias})