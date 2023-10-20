from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return HttpResponse("<h1>BIENVENIDO A HOTEL LODGING </h1>")

def invex(request):
    return render(request, 'paginas/invex.html')


def usuarios(request):
    return render(request, 'usuarios/index2.html')

