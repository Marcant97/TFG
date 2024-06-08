from django import forms
from .models import TuModelo

from django.utils import timezone
from datetime import datetime
class TuFormulario(forms.ModelForm):
    aceptolascondicionesdeusoylapolticadeprivacidad = forms.BooleanField(label='Acepto las condiciones de uso y la política de privacidad *', required=True)
    class Meta:
        model = TuModelo
        fields = [
            'introducetunombre',
            'introducetudireccindecorreoelectrnico',
            'asunto',
            'mensaje',
            'aceptolascondicionesdeusoylapolticadeprivacidad',
        ]
        labels = {
            'introducetunombre': 'Introduce tu nombre',
            'introducetudireccindecorreoelectrnico': 'Introduce tu dirección de correo electrónico',
            'asunto': 'Asunto',
            'mensaje': 'Mensaje',
        }
