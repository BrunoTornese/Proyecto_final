from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from login.models import Avatar
@login_required
def inicio(request): #vista de inicio
    return render (request, "inicio.html")#renderiza la vista inicio.html

