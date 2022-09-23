from django.shortcuts import render,redirect
from .models import Usuario, Publicaciones,Categoria

# Create your views here.
def home(request):
    return render(request,"home.html")

def ver(request):
    usuarios=Usuario.objects.all()
    return render(request, "ver.html", {"usuarios":usuarios})

def mod(request):
    usuario=Usuario.objects.all()
    return render(request,"mod.html", {"usuarios":usuario})

def add(request):
    return render(request,"add.html")

def addpublicacion(request):
    return render(request,"addpublicacion.html")

def registrarUsuario(request):
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    correo=request.POST['correo']
    telefono=request.POST['telefono']
    tipo=request.POST['tipo_usuario']
    usuario=Usuario.objects.create(nombre=nombre,apellido=apellido,correo=correo,telefono=telefono,tipo=tipo)
    return redirect('/')

def eliminarUsuario(request, id):
    usuario=Usuario.objects.get(id_usuario=id)
    usuario.delete()
    return redirect('/')

def editarUsuario(request, id):
    usuario=Usuario.objects.get(id_usuario=id)
    return render(request, "editar.html", {'usuario':usuario})

def modificarUsuario(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    telefono=request.POST['telefono']
    correo=request.POST['correo']
    tipo=request.POST['tipo_usuario']
    usuario=Usuario.objects.get(id_usuario=id)
    usuario.nombre=nombre
    usuario.apellido=apellido
    usuario.correo=correo
    usuario.telefono=telefono
    usuario.tipo=tipo
    usuario.save()
    return redirect('/')

def descripcion(request):
    return render (request, "descripcion.html")