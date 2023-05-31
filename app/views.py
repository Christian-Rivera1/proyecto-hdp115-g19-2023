from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import Context
from json import dumps
from app import models
from.models import Estadistica
from collections import defaultdict
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

    
    #estadisticas = models.Estadistica.objects.filter(id_tipo_estadistica = 1)
    #json = dumps(list(estadisticas.values()))

    #est = models.Estadistica.objects.all().values('nombre_estadistica', 'descripcion', 'seriedatos__nombre_serie')

    #est = models.SerieDatos.objects.all().values('nombre_serie', 'id_estadistica__nombre_estadistica', 'id_estadistica__descripcion')
    #est = Estadistica.objects.all().values('serie__id_serie')
    #Funiona 
    #est = Estadistica.objects.all().values('nombre_estadistica', 'seriedatos__nombre_serie', 'seriedatos__datosserie__leyenda_dato','seriedatos__datosserie__cantidad_dato')
    est = Estadistica.objects.all().values('nombre_estadistica','seriedatos__id_serie', 'seriedatos__nombre_serie')
    #est = Estadistica.objects.filter(id_tipo_estadistica = 1).values('id_estadistica', 'nombre_estadistica', 'descripcion')
    c ={}
    var = 0
    for estadistica in est:
        dato= {}
        nom_estadistica = estadistica.get('nombre_estadistica')
        dato['nom_estadistica'] = nom_estadistica
        #for seriedatos in estadistica.get('seriedatos'):
        nombre_serie = estadistica.get('seriedatos__nombre_serie')
        dato['nombre_serie'] = nombre_serie
        matriz =[]
        datosest = models.DatosSerie.objects.filter(id_serie = estadistica.get('seriedatos__id_serie'))
        for datoserie in datosest:
            leyenda_dato = datoserie.leyenda_dato
            cantidad_dato = datoserie.cantidad_dato
            matriz.append([leyenda_dato,cantidad_dato])
        dato['datos_serie'] = matriz
        c['estadistica' + str(var)] = dato
        var = var + 1

        
    """datos = Estadistica.objects.all().values('nombre_estadistica', 'seriedatos__nombre_serie')
    
    # Crear un diccionario para almacenar los datos agrupados
    datos_agrupados = defaultdict(list)
    
    # Iterar sobre los datos y agruparlos por nombre_estadistica
    for dato in datos:
        nombre_estadistica = dato['nombre_estadistica']
        nombre_serie = dato['seriedatos__nombre_serie']
        datos_agrupados[nombre_estadistica].append(nombre_serie)
    
    # Convertir el diccionario en una lista de diccionarios para pasarlo al template
    datos_agrupados = [{'nombre_estadistica': k, 'series': v} for k, v in datos_agrupados.items()]
    
    contexto = {'datos': datos_agrupados} """
    #queryset_dict = list(est.values())
    #queryset_json = dumps(queryset_dict)

    #datosjson = dumps(estadisticas)
    datos = dumps(c)
    contexto = {'est': datos}

    #return render(request, 'personascondiscapacidad.html', {'queryset_json' : queryset_json})
    return render(request, 'personascondiscapacidad.html', contexto)

def empresas(request):

    return render(request, 'empresas.html')

def login(request):

    return render(request, 'login.html')


def tabla(request):

    est = Estadistica.objects.all().values('id_estadistica','nombre_estadistica')
    c ={}
    var = 0
    for estadistica in est:
        dato= {}
        id_estadistica = estadistica.get('id_estadistica')
        nom_estadistica = estadistica.get('nombre_estadistica')
        dato['id_estadistica'] = id_estadistica
        dato['nom_estadistica'] = nom_estadistica
        #for seriedatos in estadistica.get('seriedatos'):
        """nombre_serie = estadistica.get('seriedatos__nombre_serie')
        dato['nombre_serie'] = nombre_serie
        matriz =[]
        datosest = models.DatosSerie.objects.filter(id_serie = estadistica.get('seriedatos__id_serie'))
        for datoserie in datosest:
            leyenda_dato = datoserie.leyenda_dato
            cantidad_dato = datoserie.cantidad_dato
            matriz.append([leyenda_dato,cantidad_dato])
        dato['datos_serie'] = matriz """
        c['estadistica' + str(var)] = dato
        var = var + 1

    datos = dumps(c)
    contexto = {'est': datos}

    return render(request, 'pruebatabla.html', contexto)