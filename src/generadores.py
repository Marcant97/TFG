
def limpiar_titulo(titulo):
    """
    Función que se encarga de quitar los caracteres especiales y espacios de un string, creando así un nombre 
    válido para una variable.

    Args:
      titulo (str): cadena de caracteres a limpiar.

    Returns:
      str: cadena de caracteres limpia.
    """

    caracteres_validos = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    titulo_limpio = ''.join(c if c in caracteres_validos else '' for c in titulo)
    return titulo_limpio.lower().rstrip('_')



def generar_models(miDiccionario):
  
  #^ Procesamos el diccionario para generar el modelo
  print('Creando modelos...')
  codigo = "from django.db import models\n\n"

  #* Sólo para campos numéricos con límites.
  for pregunta in miDiccionario:
    if pregunta['tipo'] == 'numero':
      if 'valorMinimo' in pregunta or 'valorMaximo' in pregunta:
        codigo += "from django.core.validators import valorMinimoValidator, valorMaximoValidator\n\n"
        break


  #* Sólo para preguntas email con dominios específicos.
  bandera = False # bandera para controlar si ya hemos importado los validadores
  for pregunta in miDiccionario:
    if pregunta['tipo'] == 'email':

      if ('dominiosDisponibles' in pregunta):

        #? Si es la primera pregunta del tipo email
        if not bandera:
          codigo += "from django.core.validators import EmailValidator\n"
          codigo += "from django.core.validators import validate_email\n"
          codigo += "from django.core.exceptions import ValidationError\n\n"
          bandera = True
      
        #^ generamos el código para el validador de dominios disponibles
        codigo += f"def f{limpiar_titulo(pregunta['titulo'])}_email(value):\n"

        #^ lo convertimos en una string y le quitamos "'", para que sea válido en el código
        dominiosDisponiblesError = str(pregunta['dominiosDisponibles']).replace("'", "")
        dominiosDisponibles = pregunta['dominiosDisponibles']
        # if not value.endswith('ull.edu.es') and not value.endswith('ull.es'):
        if (len(dominiosDisponibles) == 1):
          codigo += f"    if not value.endswith('{dominiosDisponibles[0]}'):\n"
        else:
          codigo += f"    if not"
          for i in range(len(dominiosDisponibles)):
            if i == len(dominiosDisponibles)-1: # si es el último, no se añade 'and not' y se cierra
              codigo += f" value.endswith('{dominiosDisponibles[i]}'):\n"
            else: # si no es el último, se añade 'and not'
              codigo += f" value.endswith('{dominiosDisponibles[i]}') and not"


        #codigo += f"    if not value.endswith({dominiosDisponibles}):\n"
        errorString = f"'El correo electrónico debe ser del dominio {dominiosDisponiblesError}'"
        codigo += f"        raise ValidationError({errorString})\n\n"
        


  codigo += "class TuModelo(models.Model):\n"

  ###* Se procesan las preguntas del diccionario ###
  for pregunta in miDiccionario:

    titulo_limpio = limpiar_titulo(pregunta['titulo']) # Obtenemos un nombre de campo válido para una variable.

    #^ Tipo de campo de texto con opcionalmente límite de caracteres.
    if pregunta['tipo'] == 'texto':
      # Comprobar si hay un límite de caracteres (parámetro opcional)
      if 'limite' in pregunta:
        campo = f"    {titulo_limpio} = models.CharField(max_length={pregunta['limite']})\n"
      else:
        campo = f"    {titulo_limpio} = models.CharField(max_length=100)\n"
      
      codigo += campo


    #^ Tipo de campo numérico con opcionalmente mínimo y máximo.
    elif pregunta['tipo'] == 'numero':
      valorMinimo = pregunta.get('valorMinimo', None)
      valorMaximo = pregunta.get('valorMaximo', None)
      if valorMinimo != None and valorMaximo != None:
        print('valorMinimo y valorMaximo presentes')
        campo = f"    {titulo_limpio} = models.IntegerField(validators=[valorMinimoValidator({valorMinimo}), valorMaximoValidator({valorMaximo})])\n"
      elif valorMaximo != None:
        print('valorMinimo presente')
        campo = f"    {titulo_limpio} = models.IntegerField(validators=[valorMinimoValidator({valorMinimo})])\n"
      elif valorMaximo != None:
        print('valorMaximo presente')
        campo = f"    {titulo_limpio} = models.IntegerField(validators=[valorMaximoValidator({valorMaximo})])\n"
      else:
        campo = f"    {titulo_limpio} = models.IntegerField()\n"
      codigo += campo


    #^ Tipo de campo para preguntas con varias opciones con sólo una repuesta correcta (desplegable)
    elif pregunta['tipo'] == 'desplegable':
      campo = f"    {titulo_limpio} = models.CharField(max_length=100, opciones=["

      # Se itera sobre las opciones disponibles.
      for opcion in pregunta['opciones']:
          campo += f"('{opcion}', '{opcion}'),"
      
      campo += "])\n"
      codigo += campo


    #^ Tipo de campo para preguntas de selección múltiple (casilla)
    elif pregunta['tipo'] == 'casilla':
      campo = f"    {titulo_limpio} = models.BooleanField(default=False)\n"
      codigo += campo

    #^ Tipo de campo para preguntas de multiple elección. 
    # ? Es posible que no lo implemente, su funcionalidad ya se cumple con desplegable y casilla.
      
  
    #^ Tipo de campos para preguntas de tipo específico, email.
    elif pregunta['tipo'] == 'email':

      # Determinamos si existe el campo dominiosDisponibles
      checkdominiosDisponibles = pregunta.get('dominiosDisponibles', None)

      if checkdominiosDisponibles != None:
        campo = f"    {titulo_limpio} = models.EmailField(max_length=254, validators=[validate_email,f{titulo_limpio}_email])\n"
      else:
        campo = f"    {titulo_limpio} = models.EmailField(max_length=254)\n"
      codigo += campo



    # tiposEspecificos = ["email", "dni", "phonenumero", "date", "specialField"]
    else:
      print(f"Tipo de campo no válido para la pregunta: {pregunta['titulo']}")
      continue

    

  # Escribir el código en el archivo
  with open("models.py", "w", encoding="utf-8") as f:
      f.write(codigo)

# LLAMADA PARA HACER PRUEBAS
# generar_modelo(diccionario)



def generar_forms(miDiccionario):
  """
  Función que se encarga de generar el fichero forms.py del proyecto.
  Args:
    miDiccionario (dict): Diccionario con las preguntas del formulario.
  """

  print('Creando formularios...')

  with open("forms.py", "w", encoding="utf-8") as file:
    
    file.write("from django import forms\n")
    file.write("from .models import TuModelo\n\n")

    file.write("class TuFormulario(forms.ModelForm):\n")

    #? Parte específica sólo para las preguntas del tipo casilla.
    for pregunta in miDiccionario:
      if pregunta['tipo'] == 'casilla':
        titulo = pregunta.get("titulo", "")
        nombre_campo = limpiar_titulo(titulo)
        obligatorio = pregunta.get("obligatorio", False)
        file.write(f"    {nombre_campo} = forms.BooleanField(label='{titulo}', obligatorio={obligatorio})\n")

    #? Parte común para el resto de preguntas.
    file.write("    class Meta:\n")
    file.write("        model = TuModelo\n")
    file.write("        fields = [\n")

    #* Se recorren las preguntas del diccionario
    for pregunta in miDiccionario:
      tipo = pregunta.get("tipo", "")
      titulo = pregunta.get("titulo", "")
      nombre_campo = limpiar_titulo(titulo)
      file.write(f"            '{nombre_campo}',\n") 

    file.write("        ]\n")
    file.write("        labels = {\n")

    #* Se recorren las preguntas del diccionario
    for pregunta in miDiccionario:
      titulo = pregunta.get("titulo", "")
      nombre_campo = limpiar_titulo(titulo)
      file.write(f"            '{nombre_campo}': '{titulo}',\n")

    file.write("        }\n")

# LLAMADA PARA HACER PRUEBAS
# generar_forms(diccionario)



def generar_views(miDiccionario):
  """
  Función que se encarga de generar el fichero views.py del proyecto.
  Args:
    miDiccionario (dict): Diccionario con las preguntas del formulario.
  """
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
  """
  Función que se encarga de generar el fichero mi_template.html del proyecto.
  """
  print('Creando template...')
  codigo = """<!-- mi_template.html -->

<!DOCtipo html>
<html>
<head>
    <titulo>Formulario</titulo>
</head>
<body>
    <h2>Formulario</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button tipo="submit">Enviar</button>
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
  """
  Función encargada de actualizar el archivo urls.py del proyecto.
  """
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

  #* Se abre el fichero en modo lectura
  with open("settings.py", "r", encoding="utf-8") as f:
    lineas = f.readlines() # Leemos las líneas del fichero

  # Recorremos las líneas en busca de la lista INSTALLED_APPS
  for i, linea in enumerate(lineas):
    #* Si encontramos la línea, le añadimos 'mysite' a la lista
    if 'INSTALLED_APPS' in linea:
      lineas[i] = "INSTALLED_APPS = [ 'mysite',\n"

  # Escribir las líneas modificadas en el archivo
  with open("settings.py", "w", encoding="utf-8") as f:
    f.writelines(lineas)

