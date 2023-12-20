from django.db import models


# Create your models here.

ESTADO = (
    ('', 'SELECCIONA UNA OPCION'),
    ('reservada', 'RESRVADA'),
    ('completada', 'COMPLETADA'),
    ('anulada', 'ANULADA'),
    ('no asiste', 'NO ASISTE'),
)

class Institucion(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Intituciones'
    def __str__(self):
        return self.nombre    


class Inscritos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length = 12)
    fechainscripcion = models.DateField()
    institucion = models.ForeignKey(Institucion,on_delete=models.CASCADE)
    hora = models.TimeField(auto_now=False)
    estado = models.CharField(max_length=20, choices=ESTADO)
    observacion = models.TextField(max_length=150, blank=True)


class Autor(models.Model):
    rut = models.CharField(max_length=10)
    nombres = models.CharField(max_length=100)
    correo = models.EmailField()
    carrera = models.CharField(max_length=100)
    edad = models.IntegerField()
    apellidos = models.CharField(max_length=100)

