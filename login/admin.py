from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Post)#Registramos el modelo Post
admin.site.register(models.Avatar)#Registramos el modelo Avatar