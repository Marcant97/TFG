from django.shortcuts import render
from .forms import TuFormulario
from .models import TuModelo

def mi_vista(request):
    if request.method == 'POST':
        form = TuFormulario(request.POST)
        if form.is_valid():
            # se combina el número de teléfono con el prefijo antes de guardar el contenido del formulario en la base de datos.
            prefijo = request.POST.get('prefijo_introducetunmerodetelfono')
            numero_telefono = request.POST.get('introducetunmerodetelfono')
            numero_completo = f"{prefijo} {numero_telefono}"
             # Guarda el número de teléfono completo en el formulario
            form.instance.introducetunmerodetelfono = numero_completo
            form.save()
            # Realiza acciones adicionales después de guardar el formulario
    else:
        form = TuFormulario()
    return render(request, 'mi_template.html', {'form': form})
