from django.shortcuts import render ,redirect
from web.models import *
from django.contrib import messages
from registro.forms import CustomUserCreationForm
from django.contrib.auth import authenticate , login

# Create your views here.


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
            return redirect(to="/")
        data["form"]= formulario
    return render( request,'registration/registro.html', data)