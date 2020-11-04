from django.shortcuts import render, redirect
from .models import Usuario
from .models import Producto
from django.contrib import messages
# Create your views here.


#USUARIO
def index(request):
    print("ok, estamos en la vista")
    context={}
    return render(request,'usuario/index.html', context)

def mision(request):
    print("ok, estamos en la vista")
    context={}
    return render(request,'usuario/mision.html', context)

def about(request):
    print("ok, estamos en la vista")
    context={}
    return render(request,'usuario/about.html', context)

def contact(request):
    print("ok, estamos en la vista")
    context={}
    return render(request,'usuario/contact.html', context)

def registrarse(request):
    print("ok, estamos en la vista")
    if request.method == "POST":
        mi_tipo_usuario = request.POST['user_type']
        mi_fecha_nacimiento = request.POST['user_fechaNac']
        mi_email = request.POST['user_email']
        mi_username = request.POST['username']
        mi_password = request.POST['user_password']
        mi_genero = request.POST['user_genero']
        mi_foto = request.FILES['user_foto']
        mi_activo = request.POST['user_activo']
        if mi_email != "":
           try:
               usuario = Usuario()

               usuario.tipo_usuario = mi_tipo_usuario
               usuario.fecha_nacimiento = mi_fecha_nacimiento
               usuario.email = mi_email
               usuario.username = mi_username
               usuario.password = mi_password
               usuario.genero = mi_genero
               usuario.foto = mi_foto
               usuario.activo = mi_activo

               usuario.save()

               mensaje = "Usuario registrado correctamente."
               messages.success(request, mensaje)
               return redirect('index')
           except usuario.DoesNotExist:
               mensaje = "El Usuario no existe."
               messages.error(request, mensaje)
        else:
            mensaje = "Usuario registrado correctamente."
            messages.error(request, mensaje)
    else:
        mensaje = "Error."
        messages.error(request, mensaje)

    context={}
    return render(request,'usuario/registrarse.html', context)

def login(request):
    print("ok, estamos en la vista")
    usuario = Usuario()

    if request.method == "POST":
        print("Entré al primer IF")
        mi_email = request.POST['email']
        mi_pass = request.POST['password']
        if mi_email != "":
            print("Entré al segundo IF")
            try:
                print("Entré al TRY")
                user_email = Usuario.objects.filter(email=mi_email)
                print(user_email)
                user_pass = Usuario.objects.filter(password=mi_pass)
                print(user_pass)
                if user_email == mi_email: #Aquí se cae
                    print("email validado")
                    return redirect('index')
                else:
                    print("Me caí en el email")
                    messages.error(request, "Error al Iniciar Sesión")
                    return redirect('login')
            except usuario.DoesNotExist:
                user_email = None
                user_pass = None
    context={}
    return render(request,'usuario/login.html', context)



#PRODUCTO
def agregar_producto(request):
    print("ok, estamos en la vista")
    if request.method == "POST":
        print("Entré al primer IF")
        producto = Producto()
        producto.nombre_producto = request.POST.get('nombre_producto')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.foto = request.FILES.get('foto')
        producto.activo = request.POST.get('activo')
        try:
            print("Entré al TRY")
            producto.save()
            messages.success(request, 'Producto agregado correctamente.')
        except:
            print("Me caí en el except )=")
            messages.error(request, 'No se pudo modificar el Producto.')
        return redirect('listar_producto')
    else:
        print("No entré al IF")
    context={}
    return render(request, 'producto/agregar_producto.html', context)




def listar_producto(request):
    print("ok, estamos en la vista")
    producto = Producto.objects.all()
    context={'producto':producto}
    return render(request,'producto/listar_producto.html', context)


def eliminar_producto(request, id):
    print("ok, estamos en la vista")
    producto = Producto.objects.get(id_producto=id)

    try:
        producto.delete()
        mensaje = "Producto eliminado."
        messages.success(request, mensaje)
    except:
        mensaje = "Producto NO eliminado."
        messages.error(request, mensaje)
    context={}
    return redirect('listar_producto')


def modificar_producto(request, id):
    print("ok, estamos en la vista")
    producto = Producto.objects.get(id_producto=id)
    context={'producto':producto}
    if request.method == "POST":
        print("Entré al primer IF")
        producto = Producto()
        producto.id_producto = request.POST.get('id_producto')
        producto.nombre_producto = request.POST.get('nombre_producto')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.foto = request.FILES.get('foto')
        producto.activo = request.POST.get('activo')
        try:
            print("Entré al TRY")
            producto.save()
            messages.success(request, 'Producto modificado correctamente.')
        except:
            print("Me caí en el except )=")
            messages.error(request, 'No se pudo modificar el Producto.')
        return redirect('listar_producto')
    else:
        print("No entré al IF")
    return render(request,'producto/modificar_producto.html',context)

