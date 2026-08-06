from django.contrib import admin
from django.urls import path
from meu_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.post_view, name='post_view'), # O Django vai procurar o post_view aqui
    path('', views.index, name='index'), # Adicione esta linha para a sua página inicial de templates
]
