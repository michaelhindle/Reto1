from django.db import models

# Create your models here.
class Equipo(models.Model):
    numerodeserie = models.IntegerField 
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length =50)
    tipoequipo = models.CharField(max_length =50)
    fecha_adquisicion = models.DateField()
    fecha_puestaenmarcha = models.DateField()
    proveedor_nombre = models.CharField(max_length =50)
    proveedor_tlf = models.IntegerField
    planta = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    telefono = models.IntegerField
    dni = models.CharField(max_length=9)
    def __str__(self):
        return self.nombre
        
class Ticket(models.Model):
   numeroreferencia = models.IntegerField
   titulo = models.CharField(max_length =50)
   descripcion = models.TextField(max_length =1000)
   fecha_apertura = models.DateField()
   fecha_resolucion = models.DateField()
   nivel_urgencia = models.CharField(max_length = 50)
   tipo_ticket = models.CharField(max_length=50)
   estado_ticket = models.CharField(max_length=50)
   comentario = models.TextField(max_length =1000)
   FK_Equipo_ID = models.ForeignKey(Equipo, on_delete=models.CASCADE)
   FK_Empleado_ID = models.ForeignKey(Empleado, on_delete=models.CASCADE)




