from django.db import models

# Create your models here.
class Posteo(models.Model):
    
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=350)
    fecha_publicacion = models.DateField()

# class Blog(models.Model):

#     titulo = models.CharField(max_length=100)
#     subtitulo = models.CharField(max_length=100)
#     cuerpo = models.CharField(max_length=100),
#     auto