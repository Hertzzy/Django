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