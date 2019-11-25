from django.contrib import admin
from django.urls import path
from .views import home,productos,formulario,quienes,eliminar_flor,administrar,modificar,modificar_flor,login,registro_usuario,cerrar_sesion

urlpatterns = [
    path('',home,name='HOME'),   
    path('productos/',productos,name='PROD'),
    path('formulario/',formulario,name='FORM'),
    path('quienes/',quienes,name='WHO'),
    path('eliminar_flor/<id>/',eliminar_flor,name='ELIMINAR'),
    path('modificar_flor/<id>/',modificar_flor,name='MODIFICAR'),
    path('administrar/',administrar,name='ADMIN'),
    path('modificar/',modificar,name='MOD'),
    path('login/',login,name='LOG'),
    path('registro/',registro_usuario,name='REGISTRO'),
    path('cerrar_sesion/',cerrar_sesion,name='LOGOUT'),   
]