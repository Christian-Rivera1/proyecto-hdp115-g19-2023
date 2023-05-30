from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import Context
from json import dumps
from app import models
from.models import Estadistica
# Create your views here.

def index(request):

    data= {'data1' : 
            
                [['Manzanas', 5],
                ['Naranjas', 3],
                ['Plátanos', 4]]
            ,
            'data2' :
            
                [['Manzanas', 3],
                ['Naranjas', 7],
                ['Plátanos', 2]]
            ,

            'data3' :
            
                [['Manzanas', 2],
                ['Naranjas', 2],
                ['Plátanos', 6]]
        }
    #estadisticas = models.Estadistica.objects.filter(id_tipo_estadistica = 1)
    datosjson = dumps(data)
    return render(request, 'index.html', { 'datos' : datosjson})

def discapacidad(request):

    
    estadisticas = models.Estadistica.objects.filter(id_tipo_estadistica = 1)
    datosjson = dumps(estadisticas)

    return render(request, 'personascondiscapacidad.html', {'datos' : datosjson})

def empresas(request):

    return render(request, 'empresas.html')

def login(request):

    return render(request, 'login.html')
