
from rest_framework import serializers
from modulos.incidente.models import Incidente


class IncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidente
        fields = '__all__'


    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre_corto': instance.nombre_corto,
            'descripcion': instance.descripcion,
            'fecha': instance.fecha,
            'tecnologia': instance.tecnologia.tecnologia,
            'clasificacion_incidente': instance.clasificacion_incidente.clasificacion_incidente,
            'entidad': instance.entidad.entidad
        }