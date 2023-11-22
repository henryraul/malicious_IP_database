from rest_framework import serializers
from modulos.peticion.models import *



class PeticionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Peticion
        fields = '__all__'
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'hash_peticion': instance.hash_peticion,
            'direccion_IP' :instance.direccion_IP.direccion_IP,
            'metodo_HTTP': instance.metodo_HTTP.metodo_HTTP,
            'codigo_respuesta_HTTP': instance.codigo_respuesta_HTTP.codigo_respuesta_HTTP,
            'agente_usuario': instance.agente_usuario.agente_usuario,
            'referencia': instance.referencia.referencia,
            'url': instance.url.url,
        }