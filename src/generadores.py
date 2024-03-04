# Función que se encarga de quitar los caracteres especiales y espacios de un string, para evitar problemas 
# con el nombre de los campos de las variables.
def limpiar_titulo(titulo):
  caracteres_validos = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
  titulo_sin_acentos = ''.join(c if c in caracteres_validos else '_' for c in titulo)
  return titulo_sin_acentos.lower().rstrip('_')


# # Ejemplo de uso con tu diccionario
# diccionario = [
#     {
#         "type": "text",
#         "title": "Introduce tu nombre completo:"
#     },
#     {
#         "type": "text",
#         "title": "Introduce tu dirección:"
#     }
# ]




def generar_models(miDiccionario):
  # Procesamos el diccionario
  # de momento sólo las preguntas con tipo "text"
  print('Creando modelos...')
  codigo = "from django.db import models\n\n"
  codigo += "class TuModelo(models.Model):\n"
  for pregunta in miDiccionario:
    if pregunta['type'] == 'text':
      titulo_limpio = limpiar_titulo(pregunta['title'])
      campo = f"    {titulo_limpio} = models.CharField(max_length=100)\n"
      codigo += campo

  # Escribir el código en el archivo
  with open("models.py", "w") as f:
      f.write(codigo)

# LLAMADA PARA HACER PRUEBAS
# generar_modelo(diccionario)





def generar_forms(miDiccionario):
  print('Creando formularios...')
  with open("forms.py", "w", encoding="utf-8") as file:
    file.write("from django import forms\n\n")
    file.write("class TuFormulario(forms.Form):\n")
    for pregunta in miDiccionario:
      tipo = pregunta.get("type", "")
      titulo = pregunta.get("title", "")
      nombre_campo = limpiar_titulo(titulo)
      if tipo == "text":
        file.write(f"    {nombre_campo} = forms.CharField(label='{titulo}', max_length=100)\n")
      # elif tipo == "number":
      #   f.write(f"    {nombre_campo} = forms.IntegerField(label='{titulo}')\n")
      # Agrega más tipos de campo según sea necesario
      else:
        print(f"Tipo de campo no válido para la pregunta: {titulo}")


# LLAMADA PARA HACER PRUEBAS
# generar_forms(diccionario)


def generar_views():
  print('Creando vistas...')
  codigo = "from django.shortcuts import render\n"
  codigo += "from .forms import TuFormulario\n"
  codigo += "from .models import TuModelo\n\n"

  codigo += "def mi_vista(request):\n"
  codigo += "    if request.method == 'POST':\n"
  codigo += "        form = TuFormulario(request.POST)\n"
  codigo += "        if form.is_valid():\n"
  codigo += "            form.save()\n"
  codigo += "            # Realiza acciones adicionales después de guardar el formulario\n"
  codigo += "    else:\n"
  codigo += "        form = TuFormulario()\n"
  codigo += "    return render(request, 'mi_template.html', {'form': form})\n"

  # Escribir el código en el archivo
  with open("views.py", "w") as f:
      f.write(codigo)

# LLAMADA PARA HACER PRUEBAS
# generar_views(diccionario)



def generar_template():
    print('Creando template...')
    codigo = """<!-- mi_template.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Formulario</title>
</head>
<body>
    <h2>Formulario</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
"""

    # Escribir el código en el archivo
    with open("mi_template.html", "w") as f:
        f.write(codigo)

# LLAMADA PARA HACER PRUEBAS
# generar_template()


def modify_urls_py():
  print('Modificando urls.py...')
  codigo = """from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.mi_vista, name='mi_vista'),
    path('admin/', admin.site.urls)
]
"""
  # Escribir el código en el archivo
  with open("urls.py", "w") as f:
    f.write(codigo)


# LLAMADA PARA HACER PRUEBAS
# modify_urls_py()
      


def modify_settings_py():
  print('Modificando settings.py...')
  with open("settings.py", "r") as f:
    lineas = f.readlines()

  # Buscar la línea que contiene 'INSTALLED_APPS'
  for i, linea in enumerate(lineas):
    if 'INSTALLED_APPS' in linea:
      # Añadir 'mysite' a INSTALLED_APPS
      lineas[i] = linea.rstrip()[:-1] + "[ 'mysite',\n"
      break

  # Escribir las líneas modificadas en el archivo
  with open("settings.py", "w") as f:
    f.writelines(lineas)
