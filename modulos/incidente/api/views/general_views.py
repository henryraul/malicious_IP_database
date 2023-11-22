from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from modulos.incidente.api.serializers.general_serializers import TecnologiaSerializer, ClasificacionIncidenteSerializer, EntidadSerializer


class TecnologiaSerializerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TecnologiaSerializer
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        try:
            tecnologia = self.get_queryset().filter(tecnologia=request.data['tecnologia']).first()
            return Response({'id': tecnologia.id,
                             'tecnologia': tecnologia.tecnologia
                             }, status=status.HTTP_302_FOUND)
        except:
            return Response({'id': '-1'
                             }, status=status.HTTP_400_BAD_REQUEST)
            


class ClasificacionIncidenteSerializerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ClasificacionIncidenteSerializer
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        try:
            clasificacion_incidente = self.get_queryset().filter(clasificacion_incidente=request.data['clasificacion_incidente']).first()
            return Response({'id': clasificacion_incidente.id,
                             'clasificacion_incidente': clasificacion_incidente.clasificacion_incidente
                             }, status=status.HTTP_302_FOUND)
        except:
            return Response({'id': '-1'
                             }, status=status.HTTP_400_BAD_REQUEST)



class EntidadSerializerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EntidadSerializer
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        try:
            entidad = self.get_queryset().filter(entidad=request.data['entidad']).first()
            return Response({'id': entidad.id,
                             'entidad': entidad.entidad
                             }, status=status.HTTP_302_FOUND)
        except:
            return Response({'id': '-1'
                             }, status=status.HTTP_400_BAD_REQUEST)
