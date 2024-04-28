from django import forms
from .models import TuModelo

from django.utils import timezone
from datetime import datetime
class TuFormulario(forms.ModelForm):
    aceptoelreglamentodelaprueba = forms.BooleanField(label='Acepto el reglamento de la prueba', required=False)
    class Meta:
        model = TuModelo
        fields = [
            'introducetunombre',
            'eligetutalladecamiseta',
            'aceptoelreglamentodelaprueba',
        ]
        labels = {
            'introducetunombre': 'Introduce tu nombre',
            'eligetutalladecamiseta': 'Elige tu talla de camiseta',
        }
