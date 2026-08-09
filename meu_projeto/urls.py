from django.contrib import admin
from django.urls import path
from meu_app import views  # Importa as views do seu app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.post_view, name='post_view'),
    path('async-calc/', views.async_calc_view, name='async_calc'),
]
