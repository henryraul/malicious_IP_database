from django.db import models

from modulos.ip.models import DireccionIP
from modulos.incidente.models import Incidente


class MetodoHTTP(models.Model):

    metodo_HTTP = models.CharField(
        'Descripción', max_length=100, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Método HTTP'
        verbose_name_plural = 'Métodos HTTP'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.metodo_HTTP)


class CodigoRespuestaHTTP(models.Model):

    codigo_respuesta_HTTP = models.CharField(
        'Descripción', max_length=50, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Código de Respuesta HTTP'
        verbose_name_plural = 'Códigos de Respuesta HTTP'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.codigo_respuesta_HTTP)


class AgenteUsuario(models.Model):

    agente_usuario = models.CharField(
        'Descripción', max_length=1000, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Agente de Usuario'
        verbose_name_plural = 'Agentes de usuario'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.agente_usuario)


class Referencia(models.Model):

    referencia = models.CharField('Descripción', max_length=1000, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Referencia'
        verbose_name_plural = 'Referencias'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.referencia)


class URL(models.Model):

    url = models.CharField('Descripción', max_length=500, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'URL'
        verbose_name_plural = 'URL'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.url)



class Peticion(models.Model):
    fecha = models.DateTimeField('Fecha de la peticion HTTP')
    direccion_IP = models.ForeignKey(DireccionIP, on_delete=models.CASCADE)
    hash_peticion = models.CharField('hash_peticion', max_length=64, blank=False, null=False, unique=True, default='64')

    metodo_HTTP = models.ForeignKey( MetodoHTTP, on_delete=models.CASCADE)
    codigo_respuesta_HTTP = models.ForeignKey( CodigoRespuestaHTTP, on_delete=models.CASCADE)
    agente_usuario = models.ForeignKey(AgenteUsuario, on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    incidente = models.ForeignKey(Incidente, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Petición'
        verbose_name_plural = 'Peticiones'

    def __str__(self):
        cadena = "({0})  [{1}]  {2} - {3} - {4} - {5} - {6} "
        return cadena.format(self.fecha, self.direccion_IP, self.metodo_HTTP, self.url, self.codigo_respuesta_HTTP, self.agente_usuario, self.referencia)
