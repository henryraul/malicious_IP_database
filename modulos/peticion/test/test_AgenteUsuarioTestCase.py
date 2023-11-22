from faker import Faker
from rest_framework import status
from gestor_ip_maliciosas.tests.test_setup import TestSetUp
from apps.peticion.models import AgenteUsuario

Faker.seed()
faker = Faker()

class AgenteUsuarioTestCase(TestSetUp):
    
    REPETICIONES = 20
    
    url = '/peticion/agenteusuario/'
    
    def crear_agente_usuario_JSON(self):
        return {
            'agente_usuario': faker.user_agent()
        }
    
    def test_agente_usuario_listcreate(self):
        for i in range(self.REPETICIONES):
        
            #Mandamos a crear un nuevo agente de usuario y lo devolvermos en formato JSON
            agente_usuario_prueba_JSON = self.crear_agente_usuario_JSON()
            
            # Comprobamos primero si ya existe un agente de usuario con similar nombre 
            # y devuelve None si no hay ninguno
            agente_usuario_auxiliar = AgenteUsuario.objects.filter(agente_usuario= agente_usuario_prueba_JSON['agente_usuario']).first()

            #Si el agente de usuario no existe hacemos el Test de comprobación de creación
            if agente_usuario_auxiliar == None:
                 
                # Test para agente de usuario que no existe en la base de datos
                respuesta_agente_usuario_no_existente = self.client.post(
                    self.url,
                    agente_usuario_prueba_JSON,
                    format='json'
                )
            
                # Debe adicionarlos y devolver el mismo agente de usuario en el cuerpo de la respuesta HTTP
                # y dar un código HTTP 201 Create  
 
                self.assertEqual(respuesta_agente_usuario_no_existente.status_code,status.HTTP_201_CREATED)
                self.assertEqual(respuesta_agente_usuario_no_existente.data["agente_usuario"],agente_usuario_prueba_JSON['agente_usuario'])
            
            
            # Test para agente de usuario que ya existen en la base de datos
            # En la petición anterior se creó el agente de usuario o ya estaba en la base de datos
            respuesta_agente_usuario_existente = self.client.post(
                self.url,
                agente_usuario_prueba_JSON,
                format='json'
            )
            
            # Test para agente de usuario que existen en la base de datos, debe devolver el ID y el mismo 
            # agente de usuario en el cuerpo de la respuesta HTTP y dar un código HTTP 302 Found
            self.assertEqual(respuesta_agente_usuario_existente.status_code,status.HTTP_302_FOUND)
            self.assertEqual(respuesta_agente_usuario_existente.data["agente_usuario"],agente_usuario_prueba_JSON['agente_usuario']) 
            
            # Código opcional para seguir la traza de la prueba
            print("Test:{0}, Agente usuario: {1}, Existe ({2})".format(i,agente_usuario_prueba_JSON['agente_usuario'],respuesta_agente_usuario_existente.status_code))