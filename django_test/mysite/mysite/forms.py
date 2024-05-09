from django import forms
from .models import TuModelo

class TuFormulario(forms.ModelForm):
    # Define las opciones para las casillas de verificación
    OPCIONES = [
        ('opcion1', 'Opción 1'),
        ('opcion2', 'Opción 2'),
        ('opcion3', 'Opción 3'),
        # Añade más opciones si es necesario
    ]

    # Define las casillas de verificación usando un campo ChoiceField
    opciones_correctas = forms.MultipleChoiceField(
        label='Selecciona las respuestas correctas:',
        required=False,
        widget=forms.CheckboxSelectMultiple,  # Usa CheckboxSelectMultiple para múltiples selecciones
        choices=OPCIONES,
    )

    class Meta:
        model = TuModelo
        fields = ['opciones_correctas']