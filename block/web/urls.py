from django.urls import path
from web.views import *
from registro.views import *
urlpatterns = [
    path('',index),
    path('comentarios/', comentarios),
    path('registro/',registro,name="registro")
]
