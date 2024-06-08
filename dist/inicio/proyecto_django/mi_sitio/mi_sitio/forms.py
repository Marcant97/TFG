from django import forms
from .models import TuModelo

from django.utils import timezone
from datetime import datetime
class TuFormulario(forms.ModelForm):
    opciones_indicalosserviciosquedeseas = [
        ('Corte de pelo', 'Corte de pelo'),
        ('Tinte', 'Tinte'),
        ('Peinado', 'Peinado'),
        ('Recogido', 'Recogido'),
        ('Lavado', 'Lavado'),
        ('Secado', 'Secado'),
        ('Tratamiento capilar', 'Tratamiento capilar'),
        ('Otro', 'Otro'),
    ]
    indicalosserviciosquedeseas = forms.MultipleChoiceField(label='Indica los servicios que deseas', required=False, widget=forms.CheckboxSelectMultiple, choices=opciones_indicalosserviciosquedeseas)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        min_date_eligelafechaparatucita = datetime.strptime('01/01/2024', '%d/%m/%Y').strftime('%Y-%m-%d')
        max_date_eligelafechaparatucita = datetime.strptime('08/06/2024', '%d/%m/%Y').strftime('%Y-%m-%d')
        self.fields['eligelafechaparatucita'].widget.attrs['min'] = min_date_eligelafechaparatucita
        self.fields['eligelafechaparatucita'].widget.attrs['max'] = max_date_eligelafechaparatucita
    class Meta:
        model = TuModelo
        fields = [
            'introducetunombre',
            'introducetudireccindecorreoelectrnico',
            'prefijo_introducetunmerodetelfono',
            'introducetunmerodetelfono',
            'eligetupeluqueroa',
            'eligelafechaparatucita',
            'eligelahoraparatucita',
            'indicalosserviciosquedeseas',
            'indicasitienesalgunapeticinespecial',
        ]
        labels = {
            'introducetunombre': 'Introduce tu nombre',
            'introducetudireccindecorreoelectrnico': 'Introduce tu dirección de correo electrónico',
            'prefijo_introducetunmerodetelfono': 'Prefijo telefónico',
            'introducetunmerodetelfono': 'Introduce tu número de teléfono',
            'eligetupeluqueroa': 'Elige tu peluquero/a',
            'eligelafechaparatucita': 'Elige la fecha para tu cita',
            'eligelahoraparatucita': 'Elige la hora para tu cita',
            'indicasitienesalgunapeticinespecial': 'Indica si tienes alguna petición especial',
        }
        widgets = {
            'eligelafechaparatucita': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'
                })
        }
