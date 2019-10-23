from django.shortcuts import render
from .models import Flor

# Create your views here.
def home(request):
    return render(request,'core/index.html')

def productos(request):
    return render(request,'core/productos.html')

def formulario(request):
    if request.POST:
        nombre=request.POST.get("txtNombre")
        imagen=request.FILES.get("imagen")
        precio=request.POST.get("txtPrecio")
        descripcion=request.POST.get("txtDescripcion")
        cantidad=request.POST.get("txtCantidad")
        #crear la flor
        flor=Flor(
            name=nombre,
            imagen=imagen,
            cantidad=cantidad,
            precio=precio,
            descripcion=descripcion
        )
        #guarda los datos de la flor   
        flor.save()
        return render(request,'core/formulario.html')
    return render(request,'core/formulario.html')

def quienes(request):
    flores=Flor.objects.all()
    return render(request,'core/quienes_somos.html',{'lista':flores})   

def eliminar_flor(request,id): 
    flores=Flor.objects.get(name=id)
    mensaje=''
    try:
        peli.delete()
        mensaje='Flor Eliminada'
    except:
        mensaje='Problemas al eliminar'
    flores=Flor.objects.all()
    return render(request,'core/quienes_somos.html',{'lista':flores,'msg':mensaje})
