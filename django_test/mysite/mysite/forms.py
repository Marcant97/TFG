from django import forms
from .models import TuModelo

class TuFormulario(forms.ModelForm):
    class Meta:
        model = TuModelo
        fields = ['campo1', 'campo2']
