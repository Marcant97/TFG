# views.py

from django.shortcuts import render
from .forms import TuFormulario

def mi_vista(request):
    if request.method == 'POST':
        form = TuFormulario(request.POST)
        if form.is_valid():
            form.save()
            # Realiza acciones adicionales después de guardar el formulario
    else:
        form = TuFormulario()
    return render(request, 'mi_template.html', {'form': form})
