from django.db import models

# Create your models here.

class Flor(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    imagen=models.ImageField(upload_to="flores",null=True)
    cantidad=models.IntegerField()
    precio=models.IntegerField()
    descripcion=models.TextField()

    def __str__(self):
        return self.name

class Compra(models.Model):
    usuario=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    total=models.IntegerField()

    def __str__(self):
        return str(self.usuario)+' '+str(self.name)