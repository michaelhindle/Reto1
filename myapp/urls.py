"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import (EquipoListView, TicketListView, EmpleadoListView, 
EquipoUpdateView, TicketUpdateView, EmpleadoUpdateView, 
EquipoCreateView, TicketCreateView, EmpleadoCreateView, 
EquipoDeleteView, TicketDeleteView, EmpleadoDeleteView,
EquipoDetailView, TicketDetailView, EmpleadoDetailView)

urlpatterns = [
    # Path de inicio
    path('', views.EquipoListView, name='ListaEquipos'),
    # Listas
    path('listaEquipo/', EquipoListView.as_view(), name='ListaEquipos'),
    path('listaTicket/', TicketListView.as_view(), name='ListaTickets'),
    path('listaEmpleado/', EmpleadoListView.as_view(), name='ListaEmpleados'),
    # Update
    path('updateEquipo/<int:pk>/', EquipoUpdateView.as_view(), name='UpdateEquipos'),
    path('updateTicket/<int:pk>/', TicketUpdateView.as_view(), name='UpdateTickets'),
    path('updateEmpleado/<int:pk>/', EmpleadoUpdateView.as_view(), name='UpdateEmpleado'),
    # Create
    path('createEquipo/', EquipoCreateView.as_view(), name='CreateEquipo'),
    path('createTicket/', TicketCreateView.as_view(), name='CreateTicket'),
    path('createEmpleado/', EmpleadoCreateView.as_view(), name='CreateEmpleado'),
    # Delete
    path('deleteEquipo/<int:pk>/', EquipoDeleteView.as_view(), name='DeleteEquipo'),
    path('deleteTicket/<int:pk>/', TicketDeleteView.as_view(), name='DeleteTicket'),
    path('deleteEmpleado/<int:pk>/', EmpleadoDeleteView.as_view(), name='DeleteEmpleado'),
    # Detail
    path('detailEquipo/<int:pk>/', EquipoDetailView.as_view(), name='DetailEquipo'),
    path('detailTicket/<int:pk>/', TicketDetailView.as_view(), name='DetailTicket'),
    path('detailEmpleado/<int:pk>/', EmpleadoDetailView.as_view(), name='DetailEmpleado'),
]
