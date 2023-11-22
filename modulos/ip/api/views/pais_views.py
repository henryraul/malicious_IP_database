from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from modulos.ip.api.serializers.pais_serializers import PaisSerializer
#from rest_framework.permissions import Authenticated
from gestor_ip_maliciosas.base.authentication_mixins import Authentication

#class PaisListCreateAPIView(Authentication, generics.ListCreateAPIView):
class PaisListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PaisSerializer
    #permission_classes = (IsAuthenticated,)

    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


    def post(self, request):
        try:
            #Recibimos el cuerpo de la petición HTTP
            serializer = self.serializer_class(data=request.data)

            #Tratamos de crear una nueva instancia, si el nombre ya está entonces no será válido pues no pueden existir dos paises
            #con el mismo nombre 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            #Si llegamos aquí es porque hay un país que ya está, por lo que lo buscamos en la base de datos y lo devolvemos en formato JSON
            pais = self.get_queryset().filter(pais=request.data['pais']).first()
            return Response({'id': pais.id,
                             'pais': pais.pais}, 
                             status=status.HTTP_302_FOUND)
        except:
            #Si ocurre algun error es porque el cuerpo de la petición no tiene el formato adecuado o no se envió nada,
            # por tanto se genera un error y se devuelve -1 porque es un id que nunca existirá y el código de respuesta 400 además 
            return Response({'id':'-1', 'message': 'Petición incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
        
    