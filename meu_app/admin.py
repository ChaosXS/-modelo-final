from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    # Isso faz o slug ser gerado automaticamente a partir do título
    prepopulated_fields = {'slug': ('titulo',)}
    # Opcional: exibe o status na lista do admin para facilitar
    list_display = ('titulo', 'autor', 'status')
    