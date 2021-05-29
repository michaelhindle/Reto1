from django import forms
from django.db.models import fields
from django.forms import DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Empleado, Equipo, Ticket

#La creacion del formulario de Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('__all__')
        widgets = {
            'email':forms.EmailInput(),
        }

#La creacion del formulario de Equipo
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['numero_de_serie', 
                    'modelo',
                    'marca',
                    'tipo_equipo',
                    'fecha_adquisicion',
                    'fecha_puesta_en_marcha',
                    'proveedor_nombre',
                    'proveedor_tlf',
                    'planta']
        widgets = {
            'fecha_adquisicion': forms.NumberInput(attrs={'type':'date'}),
            'fecha_puesta_en_marcha': forms.NumberInput(attrs={'type':'date'}),
        }

#La creacion del formulario de Ticket
class TicketForm(forms.ModelForm):
    URGENCIA = (
        ("Alta","Alta"),
        ("Media","Media"),
        ("Baja","Baja"),
    )
    TIPO = (
        ("Tipo1","Tipo1"),
        ("Tipo2","Tipo2"),
        ("Tipo3","Tipo3"),
    )
    ESTADO = (
        ("Estado1","Estado1"),
        ("Estado2","Estado2"),
        ("Estado3","Estado3"),
    )
    nivel_urgencia = forms.ChoiceField(choices = URGENCIA)
    tipo_ticket = forms.ChoiceField(choices = TIPO)
    estado_ticket = forms.ChoiceField(choices = ESTADO)
    class Meta:
        model = Ticket
        fields = ('__all__')
        widgets = {
            'fecha_apertura': forms.NumberInput(attrs={'type':'date'}),
            'fecha_resolucion': forms.NumberInput(attrs={'type':'date'}),
        }



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')
    
    class Meta:
        model= User
        fields = ['username', 'email', 'password1','password2']
        help_texts = {k:"" for k in fields }



class LoginForm(forms.Form):
    # Usuario
    usuario = forms.CharField(max_length=100)

    # Contraseña
    attrs = {
        "type": "password"  # Atributo para mostrarlo como contraseña
    }
    contrasena = forms.CharField(widget=forms.TextInput(attrs=attrs))