from faker import Faker
from rest_framework import status
from gestor_ip_maliciosas.tests.test_setup import TestSetUp
from apps.peticion.models import MetodoHTTP

Faker.seed()
faker = Faker()

class CodigoRespuestaHTTPTestCase(TestSetUp):
    
    REPETICIONES = 9
    
    url = '/peticion/codigorespuestahttp/'
    
    def crear_codigor_respuesta_http_JSON(self):
        return {
            'codigo_respuesta_HTTP': faker.unique.http_method()
        }
    
    def test_crear_metodo_HTTP_JSON_listcreate(self):
        for i in range(self.REPETICIONES):
        
            #Mandamos a crear un nuevo nombre de método HTTP y devolverlo en formato JSON
            metodo_http_prueba_JSON = self.crear_codigorespuestahttp_JSON()
            
            # Comprobamos primero si ya existe un método HTTP con similar nombre 
            # y devuelve None si no hay ninguno
            metodo_http_auxiliar = MetodoHTTP.objects.filter(metodo_HTTP= metodo_http_prueba_JSON['metodo_HTTP']).first()

            #Si el método HTTP no existe hacemos el Test de comprobación de creación
            if metodo_http_auxiliar == None:
                 
                # Test para métodos HTTP que no existe en la base de datos
                respuesta_metodo_http_no_existente = self.client.post(
                    self.url,
                    metodo_http_prueba_JSON,
                    format='json'
                )
            
                # Debe adicionarlos y devolver el mismo método HTTP en el cuerpo de la respuesta HTTP
                # y dar un código HTTP 201 Create  
 
                self.assertEqual(respuesta_metodo_http_no_existente.status_code,status.HTTP_201_CREATED)
                self.assertEqual(respuesta_metodo_http_no_existente.data["metodo_HTTP"],metodo_http_prueba_JSON['metodo_HTTP'])
            
            
            # Test para métodos HTTP que ya existen en la base de datos
            # En la petición anterior se creó el método HTTP o ya estaba en la base de datos
            respuesta_metodo_http_existente = self.client.post(
                self.url,
                metodo_http_prueba_JSON,
                format='json'
            )
            
            # Test para métodos HTTP que existen en la base de datos, debe devolver el ID y el mismo método HTTP en el
            # cuerpo de la respuesta HTTP y dar un código HTTP 302 Found
            self.assertEqual(respuesta_metodo_http_existente.status_code,status.HTTP_302_FOUND)
            self.assertEqual(respuesta_metodo_http_existente.data["metodo_HTTP"],metodo_http_prueba_JSON['metodo_HTTP']) 
            
            print("Test:{0}, Método HTTP: {1}, Existe ({2})".format(i,metodo_http_prueba_JSON['metodo_HTTP'],respuesta_metodo_http_existente.status_code))