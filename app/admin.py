from django.contrib import admin
from app import models
# Register your models here.

admin.site.register(models.TipoEstadistica)
admin.site.register(models.Estadistica)
admin.site.register(models.TipoSerie)
admin.site.register(models.SerieDatos)
admin.site.register(models.LeyendaCompuesta)
admin.site.register(models.DatosSerie)