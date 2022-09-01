from cgitb import reset
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from web.models import *
from datetime import datetime
from web.forms import *

# Create your views here.
def index(request):
    return render(request, "web/index.html",{"dateTime": datetime.now})

def buscador(request):
    comentarios = Posteo.objects.all()
    
    if request.GET.get("buscar"):
        
        formulario = Busqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            comentarios = Posteo.objects.filter(titulo__icontains = data["buscar"])
        
        return render(request, "web/base_buscador.html", {"comentarios": comentarios, "formulario" : formulario})

    else:
        formulario = Busqueda()
        return render(request, "web/base_buscador.html", {"comentarios": comentarios, "formulario" : formulario})

def formulariosComentarios(request):

    comentarios = Posteo.objects.all()
        
    if request.method == "POST":

        formulario = FormularioPosteo(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            titulo = data.get("titulo")
            contenido = data.get("contenido")
            fecha_publicacion = data.get("fecha_publicacion")

            comentarios = Posteo(titulo=titulo, contenido=contenido, fecha_publicacion=fecha_publicacion)
            comentarios.save()

            return render(request, "web/index.html")
        
        else:
            return HTTPResponse("No valido")
        
    else:
        formulario = FormularioPosteo()
        return render(request, "web/comentarios.html", {"comentarios": comentarios, "formulario" : formulario})