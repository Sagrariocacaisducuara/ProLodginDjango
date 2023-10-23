from django.urls import path
from.import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('invex', views.invex, name='invex'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('inicio', views.inicio, name='inicio'),
    path('usuarios/crear', views.crear, name='crear'),
    path('usuarios/editar', views.editar, name='editar'),

]