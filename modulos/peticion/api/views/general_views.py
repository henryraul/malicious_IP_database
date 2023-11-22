from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from modulos.peticion.api.serializers.general_serializers import MetodoHTTPSerializer, CodigoRespuestaHTTPSerializer, AgenteUsuarioSerializer, ReferenciaSerializer, URLSerializer


class MetodoHTTPSerializerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MetodoHTTPSerializer
    #permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        try:
            metodo_HTTP = self.get_queryset().filter(metodo_HTTP=request.data['metodo_HTTP']).first()
            return Response({'id':metodo_HTTP.id,'metodo_HTTP':metodo_HTTP.metodo_HTTP}, status=status.HTTP_302_FOUND)
        except:
            return Response({'id': '-1'}, status=status.HTTP_400_BAD_REQUEST)
    
    
class CodigoRespuestaHTTPListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CodigoRespuestaHTTPSerializer
    #permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        try:
            codigorespuestahttp = self.get_queryset().filter(codigo_respuesta_HTTP=request.data['codigo_respuesta_HTTP']).first()
            return Response({'id':codigorespuestahttp.id, 'codigo_respuesta_HTTP': codigorespuestahttp.codigo_respuesta_HTTP}, status=status.HTTP_302_FOUND)
        except:
            return Response({'id': '-1'}, status=status.HTTP_400_BAD_REQUEST)



class AgenteUsuarioSerializerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AgenteUsuarioSerializer
    #permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        try:
            agente_usuario = self.get_queryset().filter(agente_usuario=request.data['agente_usuario']).first()
            return Response({'id':agente_usuario.id, 'agente_usuario':agente_usuario.agente_usuario}, status=status.HTTP_302_FOUND)
        except:
            return Response({'id': '-1'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    
class ReferenciaSerializerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReferenciaSerializer
    #permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        try:
            referencia = self.get_queryset().filter(referencia=request.data['referencia']).first()
            return Response({'id':referencia.id,'referencia':referencia.referencia}, status=status.HTTP_302_FOUND)
        except:
            return Response({'id': '-1'}, status=status.HTTP_400_BAD_REQUEST)
        
        

class URLSerializerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = URLSerializer
    #permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        try:
            url = self.get_queryset().filter(url=request.data['url']).first()
            return Response({'id':url.id,'url':url.url}, status=status.HTTP_302_FOUND)
        except:
            return Response({'id': '-1'}, status=status.HTTP_400_BAD_REQUEST)
            