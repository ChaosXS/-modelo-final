from django.contrib import admin
from .models import Livro  # Se mudou o nome no models.py, mude aqui também

admin.site.register(Livro)