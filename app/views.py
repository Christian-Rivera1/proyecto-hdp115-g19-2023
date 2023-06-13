from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from json import loads
from json import dumps
from app import models
from.models import Estadistica
from collections import defaultdict

# Create your views here.
@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        data = loads(request.body)
        id_est = data['id_est']
        nom_est = data['nombre_est']
        descrip = data['descrip']

        id_dato = data['id_dato']
        nombre_dato = data['nombre_dato']
        cantidad = data['cantidad']

        # code to save data to database goes here

        obj = Estadistica.objects.get(id_estadistica=id_est)
        if  nom_est:
            obj.nombre_estadistica = nom_est
        if  descrip:
            obj.descripcion = descrip
        obj.save()

        obj2 = models.DatosSerie.objects.get(id_dato = id_dato)
       
        if  nombre_dato:
            obj2.leyenda_dato = nombre_dato

        if  cantidad:
            obj2.cantidad_dato = cantidad

        obj2.save()

        # send response to client
        return JsonResponse({'success': 'true'})


def index(request):

    est = Estadistica.objects.filter(id_tipo_estadistica = 1).order_by('id_estadistica').values('nombre_estadistica','seriedatos__id_serie','seriedatos__id_tipo_serie', 'seriedatos__nombre_serie')
    c ={}
    var = 0
    for estadistica in est:
        dato= {}
        nom_estadistica = estadistica.get('nombre_estadistica')
        dato['nom_estadistica'] = nom_estadistica
        nombre_serie = estadistica.get('seriedatos__nombre_serie')
        dato['nombre_serie'] = nombre_serie
        if estadistica.get('seriedatos__id_tipo_serie') == 1 :
            matriz =[]
            datosest = models.DatosSerie.objects.filter(id_serie = estadistica.get('seriedatos__id_serie'))
            for datoserie in datosest:
                leyenda_dato = datoserie.leyenda_dato
                cantidad_dato = datoserie.cantidad_dato
                matriz.append([leyenda_dato,cantidad_dato])
            dato['datos_serie'] = matriz
            c['estadistica' + str(var)] = dato
            var = var + 1
        else:
            datosest = models.DatosSerie.objects.filter(id_serie = estadistica.get('seriedatos__id_serie')).values('cantidad_dato','leyenda_dato' ,'id_leyenda__leyenda_general')
            datosqwe = {}
            ListaL_C = [] #Contiene la lista de Leyendas Compuestas
            ListaL_S = []
            valoresMujeres = []
            valoresHombres = []
            for x in datosest:
                if  x.get('id_leyenda__leyenda_general') not in ListaL_C:
                    ListaL_C.append(x.get('id_leyenda__leyenda_general'))
                    
            for w in datosest:
                if w.get('leyenda_dato') not in ListaL_S:
                    ListaL_S.append(w.get('leyenda_dato'))
            
            for y in datosest:
                if y.get('leyenda_dato') == 'Hombres':
                    valoresHombres.append(y.get('cantidad_dato'))
                elif y.get('leyenda_dato') == 'Mujeres':
                    valoresMujeres.append(y.get('cantidad_dato'))
        
            datosqwe['leyendas_compuestas'] = ListaL_C
            datosqwe['leyendas_simples'] = ListaL_S
            datosqwe['valores_h'] = valoresHombres
            datosqwe['valores_m'] = valoresMujeres
                #mx.append([x.get('id_leyenda__leyenda_general'),x.get('leyenda_dato'), x.get('cantidad_dato')])
            dato['datos_serie'] = datosqwe
            c['estadistica' + str(var)] = dato
            var = var + 1
    #datos = dumps(c)
    contexto1 = {'est1': c}
    datos = dumps(c)
    contexto2 = {'est2': datos}

    return render(request, 'index.html', {'contex1':contexto1, 'contex2':contexto2})

def discapacidad(request):
    
    est = Estadistica.objects.filter(id_tipo_estadistica = 2).order_by('id_estadistica').values('nombre_estadistica','seriedatos__id_serie','seriedatos__id_tipo_serie', 'seriedatos__nombre_serie')    
    c ={}
    var = 0
    for estadistica in est:
        dato= {}
        nom_estadistica = estadistica.get('nombre_estadistica')
        dato['nom_estadistica'] = nom_estadistica
        nombre_serie = estadistica.get('seriedatos__nombre_serie')
        dato['nombre_serie'] = nombre_serie
        if estadistica.get('seriedatos__id_tipo_serie') == 1 :
            matriz =[]
            datosest = models.DatosSerie.objects.filter(id_serie = estadistica.get('seriedatos__id_serie'))
            for datoserie in datosest:
                leyenda_dato = datoserie.leyenda_dato
                cantidad_dato = datoserie.cantidad_dato
                matriz.append([leyenda_dato,cantidad_dato])
            dato['datos_serie'] = matriz
            c['estadistica' + str(var)] = dato
            var = var + 1
        else:
            datosest = models.DatosSerie.objects.filter(id_serie = estadistica.get('seriedatos__id_serie')).values('cantidad_dato','leyenda_dato' ,'id_leyenda__leyenda_general')
            datosqwe = {}
            ListaL_C = [] #Contiene la lista de Leyendas Compuestas
            ListaL_S = []
            valoresMujeres = []
            valoresHombres = []
            valoresTotales = []
            for x in datosest:
                if  x.get('id_leyenda__leyenda_general') not in ListaL_C:
                    ListaL_C.append(x.get('id_leyenda__leyenda_general'))
                    
            for w in datosest:
                if w.get('leyenda_dato') not in ListaL_S:
                    ListaL_S.append(w.get('leyenda_dato'))
            
            for y in datosest:
                if y.get('leyenda_dato') == 'Hombres':
                    valoresHombres.append(y.get('cantidad_dato'))
                elif y.get('leyenda_dato') == 'Mujeres':
                    valoresMujeres.append(y.get('cantidad_dato'))
                if y.get('leyenda_dato') == 'Total' :
                    valoresTotales.append(y.get('cantidad_dato'))
        

            datosqwe['leyendas_compuestas'] = ListaL_C
            datosqwe['leyendas_simples'] = ListaL_S
            datosqwe['valores_h'] = valoresHombres
            datosqwe['valores_m'] = valoresMujeres
            datosqwe['valores_t'] = valoresTotales
                #mx.append([x.get('id_leyenda__leyenda_general'),x.get('leyenda_dato'), x.get('cantidad_dato')])
            dato['datos_serie'] = datosqwe
            c['estadistica' + str(var)] = dato
            var = var + 1
    #datos = dumps(c)
    contexto1 = {'est1': c}
    datos = dumps(c)
    contexto2 = {'est2': datos}

    return render(request, 'personascondiscapacidad.html', {'contex1':contexto1, 'contex2':contexto2})


def empresas(request):
    est = Estadistica.objects.filter(id_tipo_estadistica = 3).order_by('id_estadistica').values('nombre_estadistica','seriedatos__id_serie','seriedatos__id_tipo_serie', 'seriedatos__nombre_serie')    
    c ={}
    var = 0
    for estadistica in est:
        dato= {}
        nom_estadistica = estadistica.get('nombre_estadistica')
        dato['nom_estadistica'] = nom_estadistica
        nombre_serie = estadistica.get('seriedatos__nombre_serie')
        dato['nombre_serie'] = nombre_serie
        if estadistica.get('seriedatos__id_tipo_serie') == 1 :
            categorias =[]
            arreglo=[]
            dic = {}
            datosest = models.DatosSerie.objects.filter(id_serie = estadistica.get('seriedatos__id_serie'))
            for datoserie in datosest:
                categorias.append(datoserie.leyenda_dato) 
                arreglo.append(datoserie.cantidad_dato)
                
            dic['categorias'] = categorias
            dic['datos'] = arreglo
            dato['datos_serie']= dic
            c['estadistica' + str(var)] = dato
            var = var + 1
        else:
            datosest = models.DatosSerie.objects.filter(id_serie = estadistica.get('seriedatos__id_serie')).values('cantidad_dato','leyenda_dato' ,'id_leyenda__leyenda_general')
            datosqwe = {}
            ListaL_C = [] #Contiene la lista de Leyendas Compuestas
            ListaL_S = []
            valoresMujeres = []
            valoresHombres = []
            valoresTotales = []
            for x in datosest:
                if  x.get('id_leyenda__leyenda_general') not in ListaL_C:
                    ListaL_C.append(x.get('id_leyenda__leyenda_general'))
                    
            for w in datosest:
                if w.get('leyenda_dato') not in ListaL_S:
                    ListaL_S.append(w.get('leyenda_dato'))
            
            for y in datosest:
                if y.get('leyenda_dato') == 'Hombres':
                    valoresHombres.append(y.get('cantidad_dato'))
                elif y.get('leyenda_dato') == 'Mujeres':
                    valoresMujeres.append(y.get('cantidad_dato'))
                if y.get('leyenda_dato') == 'Total' :
                    valoresTotales.append(y.get('cantidad_dato'))
        

            datosqwe['leyendas_compuestas'] = ListaL_C
            datosqwe['leyendas_simples'] = ListaL_S
            datosqwe['valores_h'] = valoresHombres
            datosqwe['valores_m'] = valoresMujeres
            datosqwe['valores_t'] = valoresTotales
                #mx.append([x.get('id_leyenda__leyenda_general'),x.get('leyenda_dato'), x.get('cantidad_dato')])
            dato['datos_serie'] = datosqwe
            c['estadistica' + str(var)] = dato
            var = var + 1
    #datos = dumps(c)
    contexto1 = {'est1': c}
    datos = dumps(c)
    contexto2 = {'est2': datos}

    return render(request, 'empresas.html', {'contex1':contexto1, 'contex2':contexto2})

def login(request):

    return render(request, 'registration/login.html')


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

    
@login_required
def editarestadisticas(request):
    est = Estadistica.objects.all().order_by('id_estadistica').values('id_estadistica', 'nombre_estadistica', 'descripcion', 'id_tipo_estadistica__nom_tipo_estadistica')
    # AL USAR EL METODO VALUES NO ES NECESARIO AGREGAR EL METODO .values {dumps(list(est.values())} DEL DICCIONARIO YA QUE EL METODO .VALUES DE LA CONSULTA TRAE UN DICCIONARIO
    datos = dumps(list(est))
    contexto = {'est': datos}
    return render(request, 'editarestadistica.html', contexto)

@login_required
def editando(request):
    if request.method == 'GET':
        id = request.GET.get('id')

        estadistica = Estadistica.objects.filter(id_estadistica = id).values('id_estadistica','nombre_estadistica','descripcion','seriedatos__id_serie')
        datos = models.DatosSerie.objects.filter(id_serie=estadistica[0]['seriedatos__id_serie']).order_by('id_dato')
        estadistica2 = list(estadistica.values())
        datos2 = list(datos.values())
        c ={}
        c['estadistica'] = estadistica2
        #print(datos2)
        """for e in estadistica :
            c['nombre_estadistica']=e.get('nombre_estadistica')
            c['id_estadistica']=e.get('id_estadistica')
            c['descripcion'] = e.get('descripcion') """
        c['datos'] = datos2

        datos = dumps(c)
        
    return render(request, 'editarpoblacion.html', {'datos': datos})

@login_required
def exit(request):
    logout(request)
    return redirect('app:index')

