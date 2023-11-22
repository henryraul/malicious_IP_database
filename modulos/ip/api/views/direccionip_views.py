from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from modulos.ip.api.serializers.direccionip_serializer import DireccionIPSerializer
from gestor_ip_maliciosas.base.authentication_mixins import Authentication


class DireccionIPBuscarAPIView(generics.RetrieveAPIView):
    serializer_class = DireccionIPSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def get(self,request, pk):
        serializer = self.get_queryset().filter(direccion_IP=pk).first()
        if serializer == None:
            return Response({'id':'-1','message': 'No existe una dirección IP con esos datos'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'id': serializer.id, 'direccion_IP': serializer.direccion_IP, 'pais': serializer.pais.id  }, status=status.HTTP_302_FOUND)
        
    

class DireccionIPListCreateAPIView(generics.ListCreateAPIView):
#class DireccionIPListCreateAPIView(Authentication,generics.ListCreateAPIView):
    serializer_class = DireccionIPSerializer
    #permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def post(self,request):
        try:
            #Recibimos el cuerpo de la petición HTTP
            serializer = self.serializer_class(data = request.data)
        
            #Tratamos de crear una nueva instancia, si el nombre ya está entonces no será válido pues no pueden existir dos direcciones IP
            #con el mismo nombre 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            #Si llegamos aquí es porque hay una dirección IP que ya está, por lo que lo buscamos en la base de datos y lo devolvemos en formato JSON
            direccionip = self.get_queryset().filter(direccion_IP=request.data['direccion_IP']).first()
        
            return Response({'id':direccionip.id,'direccion_IP': direccionip.direccion_IP, 'pais': direccionip.pais.pais}, status=status.HTTP_302_FOUND)
        except:
             #Si ocurre algun error es porque el cuerpo de la petición no tiene el formato adecuado o no se envió nada,
            # por tanto se genera un error y se devuelve -1 porque es un id que nunca existirá y el código de respuesta 400 además 
            return Response({'id':'-1', 'message': 'Petición incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
            
