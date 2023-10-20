from django.urls import path
from.import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('invex', views.invex, name='invex'),
    path('usuarios', views.usuarios, name='usuarios'),

]