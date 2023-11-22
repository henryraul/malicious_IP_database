from faker import Faker
from rest_framework import status
from gestor_ip_maliciosas.tests.test_setup import TestSetUp
from gestor_ip_maliciosas.settings import REPETICION_PRUEBAS

Faker.seed()
faker = Faker()


class EntidadTestCase(TestSetUp):
    
    REPETICIONES = 1

    url = '/incidente/entidad/'

    def crear_entidad_JSON(self):
        return {
            'entidad': faker.unique.company()
        }

    def test_entidad_listcreate(self):
        
        for i in range(self.REPETICIONES):
            
            entidad_prueba = self.crear_entidad_JSON()

            # Test para entidades que no existe en la base de datos
            response_no_existente = self.client.post(
                self.url,
                entidad_prueba,
                format='json'
            )

            #Debe adicionarla y devolver el mismo nombre de entidad en el cuerpo de la respuesta HTTP 
            # y dar un código HTTP 201 Create
           
            self.assertEqual(response_no_existente.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response_no_existente.data["entidad"], entidad_prueba['entidad'])
            

            # Test para clasificaciones de incidentes que ya existen en la base de datos
            response_existente = self.client.post(
                self.url,
                entidad_prueba,
                format='json'
            )
            
            # Debe devolver el ID y la misma entidad en el cuerpo de la respuesta HTTP 
            # y dar un código HTTP 302 Found

            self.assertEqual(response_existente.status_code,status.HTTP_302_FOUND)
            self.assertEqual(response_existente.data["entidad"], entidad_prueba['entidad'])
            
            # Código opcional para seguir la traza de la prueba
            print("Test entidad: Entidad: {0}, No existe ({1}), Existe ({2})".format(entidad_prueba['entidad'], response_no_existente.status_code, response_existente.status_code))