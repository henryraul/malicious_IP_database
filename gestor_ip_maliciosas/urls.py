
from django.contrib import admin
from django.urls import path, include
from gestor_ip_maliciosas.base.views import Login
from gestor_ip_maliciosas.base.views import my_logout
from gestor_ip_maliciosas.settings import NOMBRE_APP
from django.conf import settings



admin.site.site_header = NOMBRE_APP                   
admin.site.index_title = 'Administración'               
admin.site.site_title = NOMBRE_APP




urlpatterns = [
    path('', include('modulos.portal.urls')),
    path('admin/', admin.site.urls,  name='admin'),
    
    
  
    path('logout/', my_logout, name="logout"),


    
    path('ip/', include('modulos.ip.api.urls')),
    path('peticion/', include('modulos.peticion.api.urls')),
    path('incidente/', include('modulos.incidente.api.urls')),

    path('', Login.as_view(), name='Login'),


    
]
