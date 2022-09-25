from django.shortcuts import render,redirect
from .models import Usuario, Publicaciones,Categoria

# Create your views here.
def home(request):
    publicaciones=Publicaciones.objects.all()
    usuarios=Usuario.objects.all()
    categoria=Categoria.objects.all()
    return render(request,"home.html",{"publicaciones":publicaciones,"usuarios":usuarios,"categoria":categoria})

def ver(request):
    usuarios=Usuario.objects.all()
    return render(request, "ver.html", {"usuarios":usuarios})

def mod(request):
    usuario=Usuario.objects.all()
    return render(request,"mod.html", {"usuarios":usuario})

def add(request):
    return render(request,"add.html")

def addcategoria(request):
    return render(request,"addcategoria.html")

def readme(request):
    return render(request,"readme.html")

def addpublicacion(request):
    usuarios=Usuario.objects.all()
    categorias=Categoria.objects.all()
    return render(request, "addpublicacion.html", {"usuarios":usuarios,"categorias":categorias})

def registrarPublicacion(request):
    titulo=request.POST['titulo']
    resumen=request.POST['resumen']
    articulo=request.POST['articulo']
    id_categoria=request.POST['id_categoria']
    id_usuario=request.POST['id_usuario']
    publicacion=Publicaciones.objects.create(titulo=titulo,resumen=resumen,contenido=articulo,id_categoria=id_categoria,id_usuario=id_usuario)
    return redirect('/')

def registrarUsuario(request):
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    correo=request.POST['correo']
    telefono=request.POST['telefono']
    tipo=request.POST['tipo_usuario']
    usuario=Usuario.objects.create(nombre=nombre,apellido=apellido,correo=correo,telefono=telefono,tipo=tipo)
    return redirect('/ver')

def registrarCategoria(request):
    nombre=request.POST['nombre']
    categoria=Categoria.objects.create(nombre=nombre)
    return redirect('/addpublicacion')

def eliminarUsuario(request, id):
    usuario=Usuario.objects.get(id_usuario=id)
    usuario.delete()
    return redirect('/ver')

def editarUsuario(request, id):
    usuario=Usuario.objects.get(id_usuario=id)
    return render(request, "editar.html", {'usuario':usuario})

def perfil(request, id):
    usuario=Usuario.objects.get(id_usuario=id)
    return render(request, "perfil.html", {'usuario':usuario})

def articulo(request, id):
    publicacion=Publicaciones.objects.get(id_publicaciones=id)
    usuarios=Usuario.objects.all()
    categoria=Categoria.objects.all()
    return render(request, "post.html", {'publicaciones':publicacion,"usuarios":usuarios,"categorias":categoria})

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
    return redirect('/ver')