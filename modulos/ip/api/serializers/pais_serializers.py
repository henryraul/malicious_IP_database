from modulos.ip.models import Pais
from rest_framework import serializers


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'pais',)


    def to_representation(self, instance):
        return {
            'id': instance.id,
            'pais': instance.pais
        }
