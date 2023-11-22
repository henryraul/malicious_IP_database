from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from modulos.incidente.api.serializers.incidente_serializer import IncidenteSerializer


    
class IncidenteSerializerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = IncidenteSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        incidente = self.get_queryset().filter(nombre_corto=request.data['nombre_corto']).first()
        if incidente == None:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'Mensaje': 'Necesita completar todos los datos del incidente para poderla registrar correctamente'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'id':incidente.id, 
            'nombre_corto' : incidente.nombre_corto,
            'descripcion' : incidente.descripcion,
            'fecha' : incidente.fecha,
            'tecnologia' : incidente.tecnologia.tecnologia,
            'clasificacion_incidente' : incidente.clasificacion_incidente.clasificacion_incidente,
            'entidad' : incidente.entidad.entidad}, status=status.HTTP_400_BAD_REQUEST)
            
class IncidenteSerializerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = IncidenteSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def get(self,request, pk):
        serializer = self.get_queryset().filter(id=pk).first()
        if serializer == None:
            return Response({'id':'-1','message': 'No existe un incidente con estos datos'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'id': serializer.id, 
                             'nombre': serializer.nombre_corto, 
                             'descripcion' : serializer.descripcion,
                             'fecha' : serializer.fecha,             
                             'tecnologia' : serializer.tecnologia.tecnologia,
                             'clasificacion_incidente' : serializer.clasificacion_incidente.clasificacion_incidente,
                             'entidad' : serializer.entidad.entidad  }, status=status.HTTP_302_FOUND)
        
    