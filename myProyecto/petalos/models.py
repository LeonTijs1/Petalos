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

