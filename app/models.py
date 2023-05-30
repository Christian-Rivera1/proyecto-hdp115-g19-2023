from django.db import models

# Create your models here.

class TipoEstadistica(models.Model):
    id_tipo_estadistica = models.AutoField(primary_key= True, unique=True)
    nom_tipo_estadistica = models.CharField(max_length=25, null= False)

    def __str__(self):
        return self.nom_tipo_estadistica

    #class Meta:
        #db_table = 'tipo_estadistica'



class Estadistica(models.Model):
    id_estadistica = models.AutoField(primary_key=True, unique=True)
    id_tipo_estadistica = models.ForeignKey(TipoEstadistica, on_delete = models.CASCADE, null=False, blank= False)
    nombre_estadistica = models.CharField(max_length= 100, null= False)
    descripcion = models.CharField(max_length=500, null=False, blank= False)

    def __str__(self):
        return self.nombre_estadistica
    #class Meta:
    #    db_table = 'estadistica'

class TipoSerie(models.Model):
    id_tipo_serie = models.AutoField(primary_key=True, unique=True)
    nombre_tipo_serie = models.CharField(max_length=50, null= False, blank= False)


    def __str__(self):
        return self.nombre_tipo_serie
   # class Meta:
    #    db_table = 'tipo_serie'

class SerieDatos(models.Model):
    id_serie = models.AutoField(primary_key=True, unique=True)
    id_tipo_serie = models.ForeignKey(TipoSerie, on_delete = models.CASCADE, null=False, blank= False)
    id_estadistica = models.ForeignKey(Estadistica, on_delete = models.CASCADE, null=False, blank= False)
    nombre_serie = models.CharField(max_length=100, null=False, blank= False)

    def __str__(self):
        return self.nombre_serie
    #class Meta:
     #   db_table = 'serie_datos'

class LeyendaCompuesta(models.Model):
    id_leyenda = models.AutoField(primary_key=True, unique=True)
    leyenda_general= models.CharField(max_length=100, null=False, blank= False)

    def __str__(self):
        return self.leyenda_general
    #class Meta:
     #   db_table = 'leyenda_compuesta'

class DatosSerie(models.Model):
    id_dato = models.AutoField(primary_key=True, unique=True)
    id_leyenda = models.ForeignKey(LeyendaCompuesta, on_delete = models.CASCADE, null=True, blank= True)
    id_serie = models.ForeignKey(SerieDatos, on_delete = models.CASCADE, null=False, blank= False)
    cantidad_dato = models.IntegerField(null=False, blank= False)
    leyenda_dato = models.CharField(max_length=50, null=False, blank=False)

    #class Meta:
     #   db_table = 'datos_serie'









