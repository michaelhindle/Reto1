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
from .views import buscarEquipo
from django.contrib.auth.decorators import login_required

app_name = 'reto'

urlpatterns = [
    # Path de inicio
    path('',LoginView.as_view(template_name='login.html'), name='login'),
    # Listas
    path('myapp/listaEquipo/', login_required(EquipoListView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/'), name='ListaEquipos'),
    path('myapp/listaTicket/', login_required(TicketListView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/'), name='ListaTicket'),
    path('myapp/listaEmpleado/', login_required(EmpleadoListView.as_view(),login_url='http://127.0.0.1:8000/myapp/login/'), name='ListaEmpleado'),
    # Update
    path('myapp/updateEquipo/<int:pk>/', login_required(EquipoUpdateView.as_view(),login_url='http://127.0.0.1:8000/myapp/login/') ,name='UpdateEquipo'),
    path('myapp/updateTicket/<int:pk>/', login_required(TicketUpdateView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/') ,name='UpdateTicket'),
    path('myapp/updateEmpleado/<int:pk>/', login_required(EmpleadoUpdateView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/') ,name='UpdateEmpleado'),
    # Create
    path('myapp/createEquipo/', login_required(EquipoCreateView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/') ,name='CreateEquipo'),
    path('myapp/createTicket/', login_required(TicketCreateView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/') , name='CreateTicket'),
    path('myapp/createEmpleado/', login_required(EmpleadoCreateView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/') , name='CreateEmpleado'),
    # Delete
    path('myapp/deleteEquipo/<int:pk>/', login_required( EquipoDeleteView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/') , name='DeleteEquipo'),
    path('myapp/deleteTicket/<int:pk>/', login_required( TicketDeleteView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/') ,name='DeleteTicket'),
    path('myapp/deleteEmpleado/<int:pk>/', login_required( EmpleadoDeleteView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/') , name='DeleteEmpleado'),
    # Detail
    path('myapp/detailEquipo/<int:pk>/', login_required( EquipoDetailView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/') , name='DetailEquipo'),
    path('myapp/detailTicket/<int:pk>/', login_required( TicketDetailView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/') , name='DetailTicket'),
    path('myapp/detailEmpleado/<int:pk>/', login_required( EmpleadoDetailView.as_view(), login_url='http://127.0.0.1:8000/myapp/login/') , name='DetailEmpleado'),
    # Login
    path('myapp/register/', views.register, name= 'register'), 
    path('myapp/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('myapp/logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # Buscador
    path('myapp/buscarEquipo/',login_required( views.buscarEquipo,login_url='http://127.0.0.1:8000/myapp/login/'), name='BuscarEquipo'),

]
