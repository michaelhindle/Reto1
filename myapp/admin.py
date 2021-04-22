from django.contrib import admin
from .models import Red, Equipo, Empresa, Trabajador

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Trabajador)
admin.site.register(Red)
admin.site.register(Equipo)
