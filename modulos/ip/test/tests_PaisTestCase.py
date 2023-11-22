from faker import Faker
from rest_framework import status
from gestor_ip_maliciosas.tests.test_setup import TestSetUp
from gestor_ip_maliciosas.settings import REPETICION_PRUEBAS
from apps.ip.models import Pais

Faker.seed()
faker = Faker('es')

    
class PaisTestCase(TestSetUp):
    
    REPETICIONES = 150
    
    url = '/ip/pais/'
    
    def crear_pais_JSON(self):
        return {
            'pais': faker.country()
        }
    

    def test_pais_listcreate(self):
        for i in range(self.REPETICIONES):
            
            #Mandamos a crear un nuevo nombre de país y devolverlo en formato JSON
            pais_prueba_JSON = self.crear_pais_JSON()
            
            # Comprobamos primero si ya existe un país con similar nombre
            pais_auxiliar = Pais.objects.filter(pais= pais_prueba_JSON['pais']).first()

            #Si el país no existe hacemos la comprobación de creación
            if pais_auxiliar == None:
                 
                # Test para paises que no existe en la base de datos
                respuesta_pais_no_existente = self.client.post(
                    self.url,
                    pais_prueba_JSON,
                    format='json'
                )
            
                # Debe adicionarlos y devolver el mismo Pais en el cuerpo de la respuesta HTTP
                # cuerpo de la respuesta HTTP y dar un código HTTP 201 Create  
 
                self.assertEqual(respuesta_pais_no_existente.status_code,status.HTTP_201_CREATED)
                self.assertEqual(respuesta_pais_no_existente.data["pais"],pais_prueba_JSON['pais'])
            
            
            # Test para paises que ya existe en la base de datos
            # En la petición anterior se creó el país o ya estaba en la base de datos
            respuesta_pais_existente = self.client.post(
                self.url,
                pais_prueba_JSON,
                format='json'
            )
            
            # Test para paises que  existe en la base de datos, debe devolver el ID y el mismo país en el
            # cuerpo de la respuesta HTTP y dar un código HTTP 302 Found
            self.assertEqual(respuesta_pais_existente.status_code,status.HTTP_302_FOUND)
            self.assertEqual(respuesta_pais_existente.data["pais"],pais_prueba_JSON['pais']) 
            
            print("Test:{0}, País: {1}, Existe ({2})".format(i,pais_prueba_JSON['pais'],respuesta_pais_existente.status_code))
