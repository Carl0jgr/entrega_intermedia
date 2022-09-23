from django.urls import path
#from views import *
#from . import views
from blog.views import *

urlpatterns = [

    path('', home),
    path('home.html', home),
    path('usuarios/', usuarios),
    path('usuarios.html', usuarios),
    path('descripcion/', descripcion),
    path('descripcion.html', descripcion),
    path('publicaciones.html', publicaciones),
    path('publicaciones/', publicaciones),
    
    
]