from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):#Formulario para registrar usuarios
    email= forms.EmailField()#Campo email
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)#Campo contraseña
    password2 = forms.CharField(label='Confirme la contraseña', widget=forms.PasswordInput)#Campo confirmacion de contraseña

    class Meta:
        model = User#Modelo de usuario
        fields = ['username', 'email', 'password1', 'password2']#Campos del modelo
        help_texts = {k:"" for k in fields}#Ayuda para los campos del modelo

class UserEditForm(UserCreationForm):#Formulario para editar usuarios
    password1 = forms.CharField(label=' Nueva Contraseña', widget=forms.PasswordInput)#Campo contraseña
    password2 = forms.CharField(label='Confirme la contraseña', widget=forms.PasswordInput)#Campo confirmacion de contraseña

    first_name= forms.CharField(max_length=50)#Campo nombre
    last_name= forms.CharField(max_length=50)#Campo apellido

    class Meta:
        model = User#Modelo de usuario
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name'] #Campos del modelo
        help_texts = {k:"" for k in fields}#Ayuda para los campos del modelo

class Avatar_Form(forms.Form):#formulario de avatar
    imagen = forms.ImageField(label='imagen')#se agrega el campo imagen