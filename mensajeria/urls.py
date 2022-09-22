from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from login.views import inicio
urlpatterns = [
    path('', inicio, name='inicio'),
    path('mensajes', mensajes, name='mensajes'), # url para ver los mensajes
    path('mensaje/nuevo/', Mensaje_creacion.as_view(), name='mensaje_creacion'), # url para crear un mensaje
]