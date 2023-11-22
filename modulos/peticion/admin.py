from django.contrib import admin
from .models import *

class MetodoHTTPVisualizacion(admin.ModelAdmin):
    list_display = ['id', 'metodo_HTTP']
    list_display_links = ['metodo_HTTP']
    ordering = ['metodo_HTTP']

class CodigoRespuestaHTTPVisualizacion(admin.ModelAdmin):
    list_display=['id', 'codigo_respuesta_HTTP']
    list_display_links = ['codigo_respuesta_HTTP']
    ordering = ['codigo_respuesta_HTTP']

class AgenteUsuarioVisualizacion(admin.ModelAdmin):
    list_display=['id', 'agente_usuario']
    list_display_links = ['agente_usuario']
    ordering = ['agente_usuario']

class ReferenciaVisualizacion(admin.ModelAdmin):
    list_display=['id', 'referencia']
    list_display_links = ['referencia']
    ordering = ['referencia']

class URLVisualizacion(admin.ModelAdmin):
    list_display=['id', 'url']
    list_display_links = ['url']
    ordering = ['url']

class PeticionVisualizacion(admin.ModelAdmin):
    list_display=['id', 
                  'fecha', 
                  'url', 
                  'direccion_IP', 
                  'hash_peticion', 
                  'metodo_HTTP', 
                  'codigo_respuesta_HTTP', 
                  'agente_usuario', 
                  'referencia', 
                  'incidente']
    
    list_display_links = ['url']
    ordering = ['fecha']

    list_filter = ['fecha', 
                  'url', 
                  'direccion_IP', 
                  'metodo_HTTP', 
                  'codigo_respuesta_HTTP', 
                  'agente_usuario', 
                  'referencia', 
                  'incidente']

admin.site.register(MetodoHTTP, MetodoHTTPVisualizacion)
admin.site.register(CodigoRespuestaHTTP, CodigoRespuestaHTTPVisualizacion)
admin.site.register(AgenteUsuario, AgenteUsuarioVisualizacion)
admin.site.register(Referencia, ReferenciaVisualizacion)
admin.site.register(URL, URLVisualizacion)
admin.site.register(Peticion, PeticionVisualizacion)