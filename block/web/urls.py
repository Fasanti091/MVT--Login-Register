from django.urls import path
from web.views import *
from registro.views import *
urlpatterns = [
    path('',index,name="inicio"),
    path('buscador/', buscador, name="buscador"),
    path('registro/', registro ,name="registro"),
    path('edit/',editPerfil,name='editar'),
    path('comentarios/', formulariosComentarios, name="comentarios")
    
]
