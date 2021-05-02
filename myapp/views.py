from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Equipo, Ticket, Empleado
from .forms import EquipoForm, TicketForm, EmpleadoForm

# Create your views here.

class EquipoUpdateView(UpdateView) :
    form_class = EquipoForm
    template_name = 'updateEquipo.html'
    quearyset = Equipo 

class EquipoCreateView(CreateView) :
    form_class = EquipoForm
    template_name = 'createEquipo.html'
    quearyset = Equipo 

class EquipoListView(ListView):
    model = Equipo
    template_name = 'listaEquipo.html'
    context_object_name = 'lista_equipos'

class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'detalleEmpresa.html'
    context_object_name = 'empresa'
    
class EquipoDeleteView(DeleteView):
    form_class = EquipoForm
    template_name = 'deleteEquipo.html'
    quearyset = Equipo 




class TicketUpdateView(UpdateView) :
    form_class = TicketForm
    template_name = 'updateTicket.html'
    quearyset = Ticket 

class TicketCreateView(CreateView) :
    form_class = TicketForm
    template_name = 'createTicket.html'
    quearyset = Ticket

class TicketListView(ListView):
    model = Ticket
    template_name = 'listaTicket.html'
    context_object_name = 'lista_Tickets'

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'detalleTicket.html'
    context_object_name = 'Ticket'
    
class TicketDeleteView(DeleteView):
    form_class = TicketForm
    template_name = 'deleteTicket.html'
    quearyset = Ticket 



class EmpleadoUpdateView(UpdateView) :
    form_class = EmpleadoForm
    template_name = 'updateEmpleado.html'
    quearyset = Empleado

class EmpleadoCreateView(CreateView) :
    form_class = EmpleadoForm
    template_name = 'createEmpleado.html'
    quearyset = Empleado

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'listaEmpleado.html'
    context_object_name = 'lista_Empleados'

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'detalleEmpleado.html'
    context_object_name = 'Empleado'
    
class EmpleadoDeleteView(DeleteView):
    form_class = EmpleadoForm
    template_name = 'deleteEmpleado.html'
    quearyset = Empleado 