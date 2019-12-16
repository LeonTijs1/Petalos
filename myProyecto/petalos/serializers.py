from rest_framework import serializers
from .models import Flor, Compra

class  FlorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flor
        fields = ['name','imagen','cantidad','precio','descripcion']

class  CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['usuario','name','precio','cantidad','total']