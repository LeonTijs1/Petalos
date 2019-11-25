from django.shortcuts import render
from .models import Flor
from .forms import FlorForm,CustomUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_autent
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'core/index.html')

def productos(request):
    flores=Flor.objects.all()
    return render(request,'core/productos.html',{'lista':flores})

def registro_usuario(request):
    data={
        'form':CustomUserForm()
    }
    if request.method=='POST':
        formulario=CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request, user)
            return redirect(to='HOME')
    return render(request,'registro/registrar.html',data)

def login(request):
    if request.POST:
        usuario=request.POST.get('txtUsuario')
        password=request.POST.get('txtPass')
        use=authenticate(request,username=usuario, password=password)
        if use is not None and use.is_active:
            if use.is_staff:
                login_autent(request,use)
                arreglo={'nombre':usuario,'contraseña':password,'tipo':'administrador'}
                return render(request, 'core/formulario.html',arreglo)
            else:
                arreglo={'nombre':usuario,'contraseña':password,'tipo':'cliente'}
                return render(request, 'core/productos.html',arreglo)       
    return render(request,'registro/login.html')     

@login_required(login_url='/login/')
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
    return render(request,'core/quienes_somos.html')   

@login_required(login_url='/login/')
def eliminar_flor(request,id): 
    mensaje=''
    fl=Flor.objects.get(name=id)  
    try:
        fl.delete()
        mensaje='Flor Eliminada'
    except:
        mensaje='Problemas al eliminar la flor'
    flores=Flor.objects.all()
    return render(request,'core/administracion.html',{'lista':flores,'msg':mensaje})

@login_required(login_url='/login/')
def administrar(request):
    flores=Flor.objects.all()
    return render(request,'core/administracion.html',{'lista':flores})

@login_required(login_url='/login/')
def modificar(request):
    flores=Flor.objects.all()
    return render(request,'core/modificar_flor.html')

@login_required(login_url='/login/')
def modificar_flor(request,id):
    fl=Flor.objects.get(name=id)  
    data = {
        'form':FlorForm(instance=fl) 
    }  
    if request.method == 'POST':
        formulario = FlorForm(data=request.POST, instance=fl, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['msj'] = "Modificado correctamente"
            data['form'] = formulario    
            flores=Flor.objects.all()
        return render(request,'core/administracion.html',{'lista':flores})      
    return render(request,'core/modificar_flor.html',data)

def cerrar_sesion(request):
    logout(request)
    return render(request,'registro/login.html')