from django.shortcuts import render,redirect
from .models import Flor,Compra
from django.contrib.auth.models import User
from .forms import FlorForm, CustomUserForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import authenticate,logout,login as login_autent
from .clases import elemento


# Create your views here.
def home(request):
    return render(request,'core/index.html')

def productos(request):
    flores=Flor.objects.all()
    return render(request,'core/productos.html',{'lista':flores})

@permission_required('petalos.add_flor')
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
        return redirect(to='ADMI')
    return render(request,'core/formulario.html')

def quienes(request):   
    return render(request,'core/quienes_somos.html')   

@permission_required('petalos.add_flor')
def eliminar_flor(request,id):  
    mensaje=''
    fl=Flor.objects.get(name=id)  
    try:
        fl.delete()
        mensaje='Flor Eliminada'
    except:
        mensaje='Problemas al eliminar'     
    flores=Flor.objects.all()
    return render(request,'core/admistracion.html',{'lista':flores,'msg':mensaje})

@permission_required('petalos.add_flor')
def modificar_flor(request,id):
    fl=Flor.objects.get(name=id)  
    data = {
        'form':FlorForm(instance=fl) 
    }  
    if request.method == 'POST':
        formulario = FlorForm(data=request.POST, instance=fl, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['form'] = formulario
        return redirect(to='ADMI')
    return render(request,'core/modificar.html',data)

@login_required
def admistracion(request):
    flores=Flor.objects.all()
    return render(request,'core/admistracion.html',{'lista':flores})

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }   
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autentificar
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login_autent(request, user)
            return redirect(to='HOME')            
    return render(request,'registration/registrar.html', data)

@login_required
def version(request):
    return render(request,'core/version.html')

def login(request):
    if request.POST:
        usuario=request.POST.get("txtUsuario")
        password=request.POST.get("txtPass")
        us=authenticate(request,username=usuario,password=password)
        msg=''    
        request.session["carritox"] = []        
        print('realizado')
        if us is not None and us.is_active:
            login_autent(request,us)#autentificacion de login            
            return render(request,'core/index.html')
        else:
            return render(request,'registration/login.html')
    return render(request,'registration/login.html')

##########
#Carro de compra 

@login_required(login_url='/login/')
def carros(request):
    x=request.session["carritox"]
    suma=0
    for item in x:
        suma=suma+int(item["total"])           
    return render(request,'core/carro.html',{'x':x,'total':suma})

@login_required(login_url='/login/')
def grabar_carro(request):
    x=request.session["carritox"]    
    usuario=request.user.username
    suma=0
    try:
        for item in x:        
            name=item["nombre"]
            precio=int(item["precio"])
            cantidad=int(item["cantidad"])
            total=int(item["total"])        
            compra=Compra(
                usuario=usuario,
                name=name,
                precio=precio,
                cantidad=cantidad,
                total=total,
            )
            compra.save()
            suma=suma+int(total)  
            print("reg grabado")                 
        mensaje="Flor(es) compradas"
        request.session["carritox"] = []    
    except:
        mensaje="Error en la compra"            
    return render(request,'core/carro.html',{'x':x,'total':suma,'mensaje':mensaje})

@login_required(login_url='/login/')
def carro_compras(request,id):
    f=Flor.objects.get(name=id)
    x=request.session["carritox"]
    el=elemento(1,f.name,f.precio,1)
    sw=0
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            sw=1
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    if sw==0:
        clon.append(el.toString())
    x=clon    
    request.session["carritox"]=x
    flores=Flor.objects.all()    
    mensaje='Flor guardada, vaya al carrito de compras para ver su compra :D'  
    return render(request,'core/productos.html',{'lista':flores,'total':suma,'mensaje':mensaje})

@login_required(login_url='/login/')
def carro_compras_mas(request,id):
    f=Flor.objects.get(name=id)
    x=request.session["carritox"]
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]        
    return render(request,'core/carro.html',{'x':x,'total':suma})

@login_required(login_url='/login/')
def carro_compras_menos(request,id):
    f=Flor.objects.get(name=id)
    x=request.session["carritox"]
    clon=[]
    suma=0
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            cantidad=int(cantidad)-1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total)
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]    
    return render(request,'core/carro.html',{'x':x,'total':total})

