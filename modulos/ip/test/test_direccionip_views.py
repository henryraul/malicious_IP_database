from faker import Faker
from rest_framework import status
from gestor_ip_maliciosas.tests.test_setup import TestSetUp
from gestor_ip_maliciosas.settings import REPETICION_PRUEBAS
from apps.ip.models import Pais, DireccionIP
import urllib.parse

Faker.seed()
faker = Faker('es')
    
class DireccionIPTestCase(TestSetUp):
    
    url = '/ip/direccionip/'
    REPETICIONES = REPETICION_PRUEBAS
    
    def crear_direccionip_JSON(self):
        pais_auxiliar = Pais.objects.first()
        if pais_auxiliar == None:
            pais_auxiliar = Pais.objects.create(pais=faker.country())

        return {
            "direccion_IP": faker.unique.ipv4(),
            "pais": pais_auxiliar.id
        }
        
        
    def crear_direccionip_incorrecta_JSON(self):
        return {
            "direccion_IP": faker.unique.pystr(),
            "pais": ""
        }
    

    def test_direccionip_listcreate(self):
       
        for i in range(self.REPETICIONES):
            direccionip_de_prueba = self.crear_direccionip_JSON()                        
            
            # Test para direcciones IP que no existe en la base de datos, debe adicionarlos y devolver la misma dirección IP en el
            # cuerpo de la respuesta HTTP y dar un código HTTP 201 Create
            
            respuesta_no_existe = self.client.post(
                self.url+'listcreate/',
                direccionip_de_prueba,
                format='json'
            )

            self.assertEqual(respuesta_no_existe.status_code,status.HTTP_201_CREATED)
            self.assertEqual(respuesta_no_existe.data["direccion_IP"],direccionip_de_prueba['direccion_IP'])
            
            
            # Test para direcciones IP que  existe en la base de datos, debe devolver el ID y la la misma dirección IP en el
            # cuerpo de la respuesta HTTP y dar un código HTTP 302 Found
            
            response_existente = self.client.post(
                self.url+'listcreate/',
                direccionip_de_prueba,
                format='json'
            )
            
            self.assertEqual(response_existente.status_code,status.HTTP_302_FOUND)
            self.assertEqual(response_existente.data["direccion_IP"],direccionip_de_prueba['direccion_IP'])

            # Código opcional para seguir la traza de la prueba
            print("Test direccionip_listcreate:{0} IP: {1} No existe ({2}) Existe ({3})".format(i,direccionip_de_prueba['direccion_IP'],respuesta_no_existe.status_code,response_existente.status_code))



    def test_direccionip_incorrecta_listcreate(self):

       for i in range(self.REPETICIONES):
            direccionip_de_prueba_incorrecta = self.crear_direccionip_incorrecta_JSON()                        
            
            # Se envía una dirección IP que no está correctamente formada (solo caracteres aleatorios)
            # Debe devolver un código de respuesta HTTP 400 (Petición incorrecta)
            # Debe devolver un id igual a -1 que es incorrecto pues los id empiezan en 0, esto se configuró en direccionip_views:
            #          return Response({'id':'-1', 'message': 'Petición incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
            
            respuesta_no_existente = self.client.post(
                self.url+'listcreate/',
                direccionip_de_prueba_incorrecta,
                format='json'
            )

            self.assertEqual(respuesta_no_existente.status_code,status.HTTP_400_BAD_REQUEST)
            self.assertEqual(respuesta_no_existente.data["id"],'-1')
            
            # Código opcional para seguir la traza de la prueba
            print("Test incorrecta_listcreate:{0} IP: {1}  No existe ({2})".format(i,direccionip_de_prueba_incorrecta['direccion_IP'],respuesta_no_existente.status_code))

       
       
    def test_direccionip_retrieve(self):
        
        for i in range(self.REPETICIONES):
            
            continuar_creando_direccionip = True
            while(continuar_creando_direccionip):
                try:
                    # Obtenemos un país previamente registrado, si hay un error lo creo en la sección except
                    pais_auxiliar = Pais.objects.get(id=1)
                    
                    # Creamos una nueva dirección IP, si ya existe dará error y por eso repetiremos el ciclo while
                    direccionip_de_prueba = DireccionIP.objects.create(direccion_IP=faker.unique.ipv4(),pais=pais_auxiliar)
                    
                    #Si la dirección Ip se creó correctamente no es necesario volver a realizar el ciclo while
                    continuar_creando_direccionip = False
                except:
                    pais_auxiliar = Pais.objects.create(pais=faker.country())

            # Se envía una dirección IP que existe
            # debe devolver el ID de la dirección IP en el cuerpo de la respuesta HTTP y dar un código HTTP 302 Found    
 
            respuesta_existe = self.client.get(self.url+'retrieve/' + direccionip_de_prueba.direccion_IP)
            
            self.assertEqual(respuesta_existe.status_code,status.HTTP_302_FOUND)
            self.assertEqual(respuesta_existe.data["id"],direccionip_de_prueba.id)
            
            
            # Se envía una dirección IP mal formada
            # Debe devolver un código de respuesta HTTP 400 (Petición incorrecta)
            # Debe devolver un id igual a -1 que es incorrecto pues los id empiezan en 0, esto se configuró en direccionip_views:
            #          return Response({'id':'-1', 'message': 'Petición incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
            
            respuesta_no_existe = self.client.get(self.url+'retrieve/' + faker.unique.pystr())
            
            self.assertEqual(respuesta_no_existe.status_code,status.HTTP_404_NOT_FOUND)
            self.assertEqual(respuesta_no_existe.data["id"],'-1')
            
            # Código opcional para seguir la traza de la prueba
            print("Test direccionip_retrieve:{0}, IP: {1}, Existe ({2}), IP_DB ({3}), IP_Resp ({4}))".format(i,direccionip_de_prueba.direccion_IP,respuesta_existe.status_code,direccionip_de_prueba.id, respuesta_existe.data["id"]))