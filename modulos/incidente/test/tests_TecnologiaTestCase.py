from faker import Faker
from rest_framework import status
from gestor_ip_maliciosas.tests.test_setup import TestSetUp
from gestor_ip_maliciosas.settings import REPETICION_PRUEBAS

Faker.seed()
faker = Faker()

class TecnologiaTestCase(TestSetUp):
    
    REPETICION = REPETICION_PRUEBAS

    url = '/incidente/tecnologia/'

    def crear_Tecnologia_JSON(self):
        return {
            'tecnologia': faker.unique.pystr()
        }


    def test_tecnologia_listcreate(self):
        
        for i in range(self.REPETICION):
            tecnologia_prueba = self.crear_Tecnologia_JSON()

            ### Test para tecnología que no existe en la base de datos
            response_no_existente = self.client.post(
                self.url,
                tecnologia_prueba,
                format='json'
            )

            # Debe adicionarla y devolver la misma tecnología en el cuerpo de la respuesta HTTP 
            # y dar un código HTTP 201 Create
            
            self.assertEqual(response_no_existente.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response_no_existente.data["tecnologia"], tecnologia_prueba['tecnologia'])
            

            ### Test para tecnología que ya existe en la base de datos
            response_existente = self.client.post(
                self.url,
                tecnologia_prueba,
                format='json'
            )
            
            # Debe devolver el ID y la misma tecnologia en el cuerpo de la respuesta HTTP 
            # y dar un código HTTP 302 Found
           
            self.assertEqual(response_existente.status_code,status.HTTP_302_FOUND)
            self.assertEqual(response_existente.data["tecnologia"], tecnologia_prueba['tecnologia'])
            
            # Código opcional para seguir la traza de la prueba
            print("Test:{0}, Tecnologia: {1}, No existe ({2}), Existe ({3})".format(i, tecnologia_prueba['tecnologia'], response_no_existente.status_code, response_existente.status_code))