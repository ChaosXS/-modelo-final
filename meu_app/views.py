from django.shortcuts import render
from django.http import HttpResponse 
from .models import Livro  # IMPORTANTE: Você precisa importar o modelo Livro

# Mantém a view que o seu urls.py está chamando para evitar erros
def post_view(request):
    return HttpResponse("Hello World")

# Esta versão da função index resolve o problema apontado pelo tutor Samir
def index(request):
    # Busca todos os livros cadastrados no Django Admin
    livros = Livro.objects.all() 
    
    # Envia a variável 'livros' para o seu index.html
    return render(request, 'meu_app/index.html', {'livros': livros})
    