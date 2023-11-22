from faker import Faker
from rest_framework import status
from gestor_ip_maliciosas.tests.test_setup import TestSetUp
from apps.peticion.models import Referencia

Faker.seed()
faker = Faker()

class ReferenciaTestCase(TestSetUp):
    
    REPETICIONES = 20
    
    url = '/peticion/referencia/'
    
    def crear_referencia_JSON(self):
        return {
            'referencia': faker.url()
        }
    
    def test_referencia_listcreate(self):
        for i in range(self.REPETICIONES):
        
            #Mandamos a crear una nueva referencia y la devolvermos en formato JSON
            referencia_prueba_JSON = self.crear_referencia_JSON()
            
            # Comprobamos primero si ya existe una referencia con similar nombre 
            # y devuelve None si no hay ninguna
            referencia_auxiliar = Referencia.objects.filter(referencia= referencia_prueba_JSON['referencia']).first()

            #Si la referencia no existe hacemos el Test de comprobación de creación
            if referencia_auxiliar == None:
                 
                # Test para referencia que no existe en la base de datos
                respuesta_referencia_no_existente = self.client.post(
                    self.url,
                    referencia_prueba_JSON,
                    format='json'
                )
            
                # Debe adicionarla y devolver la misma referencia en el cuerpo de la respuesta HTTP
                # y dar un código HTTP 201 Create  
 
                self.assertEqual(respuesta_referencia_no_existente.status_code,status.HTTP_201_CREATED)
                self.assertEqual(respuesta_referencia_no_existente.data["referencia"],referencia_prueba_JSON['referencia'])
            
            
            # Test para referencia que ya existen en la base de datos
            # En la petición anterior se creó el referencia o ya estaba en la base de datos
            respuesta_referencia_existente = self.client.post(
                self.url,
                referencia_prueba_JSON,
                format='json'
            )
            
            # Test para referencia que existen en la base de datos, debe devolver el ID y el mismo 
            # referencia en el cuerpo de la respuesta HTTP y dar un código HTTP 302 Found
            self.assertEqual(respuesta_referencia_existente.status_code,status.HTTP_302_FOUND)
            self.assertEqual(respuesta_referencia_existente.data["referencia"],referencia_prueba_JSON['referencia']) 
            
            # Código opcional para seguir la traza de la prueba
            print("Test:{0}, Referencia: {1}, Existe ({2})".format(i,referencia_prueba_JSON['referencia'],respuesta_referencia_existente.status_code))