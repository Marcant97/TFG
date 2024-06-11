from django.shortcuts import render, redirect
from .forms import TuFormulario
from .models import TuModelo

def home(request):
    return render(request, 'home.html')

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
            return redirect('vista_enviar')
    else:
        form = TuFormulario()
    return render(request, 'mi_template.html', {'form': form})
def vista_enviar(request):
    return render(request, 'enviar.html')