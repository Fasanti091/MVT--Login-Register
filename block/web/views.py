from django.shortcuts import render
from web.models import *


# Create your views here.
def index(request):
    return render(request, "web/index.html")

def comentarios(request):

    comentarios = Posteo.objects.all()

    return render(request, "web/comentarios.html", {"comentarios":comentarios})
