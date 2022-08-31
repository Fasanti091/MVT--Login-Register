from django.shortcuts import render
from web.models import *
from datetime import datetime
from web.forms import *

# Create your views here.
def index(request):
    return render(request, "web/index.html",{"dateTime": datetime.now})

def comentarios(request):

    comentarios = Posteo.objects.all()

    if request.GET.get("buscar"):
        
        formulario = Busqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            comentarios = Posteo.objects.filter(titulo__icontains = data["buscar"])
        
        return render(request, "web/comentarios.html", {"comentarios": comentarios, "formulario" : formulario})

    else:
        formulario = Busqueda()
        return render(request, "web/comentarios.html", {"comentarios": comentarios, "formulario" : formulario})


