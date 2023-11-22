from faker import Faker
from rest_framework import status
from datetime import date
from gestor_ip_maliciosas.tests.test_setup import TestSetUp
from gestor_ip_maliciosas.settings import REPETICION_PRUEBAS
from apps.incidente.models import Tecnologia, ClasificacionIncidente, Entidad, Incidente

Faker.seed()
faker = Faker('es')
    
class IncidenteTestCase(TestSetUp):
    
    url = '/incidente/incidente/'
    REPETICIONES = REPETICION_PRUEBAS
    
    def crear_incidente_JSON(self):
        tecnologia = Tecnologia.objects.create(tecnologia=faker.unique.pystr())
        clasificacion_incidente = ClasificacionIncidente.objects.create(clasificacion_incidente=faker.unique.pystr())
        entidad = Entidad.objects.create(entidad=faker.unique.pystr())

        return {
            'nombre_corto': 'Incidente: ' + faker.unique.word(),
            'descripcion': faker.texts(nb_texts=5),
            'fecha' : date.today(),
            'tecnologia' : tecnologia.id,
            'clasificacion_incidente' : clasificacion_incidente.id,
            'entidad' : entidad.id
        }
    

    def test_incidente_listcreate(self):
       
        for i in range(self.REPETICIONES):
            incidente_de_prueba_JSON = self.crear_incidente_JSON()                        
            
            # Test para incidentes que no existen en la base de datos, debe adicionarlos y devolver el misma incidente en el
            # cuerpo de la respuesta HTTP y dar un código HTTP 201 Create
            
            respuesta_incidente_no_existe = self.client.post(
                self.url+'listcreate/',
                incidente_de_prueba_JSON,
                format='json'
            )

            self.assertEqual(respuesta_incidente_no_existe.status_code,status.HTTP_201_CREATED)
            self.assertEqual(respuesta_incidente_no_existe.data["nombre_corto"],incidente_de_prueba_JSON['nombre_corto'])
            
            
            # Test para incidentes que  existen en la base de datos, debe devolver el ID y el mismo incidente en el
            # cuerpo de la respuesta HTTP y dar un código HTTP 302 Found
            
            response_incidente_existente = self.client.post(
                self.url+'listcreate/',
                incidente_de_prueba_JSON,
                format='json'
            )
            
            self.assertEqual(response_incidente_existente.status_code,status.HTTP_302_FOUND)
            self.assertEqual(response_incidente_existente.data["nombre_corto"],incidente_de_prueba_JSON['nombre_corto'])

            # Código opcional para seguir la traza de la prueba
            print("Test incidente_listcreate:{0} IP: {1} No existe ({2}) Existe ({3})".format(i,incidente_de_prueba_JSON['nombre_corto'],respuesta_incidente_no_existe.status_code,response_incidente_existente.status_code))



    def test_incidente_incorrect0_listcreate(self):

       for i in range(self.REPETICIONES):
            incidente_de_prueba_incorrecta = '{cualquier cosa para generar error}'                       
            
            # Se envía una incidente que no está correctamente formada (solo caracteres aleatorios)
            # Debe devolver un código de respuesta HTTP 400 (Petición incorrecta)
            # Debe devolver un id igual a -1 que es incorrecto pues los id empiezan en 0, esto se configuró en incidente_views:
            #          return Response({'id':'-1', 'message': 'Petición incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
            
            respuesta_incorrecta = self.client.post(
                self.url+'listcreate/',
                incidente_de_prueba_incorrecta,
                format='json'
            )

            self.assertEqual(respuesta_incorrecta.status_code,status.HTTP_400_BAD_REQUEST)
            self.assertEqual(respuesta_incorrecta.data["id"],'-1')
            
            # Código opcional para seguir la traza de la prueba
            print("Test incorrecta_listcreate:{0} IP: {1}  No existe ({2})".format(i,incidente_de_prueba_incorrecta['id'],respuesta_incorrecta.status_code))

       
       
    def test_incidente_retrieve(self):
        
        incidente_de_prueba_JSON = self.crear_incidente_JSON()
        
        incidente_de_prueba = Incidente.objects.create(
            nombre_corto =incidente_de_prueba_JSON['nombre_corto'],
            descripcion = incidente_de_prueba_JSON['descripcion'],
            fecha = incidente_de_prueba_JSON['fecha'],
            tecnologia = incidente_de_prueba_JSON['tecnologia'],
            clasificacion_incidente = incidente_de_prueba_JSON['clasificacion_incidente'],
            entidad = incidente_de_prueba_JSON['entidad']
            )
        

        # Se envía una incidente que existe
        # debe devolver el ID de la incidente en el cuerpo de la respuesta HTTP y dar un código HTTP 302 Found    
 
        respuesta_incidente_existe = self.client.get(self.url+'retrieve/' + incidente_de_prueba.id)
            
        self.assertEqual(respuesta_incidente_existe.status_code,status.HTTP_302_FOUND)
        self.assertEqual(respuesta_incidente_existe.data["id"],incidente_de_prueba.id)
            
            
        # Se envía una incidente mal formada
        # Debe devolver un código de respuesta HTTP 400 (Petición incorrecta)
        # Debe devolver un id igual a -1 que es incorrecto pues los id empiezan en 0, esto se configuró en incidente_views:
        #          return Response({'id':'-1', 'message': 'Petición incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
            
        respuesta_incidente_no_existe = self.client.get(self.url+'retrieve/' + faker.unique.pystr())
            
        self.assertEqual(respuesta_incidente_no_existe.status_code,status.HTTP_404_NOT_FOUND)
        self.assertEqual(respuesta_incidente_no_existe.data["id"],'-1')
            
        # Código opcional para seguir la traza de la prueba
        print("Test incidente_retrieve:{0}, Incidente: {1}, Existe ({2}), IP_DB ({3}), IP_Resp ({4}))".format(i,incidente_de_prueba.nombre_corto,respuesta_incidente_existe.status_code,incidente_de_prueba.id, respuesta_incidente_existe.data["id"]))