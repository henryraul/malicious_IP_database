from modulos.incidente.models import Tecnologia, ClasificacionIncidente, Entidad
from rest_framework import serializers


class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = '__all__'



class ClasificacionIncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasificacionIncidente
        fields = '__all__'



class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = '__all__'

        
