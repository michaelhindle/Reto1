from django.contrib import admin
from .models import Equipo, Ticket, Empleado

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Empleado)
admin.site.register(Equipo)
