from django.shortcuts import render ,redirect
from web.models import *
from django.contrib import messages
from web.forms import CustomUserCreationForm
from django.contrib.auth import authenticate , login

# Create your views here.
def index(request):
    return render(request, "web/index.html")

def comentarios(request):

    comentarios = Posteo.objects.all()

    return render(request, "web/comentarios.html", {"comentarios":comentarios})

def registro(request):
    data ={
        'form':CustomUserCreationForm()
    }
    if request.method == "POST":
        formulario = CustomUserCreationForm(data =request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="inicio")
        data["form"]= formulario
    return render( request,'registration/registro.html', data)
