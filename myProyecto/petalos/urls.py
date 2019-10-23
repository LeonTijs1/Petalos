from django.contrib import admin
from django.urls import path
from .views import home,productos,formulario,quienes,eliminar_flor

urlpatterns = [
    path('',home,name='HOME'),   
    path('productos/',productos,name='PROD'),
    path('formulario/',formulario,name='FORM'),
    path('quienes/',quienes,name='WHO'),
    path('eliminar_flor/<id>',eliminar_flor,name='ELIMINAR'),
]