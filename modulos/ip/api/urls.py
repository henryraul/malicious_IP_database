from django.urls import path
from modulos.ip.api.views.direccionip_views import DireccionIPListCreateAPIView, DireccionIPBuscarAPIView
from modulos.ip.api.views.pais_views import  PaisListCreateAPIView


urlpatterns = [

    path('direccionip/listcreate/', DireccionIPListCreateAPIView.as_view(), name = 'direccionip_listcreate'),
    path('direccionip/buscar/<str:pk>', DireccionIPBuscarAPIView.as_view(), name = 'direccionip_buscar'),
    
    path('pais/', PaisListCreateAPIView.as_view(), name = 'pais'),
]
