from .models import mensaje
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def mensajes(request):#Funcion para ver los mensajes 
    mensajes= mensaje.objects.filter(emisor=request.user)#se obtienen los mensajes del usuario
    mensajes= mensaje.objects.filter(receptor=request.user) 
    return render(request, 'mensajes.html', {'mensajes':mensajes})#se redirecciona a la pagina de mensajes con los mensajes obtenidos

class Mensaje_creacion(CreateView, LoginRequiredMixin):#vista de creacion de mensaje
    model= mensaje#modelo de post
    fields= ['emisor','receptor', 'contenido']#campos del modelo
    template_name= 'mensaje_form.html'#plantilla de creacion de mensaje
    success_url= reverse_lazy("mensajes")#redireccion a la misma pagina