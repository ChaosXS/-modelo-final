from django.db import models

class Livro(models.Model):
    # Opções para o campo de status
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=100)
    # Novo campo: Slug (essencial para a correção)
    slug = models.SlugField(max_length=100) 
    autor = models.CharField(max_length=50)
    ano_publicacao = models.IntegerField()
    # Novo campo: Status com as opções definidas acima
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='rascunho')

    def __str__(self):
        return self.titulo
        