from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render (request, "home.html")

def descripcion(request):
    return render (request, "descripcion.html")

def usuarios(request):
    return render (request, "usuarios.html")
    
def publicaciones(request):
    return render (request, "publicaciones.html")