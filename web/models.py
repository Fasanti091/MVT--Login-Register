from django.db import models

# Create your models here.
class Posteo(models.Model):
    
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=350)
    fecha_publicacion = models.DateField()

