from django.urls import path
from . import views 
from web.views import *
from django.contrib.auth.views  import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.feed,name='feed'),
    path('profile/', views.profile,name='profile'),
    path('profile/<str:username>/',views.profile, name='profile'),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='social/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='social/logout.html'),name='logout'),
    path('post/',views.post,name='post'),
    path('edit/',views.editPerfil,name='editar_perfil'),
    path('avatar/',views.agregar_avatar,name='avatar'),
    path('follow/<str:username>/',views.follow,name='follow'),
    path('unfollow/<str:username>/',views.unfollow,name='unfollow'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
