from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    cif = models.CharField(max_length=12)
    
    def __str__(self):
        return self.nombre
class Trabajador(models.Model):
    # Campo para la relación
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    # Es posible indicar un valor por defecto mediante 'default'
    antiguedad = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre
class Red(models.Model):
    ip = models.CharField(max_length=15)
    nombre = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField('Fecha de creacion')

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    red = models.ForeignKey(Red, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30, default='')
    # Es posible indicar un valor por defecto mediante 'default'
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.tipo


