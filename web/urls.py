from django.urls import path
from web.views import *

urlpatterns = [
    path('',index, name="inicio"),
    path('registro/',registro,name="registro")
    
    
]
