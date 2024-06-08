from django import forms
from .models import TuModelo

from django.utils import timezone
from datetime import datetime
class TuFormulario(forms.ModelForm):
    opciones_indicaloquetehagustado = [
        ('La calidad del producto', 'La calidad del producto'),
        ('El precio', 'El precio'),
        ('La atención al cliente', 'La atención al cliente'),
        ('La rapidez en la entrega', 'La rapidez en la entrega'),
        ('Otro', 'Otro'),
        ('Nada', 'Nada'),
    ]
    indicaloquetehagustado = forms.MultipleChoiceField(label='Indica lo que te ha gustado', required=False, widget=forms.CheckboxSelectMultiple, choices=opciones_indicaloquetehagustado)
    class Meta:
        model = TuModelo
        fields = [
            'seleccionaturangodeedad',
            'eligetugnero',
            'indicaloquetehagustado',
            'eligedel110tugradodesatisfaccin',
            'djanostussugerenciasfelicitacionesoquejas',
        ]
        labels = {
            'seleccionaturangodeedad': 'Selecciona tu rango de edad',
            'eligetugnero': 'Elige tu género',
            'eligedel110tugradodesatisfaccin': 'Elige del 1-10 tu grado de satisfacción',
            'djanostussugerenciasfelicitacionesoquejas': 'Déjanos tus sugerencias, felicitaciones o quejas',
        }
