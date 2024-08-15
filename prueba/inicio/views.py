from django.shortcuts import render, HttpResponse

# Create your views here.

def contacto(request):
    return render(request,"inicio/contacto.html")

def formulario(request):
    return render(request,"inicio/formulario.html")

def seguridad(request):
    return render(request,"inicio/seguridad.html")

def registros(request):
    return render(request,"registros/principal.html")

def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request, "inicio/seguridad.html", {'nombre':nombre})