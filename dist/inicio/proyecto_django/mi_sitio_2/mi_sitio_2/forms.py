from django import forms
from .models import TuModelo

from django.utils import timezone
from datetime import datetime
class TuFormulario(forms.ModelForm):
    aceptolascondicionesdeusoylapolticadeprivacidad = forms.BooleanField(label='Acepto las condiciones de uso y la política de privacidad *', required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        min_date_introducetufechadenacimiento = datetime.strptime('01/01/1900', '%d/%m/%Y').strftime('%Y-%m-%d')
        max_date_introducetufechadenacimiento = datetime.strptime('31/12/2005', '%d/%m/%Y').strftime('%Y-%m-%d')
        self.fields['introducetufechadenacimiento'].widget.attrs['min'] = min_date_introducetufechadenacimiento
        self.fields['introducetufechadenacimiento'].widget.attrs['max'] = max_date_introducetufechadenacimiento
    class Meta:
        model = TuModelo
        fields = [
            'introducetunombreyapellidos',
            'introducetufechadenacimiento',
            'eligetugnero',
            'introducetudni',
            'introducetudireccindecorreoelectrnico',
            'prefijo_introducetunmerodetelfono',
            'introducetunmerodetelfono',
            'introducetudireccin',
            'introducetucdigopostal',
            'introduceunnombredeusuario',
            'aceptolascondicionesdeusoylapolticadeprivacidad',
        ]
        labels = {
            'introducetunombreyapellidos': 'Introduce tu nombre y apellidos',
            'introducetufechadenacimiento': 'Introduce tu fecha de nacimiento',
            'eligetugnero': 'Elige tu género',
            'introducetudni': 'Introduce tu DNI',
            'introducetudireccindecorreoelectrnico': 'Introduce tu dirección de correo electrónico',
            'prefijo_introducetunmerodetelfono': 'Prefijo telefónico',
            'introducetunmerodetelfono': 'Introduce tu número de teléfono',
            'introducetudireccin': 'Introduce tu dirección',
            'introducetucdigopostal': 'Introduce tu código postal',
            'introduceunnombredeusuario': 'Introduce un nombre de usuario',
        }
        widgets = {
            'introducetufechadenacimiento': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'
                })
        }
