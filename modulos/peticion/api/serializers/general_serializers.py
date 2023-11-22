from modulos.peticion.models import MetodoHTTP, CodigoRespuestaHTTP, AgenteUsuario, Referencia, URL
from rest_framework import serializers


class MetodoHTTPSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetodoHTTP
        fields = '__all__'


class CodigoRespuestaHTTPSerializer(serializers.ModelSerializer):

    class Meta:
        model = CodigoRespuestaHTTP
        fields = '__all__'


class AgenteUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgenteUsuario
        fields = '__all__'


class ReferenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Referencia
        fields = '__all__'


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'
