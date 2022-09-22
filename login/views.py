from tkinter import N
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from login.forms import UserRegisterForm, UserEditForm, Avatar_Form
from .models import  Post, Avatar
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.


def inicio(request): #vista de inicio
    return render (request, "inicio.html")

def login_request(request): # vista para loguear
    if request.method=="POST":#si el metodo es post
        form= AuthenticationForm(request, data=request.POST)#se crea un formulario con los datos del request
        if form.is_valid:#si el formulario es valido
            usu= request.POST['username']#se obtiene el usuario
            clave= request.POST['password']#se obtiene la clave

            usuario= authenticate(username=usu, password=clave)#se autentica el usuario

            if usuario is not None:#si el usuario no es nulo
                login(request, usuario)#se loguea el usuario
                return render(request, 'inicio.html', {'form':form, 'mensaje':f"Bienvenido {usuario}"})# se redirecciona a la pagina de inicio
            else:#si el usuario es nulo
                return render(request, 'login.html', {'form':form, 'mensaje':f"Usuario o contraseña incorrectos"})#se redirecciona a la pagina de login
        else:#si el formulario no es valido
            return render(request, 'login.html', {'form':form, 'mensaje':f"FORMULARIO INVALIDO"})#se redirecciona a la pagina de login
    else:#si el metodo no es post
        form= AuthenticationForm()#se crea un formulario
        return render(request, 'login.html', {'form':form})#se redirecciona a la pagina de login

def register(request):#vista para registrar
    if request.method == 'POST':#si el metodo es post
        form= UserRegisterForm(request.POST)#se crea un formulario con los datos del request
        if form.is_valid():#si el formulario es valido
            username= form.cleaned_data["username"]#se obtiene el usuario

            form.save()#se guarda el usuario
            return render(request, 'inicio.html', {'form':form, 'mensaje':f"Usuario Creado: {username}"})#se redirecciona a la pagina de inicio
    else:#si el metodo no es post
        form= UserRegisterForm()#se crea un formulario
    return render (request, 'register.html', {'form':form})#se redirecciona a la pagina de registro

@login_required#se requiere que el usuario este logueado para acceder a la vista
def electricos(request):#vista de electricos
    posts= Post.objects.all()#se obtienen todos los posts
    return render(request, 'electricos.html', {'posts':posts})#vista para editar el avatar

class Electrico_detalle(DetailView, LoginRequiredMixin):#vista de detalle de electricos
    model= Post#modelo de post
    template_name= "electrico_detalle.html"#plantilla de detalle de electricos

class Electrico_creacion(CreateView, LoginRequiredMixin):#vista de creacion de electricos
    model= Post#modelo de post
    fields= ['autor','titulo', 'texto', 'imagen', 'fecha_creacion']#campos del modelo
    template_name= 'electrico_form.html'#plantilla de creacion de electricos
    success_url= reverse_lazy("electricos")#redireccion a la misma pagina

@login_required
def eliminar_electrico(request, post_titulo): #vista de eliminar electricos
    post= Post.objects.get(titulo=post_titulo)#se obtiene el post
    post.delete()#se elimina el post

    postt= Post.objects.all()#se obtienen todos los posts
    return render(request, 'inicio.html', {"postt":postt}) # retorno a inicio


class Electrico_editar(UpdateView, LoginRequiredMixin):#vista de editar electricos
    model= Post#modelo de post
    fields= ['autor','titulo', 'texto', 'imagen', 'fecha_creacion']#campos del modelo
    template_name= 'electrico_form.html'#plantilla de editar electricos
    success_url= reverse_lazy("electricos")#redireccion a la misma pagina

@login_required
def about(request):#vista de about
    return render(request, "about.html")#se redirecciona a la pagina de about

@login_required
def editar_Perfil(request):#vista de editar perfil
    usuario=request.user#se obtiene el usuario

    if request.method =='POST':#si el metodo es post
        formulario=UserEditForm(request.POST, instance=usuario)#se crea un formulario con los datos del request
        if formulario.is_valid():#si el formulario es valido
            informacion=formulario.cleaned_data#se obtiene la informacion del formulario
            usuario.set_password(informacion['password1'])#se obtiene la contraseña
            usuario.save()#se guarda el usuario

            return render(request, 'inicio.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})#se redirecciona a la pagina de inicio
    else:#si el metodo no es post
        formulario=UserEditForm(instance=usuario)#se crea un formulario con los datos del request
    return render(request, 'editar_perfil.html', {'formulario':formulario, 'usuario':usuario.username})#se redirecciona a la pagina de editar perfil


@login_required
def usuario_detalle(request): #vista para detalle de usuario
    usuario= User.objects.all() #se obtiene el usuario
    imagen= Avatar.objects.filter(user= request.user.id) #se obtiene la imagen del usuario
    if len(imagen) !=0:#si la longitud de la imagen no es 0
        imagen=imagen[0].imagen.url#se obtiene la imagen
        return render(request, 'usuario_detalle.html', {'usuario':usuario, 'imagen':imagen}) #se redirecciona a la pagina de usuario detalle
    else:#si la imagen no es nula
        imagen= 'avatar1.jpg'#se asigna la imagen por defecto
        return render(request, 'usuario_detalle.html', {'usuario':usuario, 'imagen':imagen}) #se redirecciona a la pagina de usuario detalle
    

def agregar_avatar(request): #vista para agregar actualizar avatar
    if request.method == 'POST': #si el metodo es post
        imagen= Avatar.objects.filter(user= request.user.id)
        if len(imagen) !=0:#si la longitud de la imagen no es 0
                formulario= Avatar_Form(request.POST, request.FILES) #se crea un formulario con los datos del request
                if formulario.is_valid(): #si el formulario es valido
                    avatar_viejo= Avatar.objects.get(user=request.user)#se obtiene el avatar viejo del usuario
                    if(avatar_viejo.imagen):#si el avatar existe
                        avatar_viejo.delete()# se elimina el avatar
                    avatar= Avatar(user=request.user, imagen=formulario.cleaned_data['imagen']) #se crea un avatar con los datos del request
                    avatar.save() #se guarda el avatar
                    return render(request, 'inicio.html', {'usuario':request.user, 'mensaje':'se agrego el nuevo avatar'})#se redirecciona a la pagina de inicio
        else:#si la imagen no es nula
            return render(request, 'nuevo_avatar.html', {'formulario':Avatar_Form()})#se redirecciona a la pagina de nuevo avatar
    else: #si el metodo no es post
        formulario= Avatar_Form() #se crea un formulario
        return render(request, 'agregar_avatar.html', {'formulario':formulario, 'usuario':request.user}) #se redirecciona a la pagina para agregar un avatar


def nuevo_avatar(request): #vista para agregar el primer avatar
    if request.method == 'POST': #si el metodo es post
        imagen= Avatar.objects.filter(user= request.user.id) #se obtiene el avatar del usuario
        if len(imagen) ==0:#si la longitud de la imagen no es 0
            formulario= Avatar_Form(request.POST, request.FILES) #se crea un formulario con los datos del request
            if formulario.is_valid(): #si el formulario es valido
                avatar= Avatar(user=request.user, imagen=formulario.cleaned_data['imagen']) #se crea un avatar con los datos del request
                avatar.save() #se guarda el avatar
                return render(request, 'inicio.html', {'usuario':request.user, 'mensaje':'se agrego el nuevo avatar'})#se redirecciona a la pagina de inicio
        else:#si la imagen no es nula
            return render(request, 'agregar_avatar.html', {'formulario':Avatar_Form()})#se redirecciona a la pagina de nuevo avatar
    else: #si el metodo no es post
        formulario= Avatar_Form() #se crea un formulario
    return render(request, 'nuevo_avatar.html', {'formulario':formulario, 'usuario':request.user}) #se redirecciona a la pagina de nuevo avatar
