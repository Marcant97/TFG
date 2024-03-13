from django.core.validators import MinValueValidator, MaxValueValidator


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



# Función que se encarga de quitar los caracteres especiales y espacios de un string, para evitar problemas 
# con el nombre de los campos de las variables.
def limpiar_titulo(titulo):
    caracteres_validos = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    titulo_limpio = ''.join(c if c in caracteres_validos else '' for c in titulo)
    return titulo_limpio.lower().rstrip('_')




def generar_models(miDiccionario):
  # Procesamos el diccionario
  # ! de momento sólo las preguntas con tipo "text"
  print('Creando modelos...')
  codigo = "from django.db import models\n\n"
  # *Comprobar si hay un campo numérico con límites, para añadir los validadores de django.
  for pregunta in miDiccionario:
    if pregunta['type'] == 'number':
      if 'minValue' in pregunta or 'maxValue' in pregunta:
        codigo += "from django.core.validators import MinValueValidator, MaxValueValidator\n\n"
        break
  codigo += "class TuModelo(models.Model):\n"


  ### * Se procesan las preguntas ###
  for pregunta in miDiccionario:

    titulo_limpio = limpiar_titulo(pregunta['title']) # Limpiar el título para que sea un nombre de campo válido

    #^ Tipo de campo de texto con opcionalmente límite de caracteres.
    if pregunta['type'] == 'text':
      # Comprobar si hay un límite de caracteres (parámetro opcional)
      if 'limit' in pregunta:
        campo = f"    {titulo_limpio} = models.CharField(max_length={pregunta['limit']})\n"
      else:
        campo = f"    {titulo_limpio} = models.CharField(max_length=100)\n"
      
      codigo += campo


    #^ Tipo de campo numérico con opcionalmente mínimo y máximo.
    elif pregunta['type'] == 'number':
      minValue = pregunta.get('minValue', None)
      maxValue = pregunta.get('maxValue', None)
      if minValue != None and maxValue != None:
        print('minValue y maxValue presentes')
        campo = f"    {titulo_limpio} = models.IntegerField(validators=[MinValueValidator({minValue}), MaxValueValidator({maxValue})])\n"
      elif minValue != None:
        print('minValue presente')
        campo = f"    {titulo_limpio} = models.IntegerField(validators=[MinValueValidator({minValue})])\n"
      elif maxValue != None:
        print('maxValue presente')
        campo = f"    {titulo_limpio} = models.IntegerField(validators=[MaxValueValidator({maxValue})])\n"
      else:
        campo = f"    {titulo_limpio} = models.IntegerField()\n"
      codigo += campo


    #^ Tipo de campo para preguntas con varias opciones con sólo una repuesta correcta (dropdown)
    elif pregunta['type'] == 'dropdown':
      
      campo = f"    {titulo_limpio} = models.CharField(max_length=100, choices=["
      # Se itera sobre las opciones ("choices") disponibles.
      for choice in pregunta['choices']:
          campo += f"('{choice}', '{choice}'),"
      
      campo += "])\n"
      codigo += campo



    #^ Tipo de campo para preguntas de multiple elección. 
    # Si multipleAnswers es True, pueden haber varias respuestas, si está a false, sólo una.
    # elif pregunta['type'] == 'multipleChoice':
    #   multipleAnswers = pregunta.get('multipleAnswers', None)
    #   campo = f"    {titulo_limpio} = models.ManyToManyField('Choice', related_name='{titulo_limpio}')\n"
    #   codigo += campo

    #   # Crear el modelo Choice
    #   codigo += "\nclass Choice(models.Model):\n"
    #   codigo += "    id = models.AutoField(primary_key=True)\n"
    #   codigo += "    choice = models.CharField(max_length=100)\n"
    #   codigo += "    is_correct = models.BooleanField(default=False)\n"
    #   default_choices = {choice['choice']: choice['answer'] for choice in pregunta['choices']}
    #   codigo += f"    choices = models.JSONField(default={default_choices})\n"
      
    

    else:
      print(f"Tipo de campo no válido para la pregunta: {pregunta['title']}")
      continue

    

  # Escribir el código en el archivo
  with open("models.py", "w", encoding="utf-8") as f:
      f.write(codigo)

# LLAMADA PARA HACER PRUEBAS
# generar_modelo(diccionario)



def generar_forms(miDiccionario):
  print('Creando formularios...')
  with open("forms.py", "w", encoding="utf-8") as file:
    file.write("from django import forms\n")
    file.write("from .models import TuModelo\n\n")

    file.write("class TuFormulario(forms.ModelForm):\n")
    file.write("    class Meta:\n")
    file.write("        model = TuModelo\n")

    file.write("        fields = [\n")
    for pregunta in miDiccionario:
      tipo = pregunta.get("type", "")
      titulo = pregunta.get("title", "")
      nombre_campo = limpiar_titulo(titulo)
      # if tipo == "text":
      # Comentado por que en realidad el tipo da igual, todas las variables se añaden.
      file.write(f"            '{nombre_campo}',\n") 

    file.write("        ]\n")
    file.write("        labels = {\n")

    for pregunta in miDiccionario:
      tipo = pregunta.get("type", "")
      titulo = pregunta.get("title", "")
      nombre_campo = limpiar_titulo(titulo)
      # if tipo == "text":
      # Comentado por que en realidad el tipo da igual, todas las variables se añaden.
      file.write(f"            '{nombre_campo}': '{titulo}',\n")

    file.write("        }\n")

# LLAMADA PARA HACER PRUEBAS
# generar_forms(diccionario)




def generar_views(miDiccionario):
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
  with open("views.py", "w", encoding="utf-8") as f:
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
    with open("mi_template.html", "w", encoding="utf-8") as f:
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
  with open("urls.py", "w", encoding="utf-8") as f:
    f.write(codigo)


# LLAMADA PARA HACER PRUEBAS
# modify_urls_py()
      

def modify_settings_py():
  print('Modificando settings.py...')
  with open("settings.py", "r", encoding="utf-8") as f:
    lineas = f.readlines()

  # Buscar la línea que contiene 'INSTALLED_APPS'
  for i, linea in enumerate(lineas):
    if 'INSTALLED_APPS' in linea:
      lineas[i] = "INSTALLED_APPS = [ 'mysite',\n"

  # Escribir las líneas modificadas en el archivo
  with open("settings.py", "w", encoding="utf-8") as f:
    f.writelines(lineas)

