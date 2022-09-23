from django.urls import path
#from views import *
#from . import views
from blog.views import *

urlpatterns = [

    path('', home),
    path('home.html', home),
    path('descripcion/', descripcion),
    path('descripcion.html', descripcion),
    path('publicaciones.html', publicaciones),
    path('publicaciones/', publicaciones),
    path('ver',ver),
    path('ver.html',ver),
    path('mod',mod),
    path('add',add),
    path('registarUsuario/',registrarUsuario),
    path('editarUsuario/<id>/',editarUsuario),
    path('modificarUsuario/',modificarUsuario),
    path('eliminarUsuario/<id>/',eliminarUsuario),
    path('addpublicacion',addpublicacion)
    
    
]