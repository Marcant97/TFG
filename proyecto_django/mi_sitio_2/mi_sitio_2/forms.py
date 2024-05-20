from django import forms
from .models import TuModelo

from django.utils import timezone
from datetime import datetime
class TuFormulario(forms.ModelForm):
    opciones_casilladeseleccin = [
        ('opcion 1', 'opcion 1'),
        ('opcion 2', 'opcion 2'),
        ('opcion 3', 'opcion 3'),
    ]
    casilladeseleccin = forms.MultipleChoiceField(label='casilla de selección', required=False, widget=forms.CheckboxSelectMultiple, choices=opciones_casilladeseleccin)
    class Meta:
        model = TuModelo
        fields = [
            'casilladeseleccin',
        ]
