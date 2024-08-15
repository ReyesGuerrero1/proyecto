from django.shortcuts import render
from .models import Alumnos, ComentarioContacto 
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
#accedemos al modelo Alumnos que contiene la estructura de la tabla

# Create your views here.

def registros(request):
    alumnos=Alumnos.objects.all()
    #all recupera todos los objetos del modelo(registro de la tabla alumnos)
    return render(request, "registros/principal.html",{'alumnos':alumnos})
#indicamos el lugar donde se renderizará el resultado de esta vista.
#y enviamos la lista de alumnos
def registrar(request):
    if request.method == "POST":
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():#si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'registros/contacto.html')
        form = ComentarioContactoForm()
        return render(request, 'registros/contacto.html',{'form':form})

def contacto(request):
        return render(request,"registros/contacto.html")

def comentarioContacto(request):
        comentario=ComentarioContacto.objects.all()
        return render(request,"registros/comentario.html",{'comentarios':comentario})

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
     comentario = get_object_or_404(ComentarioContacto, id=id)
     if request.method=='POST':
          comentario.delete()
          comentarios = ComentarioContacto.objects.all()
          return render(request,"registros/confirmarEliminacion.html",{'comentarios':comentarios})
     return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
#get permite establecer una condicionante a la consulta y recupera el objetos
#del modelo que cumple la condición (registro de la tabla ComentariosContacto.
#get se emplea cuando se sabe que solo hay un objeto que coincide con su
#consulta.
    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados.


def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
#Referenciamos que el elemento del formulario pertenece al comentario
# ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentario.html",{'comentarios':comentarios})
#Si el formulario no es valido nos regresa al formulario para verificar
#datos
    return render(request,"registros/formEditarComentario.html",{'comentarios':comentario})

def comentarios(request):
    coment = ComentarioContacto.objects.all()
    return render(request,"registros/comentarios.html",{'comentarios':coment})

def consultar1(request):
     alumnos=Alumnos.objects.filter(carrera="Ti")
     return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
     alumnos=Alumnos.objects.filter(carrera="Ti").filter(turno="Matutino")
     return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
     alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
     return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
     alumnos=Alumnos.objects.filter(turno__contains="Vesp")
     return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
     alumnos=Alumnos.objects.filter(turno__in=["Juan", "Ana"])
     return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2022, 7, 1)
    fechaFin = datetime.date(2024, 7, 17)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
     alumnos=Alumnos.objects.filter(comentario__coment_contains="No inscrito")
     return render(request,"registros/consultas.html",{'alumnos':alumnos})