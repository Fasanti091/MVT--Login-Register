
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from web.models import *
from django.contrib.auth.models import User
from datetime import datetime
from web.forms import *
from social.views import *
from social.models import *
from django.views.generic import ListView,DetailView
# Create your views here.
def index(request):
    return render(request, "web/index.html",{"dateTime": datetime.now})

def nosotros(request):
    return render(request, "web/nosotros.html")

def frameworks(request):
    return render(request, "web/frameworks.html")

class UsuariosList(ListView):
    model = User
    template_name = "web/lista_usuarios.html"
    
class UserDetail(DetailView):
    model = User
    template_name = "web/detalles_usuarios.html"
    

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

            return redirect("comentarios")
        
        else:
            return HTTPResponse("No valido")
        
    else:
        formulario = FormularioPosteo()
        return render(request, "web/comentarios.html", {"comentarios": comentarios, "formulario" : formulario})

def borrar_comentarios(request, id_titulo):
    try:
        titulo = Posteo.objects.get(id=id_titulo)
        titulo.delete()

        return redirect("comentarios")
    except:
        return HTTPResponse("No valido")

def editar_comentarios(request,id_titulo):
    if request.method == "GET":
        formulario = FormularioPosteo()
        return render(request, "web/comentarios_actualizar.html",{"formulario": formulario})

    else:
        formulario = FormularioPosteo(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            try:
                posteo = Posteo.objects.get(id=id_titulo)
                posteo.titulo = data.get("titulo")
                posteo.contenido = data.get("contenido")
                posteo.save()

            except:
                return HTTPResponse("Error en la actualizacion")
        return redirect("comentarios")