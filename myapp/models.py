from django.db import models

# Create your models here.
class Equipo(models.Model):
    numero_de_serie = models.IntegerField(default=0)
    modelo = models.CharField(max_length=50,default=' ')
    marca = models.CharField(max_length =50,default=' ')
    tipo_equipo = models.CharField(max_length =50,default=' ')
    fecha_adquisicion = models.DateField()
    fecha_puesta_en_marcha = models.DateField()
    proveedor_nombre = models.CharField(max_length =50,default=' ')
    proveedor_tlf = models.IntegerField(default=0)
    planta = models.CharField(max_length=50,default=' ')
    def __str__(self):
        return f'Proveedor:{self.proveedor_nombre} - {self.proveedor_tlf}, Nserie: {self.numero_de_serie}, Tipo:{self.tipo_equipo}'

class Empleado(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    telefono = models.IntegerField(default=0)
    dni = models.CharField(max_length=9)
    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellidos}, Correo: {self.email}, Telefono: {self.telefono}, DNI: {self.dni}'
        
class Ticket(models.Model):
   numero_referencia = models.IntegerField(default=0)
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




