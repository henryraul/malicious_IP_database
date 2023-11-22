from faker import Faker
from rest_framework import status
from gestor_ip_maliciosas.tests.test_setup import TestSetUp
from gestor_ip_maliciosas.settings import REPETICION_PRUEBAS

Faker.seed()
faker = Faker()

class ClasificacionIncidenteTestCase(TestSetUp):
    
    REPETICIONES = REPETICION_PRUEBAS
    
    url = '/incidente/clasificacionincidente/'
    
    def crear_ClasificacionIncidente_JSON(self):
        return {
            'clasificacion_incidente': faker.unique.pystr()
        }
    
    
    def test_clasificacion_incidente_listcreate(self):
        
        clasificacion_de_prueba = self.crear_ClasificacionIncidente_JSON()
            
        # Test para clasificaciones de incidentes que no existe en la base de datos
        respuesta_no_existente = self.client.post(
            self.url,
            clasificacion_de_prueba,
            format='json')
            
        # Debe adicionarla y devolver la misma clasificación en el cuerpo de la respuesta HTTP 
        # y dar un código HTTP 201 Create
            
        self.assertEqual(respuesta_no_existente.status_code,status.HTTP_201_CREATED)
        self.assertEqual(respuesta_no_existente.data["clasificacion_incidente"],clasificacion_de_prueba['clasificacion_incidente'])
                
        # Test para clasificaciones de incidentes que ya existen en la base de datos
            
        response_existente = self.client.post(
            self.url,
            clasificacion_de_prueba,
            format='json')
            
        # Debe devolver el ID y la misma clasificación en el cuerpo de la respuesta HTTP 
        # y dar un código HTTP 302 Found
            
        self.assertEqual(response_existente.status_code,status.HTTP_302_FOUND)
        self.assertEqual(response_existente.data["clasificacion_incidente"],clasificacion_de_prueba['clasificacion_incidente']) 
            
        # Código opcional para seguir la traza de la prueba
        print("Test clasificación:  Clasificación: {0}, No existe ({1}), Existe ({2})".format(clasificacion_de_prueba['clasificacion_incidente'],respuesta_no_existente.status_code,response_existente.status_code))