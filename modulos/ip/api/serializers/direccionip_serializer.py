
from rest_framework import serializers

from modulos.ip.models import  DireccionIP

class DireccionIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = DireccionIP
        fields = ('id', 'direccion_IP','pais',)
        
        
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'direccion_IP': instance.direccion_IP,
            'pais': instance.pais.pais
        }