from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('flores', FlorViewSet)
router.register('compras', CompraViewSet)


urlpatterns = [
    path('',home,name='HOME'),   
    path('productos/',productos,name='PROD'),
    path('formulario/',formulario,name='FORM'),
    path('quienes/',quienes,name='WHO'),
    path('eliminar_flor/<id>/',eliminar_flor,name='ELIMINAR'),
    path('modificar_flor/<id>/',modificar_flor,name='MODIFICAR'),
    path('admistracion/',admistracion,name='ADMI'),
    path('registro/',registro_usuario,name='REG_USER'),
    path('version/',version,name='VER'),
    path('login/',login,name='LOGIN'),
    path('agregar_carro/<id>/',carro_compras,name='AGREGAR_CARRO'),
    path('carro/',carros,name='CARRO'),
    path('carro_mas/<id>/',carro_compras_mas,name='CARRO_MAS'),
    path('carro_menos/<id>/',carro_compras_menos,name='CARRO_MENOS'),
    path('grabar_carro/',grabar_carro,name='GRABAR_CARRO'),
    path('api/', include(router.urls)),
    path('guardar-token/',guardar_token, name='guardar_token'),
    path('consejo/',consejo,name='CONS')
]