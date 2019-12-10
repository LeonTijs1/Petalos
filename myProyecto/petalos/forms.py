from django import forms
from django.forms import ModelForm 
from .models import Flor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FlorForm(ModelForm):
    
    class Meta:
        model = Flor
        fields = ['name', 'imagen','cantidad','precio','descripcion']

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']