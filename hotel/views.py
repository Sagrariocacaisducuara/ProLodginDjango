from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')

def invex(request):
    return render(request, 'paginas/invex.html')


def usuarios(request):
    return render(request, 'usuarios/index2.html')

def crear(request):
    return render(request, 'usuarios/crear.html')

def editar(request):
    return render(request, 'usuarios/editar.html')


