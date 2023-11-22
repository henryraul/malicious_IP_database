from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from modulos.peticion.api.serializers.peticion_serializer import PeticionSerializer



class PeticionSerializerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PeticionSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        peticion = self.get_queryset().filter(hash_peticion=request.data['hash_peticion']).first()
        print(peticion)
        if peticion == None:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'Mensaje': 'Necesita completar todos los datos de la petición para poderla registrar correctamente'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'id':peticion.id,
                             'hash_peticion' : peticion.hash_peticion,
                             'direccion_IP': peticion.direccion_IP.direccion_IP, 
                             'metodo_HTTP': peticion.metodo_HTTP.metodo_HTTP, 
                             'codigo_respuesta_HTTP': peticion.codigo_respuesta_HTTP.codigo_respuesta_HTTP, 
                             'agente_usuario': peticion.agente_usuario.agente_usuario, 
                             'referencia': peticion.referencia.referencia, 
                             'url': peticion.url.url
                             }, status=status.HTTP_400_BAD_REQUEST)