from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import Empresa 

# Create your views here.

class EmpresaListView(ListView):
    model = Empresa
    #queryset = Empleado.objects.all()
    template_name = 'index.html'
    context_object_name = 'lista_empresas'

class EmpresaDetailView(DetailView):
    model = Empresa
    #queryset = Empleado.objects.all()
    template_name = 'detalleEmpresa.html'
    context_object_name = 'empresa'
    '''
    def get_context_data(self, **kwargs):
        # Cargar el contexto base
        context = super().get_context_data(**kwargs)
        #context['lista_trabajadores']=
'''
def index(request):
    empresas = get_list_or_404(Empresa)
    context={
        'lista_empresas': empresas
    }
    return render(request, "index.html", context)
'''    
def buscarEmpresa(request,nombre_empresa):
    empresas = get_list_or_404(Empresa, nombre = nombre_empresa)
    output = ', '.join([str(e.id) for e in empresas])
    return HttpResponse(output)
    
def detalleEmpresa(request, id_empresa):
    empresa = get_object_or_404(Empresa, pk = id_empresa)
    trabajadores = empresa.trabajador_set.all()
    context = {
        'empresa':empresa,
        'lista_trabajadores':trabajadores
    }
    return render(request, "detalleEmpresa.html", context)

def detalleTrabajador(request, id_trabajador):
    trabajador = get_object_or_404(Trabajador, pk = id_trabajador)
    context = {
        'trabajador':trabajador
    }
    return render(request, "detalleTrabajador.html", context)