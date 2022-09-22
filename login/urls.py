from django.contrib import admin
from django.urls import path
from .views import *
from login.views import inicio
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='inicio'),#se crea la ruta para inicio
    path('login/', login_request, name='login'),#se crea la ruta para iniciar sesion
    path('register/', register, name='register'),#se crea la ruta para registrar usuario
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),#se crea la ruta para cerrar sesion
    path('electricos/', electricos, name='electricos'),#se crea la ruta para electricos
    path('electrico/<pk>', Electrico_detalle.as_view(), name='electrico_detalle'),#se crea la ruta para electrico detalle
    path('electrico/nuevo/', Electrico_creacion.as_view(), name='electrico_creacion'),#se crea la ruta para electrico creacion
    path('eliminar_electrico/<post_titulo>', eliminar_electrico, name='eliminar_electrico'),#se crea la ruta para eliminar electrico
    path('electrico/editar/<pk>', Electrico_editar.as_view(), name='electrico_editar'),
    path('about/', about, name='about'),#se crea la ruta para about
    path('editar_perfil/', editar_Perfil, name='editar_perfil'),#se crea la ruta para editar perfil
    path('usuario_detalle/', usuario_detalle, name='usuario_detalle'),#se crea la ruta para usuario detalle
    path('agregar_avatar/', agregar_avatar, name='agregar_avatar'),#se crea la ruta para agregar avatar
    path('nuevo_avatar/', nuevo_avatar, name='nuevo_avatar'),#se crea la ruta para nuevo avatar
    
]