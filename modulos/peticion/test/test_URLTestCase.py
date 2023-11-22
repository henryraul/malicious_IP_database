from faker import Faker
from rest_framework import status
from gestor_ip_maliciosas.tests.test_setup import TestSetUp
from apps.peticion.models import URL

Faker.seed()
faker = Faker()

class URLTestCase(TestSetUp):
    
    REPETICIONES = 20
    
    url = '/peticion/url/'
    
    def crear_url_JSON(self):
        return {
            'url': faker.unique.uri()
        }
    
    def test_url_listcreate(self):
        for i in range(self.REPETICIONES):
        
            #Mandamos a crear una nueva url y la devolvermos en formato JSON
            url_prueba_JSON = self.crear_url_JSON()
            
            # Comprobamos primero si ya existe una url con similar nombre 
            # y devuelve None si no hay ninguna
            url_auxiliar = URL.objects.filter(url= url_prueba_JSON['url']).first()

            #Si la url no existe hacemos el Test de comprobación de creación
            if url_auxiliar == None:
                 
                # Test para url que no existe en la base de datos
                respuesta_url_no_existente = self.client.post(
                    self.url,
                    url_prueba_JSON,
                    format='json'
                )
            
                # Debe adicionarla y devolver la misma url en el cuerpo de la respuesta HTTP
                # y dar un código HTTP 201 Create  
 
                self.assertEqual(respuesta_url_no_existente.status_code,status.HTTP_201_CREATED)
                self.assertEqual(respuesta_url_no_existente.data["url"],url_prueba_JSON['url'])
            
            
            # Test para url que ya existen en la base de datos
            # En la petición anterior se creó el url o ya estaba en la base de datos
            respuesta_url_existente = self.client.post(
                self.url,
                url_prueba_JSON,
                format='json'
            )
            
            # Test para url que existen en la base de datos, debe devolver el ID y la misma 
            # url en el cuerpo de la respuesta HTTP y dar un código HTTP 302 Found
            self.assertEqual(respuesta_url_existente.status_code,status.HTTP_302_FOUND)
            self.assertEqual(respuesta_url_existente.data["url"],url_prueba_JSON['url']) 
            
            # Código opcional para seguir la traza de la prueba
            print("Test:{0}, url: {1}, Existe ({2})".format(i,url_prueba_JSON['url'],respuesta_url_existente.status_code))