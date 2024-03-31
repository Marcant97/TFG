from django import forms
from .models import TuModelo

from django.utils import timezone
from datetime import datetime
class TuFormulario(forms.ModelForm):
    aceptoelreglamentodelaprueba = forms.BooleanField(label='Acepto el reglamento de la prueba', required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        min_date_introducetufechadenacimiento = datetime.strptime('01/01/1910', '%d/%m/%Y').strftime('%Y-%m-%d')
        max_date_introducetufechadenacimiento = datetime.strptime('31/12/2010', '%d/%m/%Y').strftime('%Y-%m-%d')
        self.fields['introducetufechadenacimiento'].widget.attrs['min'] = min_date_introducetufechadenacimiento
        self.fields['introducetufechadenacimiento'].widget.attrs['max'] = max_date_introducetufechadenacimiento
    class Meta:
        model = TuModelo
        fields = [
            'introducetunombreyapellidos',
            'introducetufechadenacimiento',
            'introducetuedad',
            'introducetualu',
            'prefijo_introducetunmerodetelfono',
            'introducetunmerodetelfono',
            'introducetudireccindecorreoelectrnico',
            'introducetudni',
            'seleccionatutalladecamiseta',
            'aceptoelreglamentodelaprueba',
        ]
        labels = {
            'introducetunombreyapellidos': 'Introduce tu nombre y apellidos:',
            'introducetufechadenacimiento': 'Introduce tu fecha de nacimiento:',
            'introducetuedad': 'Introduce tu edad',
            'introducetualu': 'Introduce tu alu',
            'prefijo_introducetunmerodetelfono': 'Prefijo telefónico',
            'introducetunmerodetelfono': 'Introduce tu número de teléfono:',
            'introducetudireccindecorreoelectrnico': 'Introduce tu dirección de correo electrónico:',
            'introducetudni': 'Introduce tu DNI:',
            'seleccionatutalladecamiseta': 'Selecciona tu talla de camiseta:',
            'aceptoelreglamentodelaprueba': 'Acepto el reglamento de la prueba',
        }
        widgets = {
            'introducetufechadenacimiento': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'
                })
        }
