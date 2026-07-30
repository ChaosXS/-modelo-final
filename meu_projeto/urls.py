"""
URL configuration for meu_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from meu_app import views  # 1. Importa as views do seu app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.post_view, name='post_view'),  # 2. Conecta a URL 'posts/' à sua view
]
