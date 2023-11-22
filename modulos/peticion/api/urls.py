from django.urls import path
from modulos.peticion.api.views.peticion_views import PeticionSerializerListCreateAPIView
from modulos.peticion.api.views.general_views import  MetodoHTTPSerializerListCreateAPIView, CodigoRespuestaHTTPListCreateAPIView, AgenteUsuarioSerializerListCreateAPIView, ReferenciaSerializerListCreateAPIView, URLSerializerListCreateAPIView

urlpatterns = [
    path('metodoHTTP/', MetodoHTTPSerializerListCreateAPIView.as_view(), name='metodoHTTP'),
    path('codigorespuestahttp/', CodigoRespuestaHTTPListCreateAPIView.as_view(), name='codigorespuestahttp'),
    path('agenteusuario/', AgenteUsuarioSerializerListCreateAPIView.as_view(), name='agenteusuario'),
    path('referencia/', ReferenciaSerializerListCreateAPIView.as_view(), name='referencia'),
    path('url/', URLSerializerListCreateAPIView.as_view(), name='url'),


    path('peticion/', PeticionSerializerListCreateAPIView.as_view(), name='Peticion'),
]
