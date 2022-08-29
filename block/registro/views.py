import re
from django.shortcuts import render ,redirect
from web.models import *
from django.contrib import messages
from registro.forms import CustomUserCreationForm,UserEditForm
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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
            login(request, user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="/")
        data["form"]= formulario
    return render( request,'registration/registro.html', data)


@login_required
def editPerfil(request):
    
    if request.method == "GET":
        form = UserEditForm()
        return render(request,"registration/update_user.html",{"form":form})
    else:
        form = UserEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = request.user
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            
            usuario.save()
        return redirect("inicio")
    