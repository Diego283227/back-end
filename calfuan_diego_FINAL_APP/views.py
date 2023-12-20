from django.shortcuts import render, redirect, loader
from .serializers import InscritosSerializers, InstitucionSerializers, AutorSerializer
from .models import Inscritos, Institucion, Autor
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404, JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from calfuan_diego_FINAL_APP.forms import FormInscritos, FormInstitucion


# Create your views here.

def index(request):
    template = loader.get_template("index.html")
    context = {"titulo": "usuario",
              "carrera": "Ing en informatica",
              "email": "Diegocalfuan@gmail.com",
              "nombres":"Diego Alberto",
              "Apellidos": "Calfuan Calfuan",
              "edad": "21 años"}
    
    return HttpResponse(template.render(context,request))
   


def verinscripcion(request):
    ins = Inscritos.objects.all()
    data = {'Inscritos': list(ins.values('id','nombre','telefono','fechainscripcion','institucion','hora','estado','observacion'))}
    
    return JsonResponse(data)


class InscritosLista(APIView):
    def get(self, request):
        ins = Inscritos.objects.all()
        serial = InscritosSerializers(ins, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class InscripcionDetalle(APIView):
    def get_object(self, pk):
        try:
            return Inscritos.objects.get(pk=pk)
        except Inscritos.DoesNotExist:
            return Http404

    def get(self, request, pk):
        ins = self.get_object(pk)
        serial = InscritosSerializers(ins)
        return Response(serial.data)

    def put(self, request, pk):
        ins = self.get_object(pk)
        serial = InscritosSerializers(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(status=status.HTTP_204_NO_CONTENT)                                
    


def listar_Inscripciones(request):
    ins = Inscritos.objects.all()
    data = {'inscripcion': ins}
    return render(request, 'mostrar.html', data)

def agregar_inscripcion(request):
    form = FormInscritos()
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form ,'titulo':'AGREGAR INSCRIPCION'}
    return render(request, 'agregar.html', data)

def eliminar_inscripcion(request, id):
    ins = Inscritos.objects.get(id = id)
    ins.delete()
    return redirect( '/listar')

def actualizar_inscripcion(request, id):
    ins = Inscritos.objects.get(id = id)
    form = FormInscritos(instance=ins)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=ins)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form ,'titulo':'MODIFICAR INSCRIPCION'}
    return render(request, 'agregar.html', data)   


@api_view (['GET', 'POST'])
def InstitucionLista(request):
    if request.method == 'GET':
        estu = Institucion.objects.all()
        serial = InstitucionSerializers(estu, many=True)
        return Response(serial.data)
        
    if request.method == 'POST':
        serial = InstitucionSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def InstitucionDetalle(request, pk):
    try:
        estu = Institucion.objects.get(id=pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = InstitucionSerializers(estu)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = InstitucionSerializers(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def agregarinstituciones(request):
    form = FormInstitucion()
    if request.method == 'POST':
        form = FormInstitucion(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form ,'titulo':'AGREGAR INSTITUCION'}
    return render(request, 'institucion.html', data)

class AutorDetalleView(APIView):
    def get(self, request, *args, **kwargs):

        datos = {
            "rut": "21001667-8",
            "nombres": "Diego Alberto",
            "correo": "diegocalfuan@gmail.com",
            "apellidos": "Calfuan Calfuan",
            "edad": 21,
            "carrera": "Ing en Informatica",
        }


        # autor = Autor.objects.first()  
        serializer = AutorSerializer(datos)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
    
