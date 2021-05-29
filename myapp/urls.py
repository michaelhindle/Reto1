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
from django.contrib.auth.views import LoginView, LogoutView
from .views import (EquipoListView, TicketListView, EmpleadoListView, 
EquipoUpdateView, TicketUpdateView, EmpleadoUpdateView, 
EquipoCreateView, TicketCreateView, EmpleadoCreateView, 
EquipoDeleteView, TicketDeleteView, EmpleadoDeleteView,
EquipoDetailView, TicketDetailView, EmpleadoDetailView)

app_name = 'reto'

urlpatterns = [
    # Path de inicio
    path('', views.EquipoListView, name='ListaEquipo'),
    # Listas
    path('listaEquipo/', EquipoListView.as_view(), name='ListaEquipos'),
    path('listaTicket/', TicketListView.as_view(), name='ListaTicket'),
    path('listaEmpleado/', EmpleadoListView.as_view(), name='ListaEmpleado'),
    # Update
    path('updateEquipo/<int:pk>/', EquipoUpdateView.as_view(), name='UpdateEquipo'),
    path('updateTicket/<int:pk>/', TicketUpdateView.as_view(), name='UpdateTicket'),
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
    # Login
    path('register/', views.register, name= 'register'), 
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
