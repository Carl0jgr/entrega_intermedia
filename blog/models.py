from django.db import models
from .choices import tipo_usuario

# Create your models here.
class Usuario(models.Model):
    id_usuario=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField()
    telefono=models.IntegerField()
    tipo=models.CharField(max_length=1)

    def __str__(self):
        return "({}) {} {} [{}]".format(self.id_usuario, self.nombre, self.apellido, self.tipo)

class Categoria (models.Model):
    id_categoria=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return "({}) {}".format(self.id_categoria, self.nombre)

class Publicaciones (models.Model):
    id_publicaciones=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=50)
    id_categoria=models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.RESTRICT)

    def __str__(self):
        return "({}) {} [{}] --{}--".format(self.id_publicaciones, self.titulo, self.id_categoria, self.id_usuario)
