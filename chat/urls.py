
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from BLOG.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='chat-home'),
    path('login/', auth_views.LoginView.as_view(template_name="chat/login.html"), name='chat-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="chat/logout.html"), name='chat-logout'),
    path('register/', views.register, name='chat-register'),
    path('home/', views.home, name='chat-home'),
    path('profile/', views.profile, name='chat-profile'),
    path('send/', views.send_chat, name='chat-send'),
    path('renew/', views.get_messages, name='chat-renew'),
    path("agregarAvatar/", AgregarAvatar, name="agregarAvatar"),
    path("aboutMe/", aboutMe, name="aboutMe"),
    path("leerMas", leerMas, name="leerMas"),
    path("leerUsuarios/", leerUsuarios, name="leerUsuarios"),
    path("Crear/", formularioComentario.as_view(), name="Crear"),
    path("List/", listComentario.as_view(), name="Lista"),
    #path("Delete/<id>", deleteComentario, name="Borrar"),
    path("Delete/<pk>", deleteComentario.as_view(), name="Borrar"),
    path("Update/<pk>", updateComentario.as_view(), name="Editar"),
]   

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
