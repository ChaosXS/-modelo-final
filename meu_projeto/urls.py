from django.contrib import admin
from django.urls import path
from meu_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.post_view, name='post_view'), 
    # Adicione a linha abaixo para resolver o erro 404 da imagem
    path('', views.index, name='index'), 
]
