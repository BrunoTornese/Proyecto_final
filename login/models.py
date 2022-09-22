from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
   

class Post(models.Model):#Modelo de post
    autor= models.ForeignKey(User, on_delete=models.CASCADE, default=User)#Relacion con el usuario
    titulo= models.CharField(max_length=200)#Titulo del post
    texto = RichTextField(blank=True, null=True)#Texto del post
    imagen= models.ImageField(upload_to='', blank=True)#Imagen del post
    fecha_creacion= models.DateTimeField(default=timezone.now)#Fecha de creacion del post

    def publicacion(self):#Funcion para obtener la fecha de creacion del post
        self.fecha_creacion= timezone.now()#se obtiene la fecha de creacion del post
        self.save()#se guarda el post
    
    def __str__(self):#Funcion para obtener el titulo del post
        return self.titulo#se obtiene el titulo del post

class Avatar(models.Model):#modelo de avatar
    user= models.ForeignKey(User, on_delete=models.CASCADE)#campo usuario
    imagen= models.ImageField(upload_to='', null=True, blank=True)#campo imagen 