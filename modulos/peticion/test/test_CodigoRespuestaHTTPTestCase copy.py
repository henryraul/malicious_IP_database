from faker import Faker
from rest_framework import status
from gestor_ip_maliciosas.tests.test_setup import TestSetUp
from apps.peticion.models import CodigoRespuestaHTTP

Faker.seed()
faker = Faker()

class CodigoRespuestaHTTPTestCase(TestSetUp):
    
    REPETICIONES = 20
    
    url = '/peticion/codigorespuestahttp/'
    
    def crear_codigo_respuesta_http_JSON(self):
        return {
            'codigo_respuesta_HTTP': str(faker.random_int(min=100,max=599))
        }
    
    def test_Codigo_Respuesta_HTTP_listcreate(self):
        for i in range(self.REPETICIONES):
        
            #Mandamos a crear un nuevo código de respuesta HTTP y lo devolvermos en formato JSON
            codigo_respuesta_http_prueba_JSON = self.crear_codigo_respuesta_http_JSON()
            
            # Comprobamos primero si ya existe un código de respuesta HTTP con similar nombre 
            # y devuelve None si no hay ninguno
            codigo_respuesta_http_auxiliar = CodigoRespuestaHTTP.objects.filter(codigo_respuesta_HTTP= codigo_respuesta_http_prueba_JSON['codigo_respuesta_HTTP']).first()

            #Si el código de respuesta HTTP no existe hacemos el Test de comprobación de creación
            if codigo_respuesta_http_auxiliar == None:
                 
                # Test para código de respuesta HTTP que no existe en la base de datos
                respuesta_codigo_respuesta_http_no_existente = self.client.post(
                    self.url,
                    codigo_respuesta_http_prueba_JSON,
                    format='json'
                )
            
                # Debe adicionarlos y devolver el mismo código de respuesta HTTP en el cuerpo de la respuesta HTTP
                # y dar un código HTTP 201 Create  
 
                self.assertEqual(respuesta_codigo_respuesta_http_no_existente.status_code,status.HTTP_201_CREATED)
                self.assertEqual(respuesta_codigo_respuesta_http_no_existente.data["codigo_respuesta_HTTP"],codigo_respuesta_http_prueba_JSON['codigo_respuesta_HTTP'])
            
            
            # Test para código de respuesta HTTP que ya existen en la base de datos
            # En la petición anterior se creó el código de respuesta HTTP o ya estaba en la base de datos
            respuesta_codigo_respuesta_http_existente = self.client.post(
                self.url,
                codigo_respuesta_http_prueba_JSON,
                format='json'
            )
            
            # Test para código de respuesta HTTP que existen en la base de datos, debe devolver el ID y el mismo 
            # código de respuesta HTTP en el cuerpo de la respuesta HTTP y dar un código HTTP 302 Found
            self.assertEqual(respuesta_codigo_respuesta_http_existente.status_code,status.HTTP_302_FOUND)
            self.assertEqual(respuesta_codigo_respuesta_http_existente.data["codigo_respuesta_HTTP"],codigo_respuesta_http_prueba_JSON['codigo_respuesta_HTTP']) 
            
            # Código opcional para seguir la traza de la prueba
            print("Test:{0}, Código resp.: {1}, Existe ({2})".format(i,codigo_respuesta_http_prueba_JSON['codigo_respuesta_HTTP'],respuesta_codigo_respuesta_http_existente.status_code))