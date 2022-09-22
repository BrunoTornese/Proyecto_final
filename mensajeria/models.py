from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enviador')#Relacion con el usuario que envia el mensaje
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')#Relacion con el usuario que recibe el mensaje
    contenido = models.TextField()#Contenido del mensaje
