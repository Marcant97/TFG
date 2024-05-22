from django import forms
from .models import TuModelo

from django.utils import timezone
from datetime import datetime
class TuFormulario(forms.ModelForm):
    indicasiposeesalgncarnetdeconducir = forms.BooleanField(label='Indica si posees algún carnet de conducir', required=False)
    aceptoqueseenvenmisdatos = forms.BooleanField(label='Acepto que se envíen mis datos *', required=True)
    opciones_quactividadeshasrealizadoestasemana = [
        ('Estudiar', 'Estudiar'),
        ('Trabajar', 'Trabajar'),
        ('Hacer deporte', 'Hacer deporte'),
        ('Ver una película', 'Ver una película'),
    ]
    quactividadeshasrealizadoestasemana = forms.MultipleChoiceField(label='¿Qué actividades has realizado esta semana?', required=False, widget=forms.CheckboxSelectMultiple, choices=opciones_quactividadeshasrealizadoestasemana)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        min_date_introducetufechadenacimientoslomayoresdeedad = datetime.strptime('01/01/1900', '%d/%m/%Y').strftime('%Y-%m-%d')
        max_date_introducetufechadenacimientoslomayoresdeedad = datetime.strptime('21/05/2006', '%d/%m/%Y').strftime('%Y-%m-%d')
        self.fields['introducetufechadenacimientoslomayoresdeedad'].widget.attrs['min'] = min_date_introducetufechadenacimientoslomayoresdeedad
        self.fields['introducetufechadenacimientoslomayoresdeedad'].widget.attrs['max'] = max_date_introducetufechadenacimientoslomayoresdeedad
    class Meta:
        model = TuModelo
        fields = [
            'introducetunombre',
            'introducetusapellidos',
            'introducetuedad',
            'introducetunmerodehermanos',
            'introducetunotamedia',
            'seleccionatunivelmximodeestudios',
            'indicasiposeesalgncarnetdeconducir',
            'quactividadeshasrealizadoestasemana',
            'introduceunadireccindecorreoelectrnico',
            'introduceunadireccindecorreoelectrnicosloullesoulledues',
            'introduceundnivlido',
            'prefijo_introduceunnmerodetelfono',
            'introduceunnmerodetelfono',
            'introducetufechadenacimientoslomayoresdeedad',
            'introduceunnombredeusuario',
            'aceptoqueseenvenmisdatos',
        ]
        labels = {
            'introducetunombre': 'Introduce tu nombre',
            'introducetusapellidos': 'Introduce tus apellidos',
            'introducetuedad': 'Introduce tu edad',
            'introducetunmerodehermanos': 'Introduce tu número de hermanos',
            'introducetunotamedia': 'Introduce tu nota media',
            'seleccionatunivelmximodeestudios': 'Selecciona tu nivel máximo de estudios',
            'introduceunadireccindecorreoelectrnico': 'Introduce una dirección de correo electrónico',
            'introduceunadireccindecorreoelectrnicosloullesoulledues': 'Introduce una dirección de correo electrónico (sólo ull.es o ull.edu.es)',
            'introduceundnivlido': 'Introduce un DNI válido',
            'prefijo_introduceunnmerodetelfono': 'Prefijo telefónico',
            'introduceunnmerodetelfono': 'Introduce un número de teléfono',
            'introducetufechadenacimientoslomayoresdeedad': 'Introduce tu fecha de nacimiento (sólo mayores de edad)',
            'introduceunnombredeusuario': 'Introduce un nombre de usuario',
        }
        widgets = {
            'introducetufechadenacimientoslomayoresdeedad': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'
                })
        }
