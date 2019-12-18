from django import forms
from django.forms import ModelForm
from .models import Flor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FlorForm(ModelForm):

    name = forms.CharField(min_length=3,max_length=10)
    descripcion = forms.CharField(min_length=4,max_length=100)
    cantidad = forms.IntegerField(min_value=1,max_value=5)
    precio = forms.IntegerField(min_value=3,max_value=7)

    class Meta:
        model = Flor
        fields = ['name', 'imagen','cantidad','precio','descripcion']

class CustomUserForm():

    first_name = forms.CharField(min_length=4,max_length=20)
    password1 = forms.CharField(min_length=8,max_length=20)
    password2 = forms.CharField(min_length=8,max_length=20)
    username = forms.CharField(min_length=6,max_length=20)

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']