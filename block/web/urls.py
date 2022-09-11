
from django.urls import path
from web.views import *
from social.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',index,name="inicio"),
    path('buscador/', buscador, name="buscador"),
    path('comentarios/', formulariosComentarios, name="comentarios"),
    path('borrar_comentarios/<int:id_titulo>', borrar_comentarios, name="borrar_comentarios"),
    path('editar_comentarios/<int:id_titulo>', editar_comentarios, name="editar_comentarios"),
    path('nosotros/', nosotros, name="nosotros"),
    path('frameworks/', frameworks, name="frameworks"),
    path('lista_usuarios/',UsuariosList.as_view(), name="lista_usuarios"),
    path('usuarios/<pk>',UserDetail.as_view(),name="detalles")
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
