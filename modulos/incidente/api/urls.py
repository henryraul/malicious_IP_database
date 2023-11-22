from django.urls import path
from modulos.incidente.api.views.incidente_views import IncidenteSerializerListCreateAPIView, IncidenteSerializerRetrieveAPIView
from modulos.incidente.api.views.general_views import TecnologiaSerializerListCreateAPIView, ClasificacionIncidenteSerializerListCreateAPIView, EntidadSerializerListCreateAPIView



urlpatterns = [
    path('tecnologia/', TecnologiaSerializerListCreateAPIView.as_view(), name = 'tecnologia'),
    path('clasificacionincidente/', ClasificacionIncidenteSerializerListCreateAPIView.as_view(), name = 'clasificacionincidente'),
    path('entidad/', EntidadSerializerListCreateAPIView.as_view(), name = 'entidad'),
    path('incidente/listcreate/', IncidenteSerializerListCreateAPIView.as_view(), name = 'incidente_listcreate'),
    path('incidente/retrieve/<str:pk>', IncidenteSerializerRetrieveAPIView.as_view(), name = 'incidente_retrieve'),
]
