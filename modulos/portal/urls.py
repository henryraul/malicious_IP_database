from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('estadisticas-generales/', views.graficas, name='graficas'),
    path('contacto/', views.contacto, name='contacto'),
    path('buscar/', views.buscar, name='buscar'),
]
