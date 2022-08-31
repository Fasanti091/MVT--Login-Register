from django.urls import path
from web.views import *
from registro.views import *
urlpatterns = [
    path('',index,name="inicio"),
    path('comentarios/', comentarios, name="comentarios"),
    path('registro/', registro ,name="registro"),
    path('edit/',editPerfil,name='editar')
    
]
