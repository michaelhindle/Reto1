from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Equipo, Ticket, Empleado
from .forms import EquipoForm, TicketForm, EmpleadoForm

# Create your views here.

class EquipoUpdateView(UpdateView) :
    form_class = EquipoForm
    template_name = 'createEquipo.html'
    model = Equipo 
    success_url = "http://127.0.0.1:8000/myapp/listaEquipo"

class EquipoCreateView(CreateView) :
    form_class = EquipoForm
    template_name = 'createEquipo.html'
    queryset = Equipo 
    success_url = "http://127.0.0.1:8000/myapp/listaEquipo"

class EquipoListView(ListView):
    model = Equipo
    template_name = 'listaEquipo.html'
    

class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'detailEquipo.html'
    queryset = Equipo.objects.all()
    
class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = 'deleteEquipo.html'
    success_url = "http://127.0.0.1:8000/myapp/listaEquipo"




class TicketUpdateView(UpdateView) :
    form_class = TicketForm
    template_name = 'createTicket.html'
    model = Ticket 
    success_url = "http://127.0.0.1:8000/myapp/listaTicket"

class TicketCreateView(CreateView) :
    form_class = TicketForm
    template_name = 'createTicket.html'
    queryset = Ticket
    success_url = "http://127.0.0.1:8000/myapp/listaTicket"

class TicketListView(ListView):
    model = Ticket
    template_name = 'listaTicket.html'
    

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'detailTicket.html'
    queryset = Ticket.objects.all()
    
class TicketDeleteView(DeleteView):
    form_class = TicketForm
    template_name = 'deleteTicket.html'
    model = Ticket 
    success_url = "http://127.0.0.1:8000/myapp/listaTicket"



class EmpleadoUpdateView(UpdateView) :
    form_class = EmpleadoForm
    template_name = 'createEmpleado.html'
    model = Empleado
    success_url = "http://127.0.0.1:8000/myapp/listaEmpleado"

class EmpleadoCreateView(CreateView) :
    form_class = EmpleadoForm
    template_name = 'createEmpleado.html'
    queryset = Empleado
    success_url = "http://127.0.0.1:8000/myapp/listaEmpleado"

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'listaEmpleado.html'
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'detailEmpleado.html'
    queryset = Empleado.objects.all()
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'deleteEmpleado.html'
    success_url = "http://127.0.0.1:8000/myapp/listaEmpleado"