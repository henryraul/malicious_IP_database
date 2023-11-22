from django.contrib import admin
from .models import *

class ClasificacionIncidenteBuscador(admin.ModelAdmin):
    list_display=[ 'id', 'clasificacion_incidente']
    list_display_links = ['clasificacion_incidente']
    ordering = ['clasificacion_incidente']



class EntidadBuscador(admin.ModelAdmin):
    list_display=['id', 'entidad']
    list_display_links = ['entidad']
    ordering = ['entidad']



class TecnologiaVisualizacion(admin.ModelAdmin):
    list_display=['id', 'tecnologia']
    list_display_links = ['tecnologia']
    ordering = ['tecnologia']




class IncidenteBuscador(admin.ModelAdmin):
    list_display=['id', 'nombre_corto', 
                  'descripcion', 
                  'fecha', 
                  'tecnologia', 
                  'clasificacion_incidente', 
                  'entidad']
    
    list_filter = ['tecnologia', 
                   'clasificacion_incidente', 
                   'entidad']

    list_display_links = ['nombre_corto']
    ordering = ['fecha']


admin.site.register(Tecnologia, TecnologiaVisualizacion)
admin.site.register(ClasificacionIncidente, ClasificacionIncidenteBuscador)
admin.site.register(Entidad, EntidadBuscador)
admin.site.register(Incidente, IncidenteBuscador)