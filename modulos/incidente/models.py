from django.db import models


class Tecnologia(models.Model):

    tecnologia = models.CharField(
        'Descripcion', max_length=200, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Tecnología'
        verbose_name_plural = 'Tecnologías'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.tecnologia)


class ClasificacionIncidente(models.Model):

    clasificacion_incidente = models.CharField(
        'Descripción', max_length=200, blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Clasificación del incidente'
        verbose_name_plural = 'Clasificaciones de incidentes'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.clasificacion_incidente)


class Entidad(models.Model):

    entidad = models.CharField('Nombre', max_length=200,
                              blank=False, null=False, unique=True)

    class Meta:

        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.entidad)


class Incidente(models.Model):

    nombre_corto = models.CharField(
        'Nombre', max_length=150, blank=False, null=False)
    descripcion = models.CharField(
        'Descripcion', max_length=400, blank=False, null=False)
    fecha = models.DateTimeField(
        'Fecha del incidente')
    tecnologia = models.ForeignKey(
        Tecnologia, on_delete=models.CASCADE)
    clasificacion_incidente = models.ForeignKey(
        ClasificacionIncidente, on_delete=models.CASCADE)
    entidad = models.ForeignKey(
        Entidad, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Incidente'
        verbose_name_plural = 'Incidentes'

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.nombre_corto)
