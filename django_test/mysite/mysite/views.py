# views.py

from django.shortcuts import render
from .forms import TuFormulario
from .models import TuModelo


def mi_vista(request):
    if request.method == 'POST':
        form = TuFormulario(request.POST)
        if form.is_valid():
            form.save()
            # Realiza acciones adicionales después de guardar el formulario
            # Por ejemplo, podrías querer acceder a TuModelo aquí
            # Por ejemplo:
            nuevo_objeto = TuModelo(campo1=form.cleaned_data['campo1'], campo2=form.cleaned_data['campo2'])
            nuevo_objeto.save()
    else:
        form = TuFormulario()
    return render(request, 'mi_template.html', {'form': form})
