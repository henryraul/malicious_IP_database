from django.contrib import admin

from .models import *



class PaisVisualizacion(admin.ModelAdmin):
    list_display=['id', 'pais']
    list_display_links = ['pais']
    ordering = ['pais']


class DireccionIPVisualizacion(admin.ModelAdmin):
    list_display=['id',  'direccion_IP', 'pais']
    list_display_links = ['direccion_IP']
    ordering = ['direccion_IP']

    list_filter = ['pais']




admin.site.register(Pais,PaisVisualizacion)
admin.site.register(DireccionIP, DireccionIPVisualizacion)
