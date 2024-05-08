from datetime import datetime
import os

variables_creadas = [] # Lista para almacenar las variables creadas en el diccionario.

def generar_variables(miDiccionario):
  """
  Función que se encarga de agrgar un campo a cada pregunta del diccionario, quitando los caracteres especiales y espacios de un string, creando así un nombre 
  válido para cada variable del diccionario. En el caso de que existan preguntas idénticas en el diccionario, se añade un número al final del nombre de la variable.

  Args:
    titulo (str): cadena de caracteres a limpiar.

  Returns:
    str: cadena de caracteres limpia.
  """

  caracteres_validos = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
  for pregunta in miDiccionario:
    titulo_original = pregunta['titulo']
    titulo_limpio = ''.join(c if c in caracteres_validos else '' for c in titulo_original)
    nuevo_titulo = titulo_limpio.lower().rstrip('_')


    if nuevo_titulo not in variables_creadas:
      variables_creadas.append(nuevo_titulo)
      nombre_variable = {'nombre_variable': nuevo_titulo}
      pregunta.update(nombre_variable)

    else: # ya existe una pregunta con el mismo nombre de variable
      contador = 1
      while True:
        nuevo_titulo = f"{titulo_limpio}{contador}"
        if nuevo_titulo not in variables_creadas:
          variables_creadas.append(nuevo_titulo)
          nombre_variable = {'nombre_variable': nuevo_titulo}
          pregunta.update(nombre_variable)
          break
        contador += 1



def generar_models(miDiccionario):
  
  #^ Procesamos el diccionario para generar el modelo
  print('Creando modelos...')
  codigo = "from django.db import models\n\n"
  codigo += "from django.core.exceptions import ValidationError\n\n"


  #* Sólo para campos numéricos con límites.
  for pregunta in miDiccionario:
    if pregunta['tipo'] == 'numero':
      if 'valorMinimo' in pregunta or 'valorMaximo' in pregunta:
        codigo += "from django.core.validators import MinValueValidator, MaxValueValidator\n\n"
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
          bandera = True
      
        #^ generamos el código para el validador de dominios disponibles
        codigo += f"def f{pregunta['nombre_variable']}_email(value):\n"

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

  #* Sólo para preguntas del tipo dni.
  for pregunta in miDiccionario:
    if pregunta['tipo'] == 'dni':
      # introducir código de validar_dni.txt
      nombre_archivo = "../../../src/ficheros_generacion/validar_dni.txt"
      with open(nombre_archivo, "r", encoding="utf-8") as f:
        codigo += f.read() + "\n"
      break  

  #* Sólo para preguntas del tipo número de teléfono.
  # Se crea utils/prefijos.py a partir de src/ficheros_generacion/prefijos.txt y se importa en models.py el contenido.
  for pregunta in miDiccionario:
    if pregunta['tipo'] == 'telefono':
      codigo += "from .utils.prefijos import PREFIJOS\n\n"
      # generamos el fichero de prefijos en /utils/prefijos.py
      nombre_archivo = "../../../src/ficheros_generacion/prefijos.txt"
      with open(nombre_archivo, "r", encoding="utf-8") as f:
        contenido_fichero = f.read()

      os.makedirs("utils", exist_ok=True) # Crear el directorio para el proyecto
      os.chdir("utils")
      # Escribir el contenido del fichero en el fichero prefijos.py
      with open("prefijos.py", "w", encoding="utf-8") as f:
        f.write(contenido_fichero)
      os.chdir("..")

  codigo += ("from django.core.validators import RegexValidator\n\n")

  codigo += "class TuModelo(models.Model):\n"




  ###* Se procesan las preguntas del diccionario ###
  for pregunta in miDiccionario:

    titulo_limpio = pregunta['nombre_variable'] # Obtenemos un nombre de campo válido para una variable.

    #^ Tipo de campo de texto con opcionalmente límite de caracteres.
    if pregunta['tipo'] == 'texto':
      # Comprobar si hay un límite de caracteres (parámetro opcional)
      if 'limite' in pregunta:
        campo = f"  {titulo_limpio} = models.CharField(max_length={pregunta['limite']})\n"
      else:
        campo = f"  {titulo_limpio} = models.CharField(max_length=100)\n"
      
      codigo += campo


    #^ Tipo de campo numérico con opcionalmente mínimo y máximo.
    elif pregunta['tipo'] == 'numero':
      valorMinimo = pregunta.get('valorMinimo', None)
      valorMaximo = pregunta.get('valorMaximo', None)
      if valorMinimo != None and valorMaximo != None:
        print('valorMinimo y valorMaximo presentes')
        campo = f"  {titulo_limpio} = models.IntegerField(validators=[MinValueValidator({valorMinimo}), MaxValueValidator({valorMaximo})])\n"
      elif valorMinimo != None:
        print('valorMinimo presente')
        campo = f"  {titulo_limpio} = models.IntegerField(validators=[MinValueValidator({valorMinimo})])\n"
      elif valorMaximo != None:
        print('valorMaximo presente')
        campo = f"  {titulo_limpio} = models.IntegerField(validators=[MaxValueValidator({valorMaximo})])\n"
      else:
        campo = f"  {titulo_limpio} = models.IntegerField()\n"
      codigo += campo


    #^ Tipo de campo para preguntas con varias opciones con sólo una repuesta correcta (desplegable)
    elif pregunta['tipo'] == 'desplegable':
      campo = f"  {titulo_limpio} = models.CharField(max_length=100, choices=["

      # Se itera sobre las opciones disponibles.
      for opcion in pregunta['opciones']:
          campo += f"('{opcion}', '{opcion}'),"
      
      campo += "])\n"
      codigo += campo


    #^ Tipo de campo para preguntas de selección múltiple (casilla)
    elif pregunta['tipo'] == 'casilla':
      campo = f"  {titulo_limpio} = models.BooleanField(default=False)\n"
      codigo += campo


    #^ Tipo de campos para preguntas de tipo específico, email.
    elif pregunta['tipo'] == 'email':

      # Determinamos si existe el campo dominiosDisponibles
      checkdominiosDisponibles = pregunta.get('dominiosDisponibles', None)

      if checkdominiosDisponibles != None:
        campo = f"  {titulo_limpio} = models.EmailField(max_length=254, validators=[validate_email,f{titulo_limpio}_email])\n"
      else:
        campo = f"  {titulo_limpio} = models.EmailField(max_length=254)\n"
      codigo += campo

    #^ Tipo de campos para preguntas de tipo específico, dni.
    elif pregunta['tipo'] == 'dni':
      campo = f"  {titulo_limpio} = models.CharField(max_length=9, validators=[validar_dni])\n"
      codigo += campo


    #^ Tipo de campos para preguntas de tipo específico, fecha.
    elif pregunta['tipo'] == 'fecha':
      campo = f"  {titulo_limpio} = models.DateField()\n"
      codigo += campo


    #^ Tipo de campo para preguntas de tipo específico, numero de teléfono.
    elif pregunta['tipo'] == 'telefono':
      campo = f"  prefijo_{titulo_limpio} = models.CharField(max_length=14, blank=True, choices=PREFIJOS)\n"
      campo += f"  {titulo_limpio} = models.CharField(max_length=14, blank=True)\n"
      codigo += campo

    #^ Tipo de campo para preguntas de tipo específico, campo especial.
    elif pregunta['tipo'] == 'campoEspecial':
      titulo = pregunta.get("titulo", "")
      # nombre_campo = limpiar_titulo(titulo)
      expresion_regular = pregunta.get("expresionRegular", "")
      if expresion_regular != "":
        codigo += (f"  {titulo_limpio} = models.CharField(max_length=200, validators=[RegexValidator(regex='{expresion_regular}', message='Introduzca un valor que cumpla la expresión regular: {expresion_regular}')])\n")


    else:
      print(f"Tipo de campo no válido para la pregunta: {pregunta['titulo']}")
      continue

    

  # Escribir el código en el archivo
  with open("models.py", "w", encoding="utf-8") as f:
      f.write(codigo)




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
    # importaciones para los campos de fecha
    file.write("from django.utils import timezone\n")
    file.write("from datetime import datetime\n")


    file.write("class TuFormulario(forms.ModelForm):\n")
    #? Parte específica sólo para las preguntas del tipo casilla.
    for pregunta in miDiccionario:
      if pregunta['tipo'] == 'casilla':
        titulo = pregunta.get("titulo", "")
        nombre_campo = pregunta['nombre_variable']
        obligatorio = pregunta.get("obligatorio", False)
        file.write(f"    {nombre_campo} = forms.BooleanField(label='{titulo}', required={obligatorio})\n")

    #? Parte específica sólo para las preguntas del tipo fecha, se importan lo necesario para gestionar las fechas mínimas y máximas.
    primera_fecha_formulario = True
    for pregunta in miDiccionario:
      if pregunta['tipo'] == 'fecha':
        titulo = pregunta['nombre_variable']
        # obtenemos la primera fecha y la última fecha

        primera_fecha = pregunta.get('primeraFecha', '01/01/1900') # por defecto, la primera fecha es 01/01/1900.
        ultima_fecha = pregunta.get('ultimaFecha', datetime.now().strftime('%d/%m/%Y')) # por defecto, la útlima fecha es hoy.

        if primera_fecha_formulario == True:
          file.write("    def __init__(self, *args, **kwargs):\n")
          file.write("        super().__init__(*args, **kwargs)\n")
          primera_fecha_formulario = False

        file.write(f"        min_date_{titulo} = datetime.strptime('{primera_fecha}', '%d/%m/%Y').strftime('%Y-%m-%d')\n")
        file.write(f"        max_date_{titulo} = datetime.strptime('{ultima_fecha}', '%d/%m/%Y').strftime('%Y-%m-%d')\n")
        file.write(f"        self.fields['{titulo}'].widget.attrs['min'] = min_date_{titulo}\n")
        file.write(f"        self.fields['{titulo}'].widget.attrs['max'] = max_date_{titulo}\n")


    #? Parte común para el resto de preguntas.
    file.write("    class Meta:\n")
    file.write("        model = TuModelo\n")
    file.write("        fields = [\n")

    #* Se recorren las preguntas del diccionario
    for pregunta in miDiccionario:
      tipo = pregunta.get("tipo", "")
      titulo = pregunta.get("titulo", "")
      nombre_campo = pregunta['nombre_variable']

      if tipo == 'telefono':
        file.write(f"            'prefijo_{nombre_campo}',\n")
        
      file.write(f"            '{nombre_campo}',\n")

    file.write("        ]\n")

    # si existe un campo cuyo tipo sea diferente a 'casilla', se añade el atributo 'labels' al formulario.
    if any(pregunta['tipo'] != 'casilla' for pregunta in miDiccionario):
      # se evita escribir labels vacío si sólo hay casillas.
      file.write("        labels = {\n")
      #* Se recorren las preguntas del diccionario
      for pregunta in miDiccionario:
        tipo = pregunta.get("tipo", "")
        titulo = pregunta.get("titulo", "")
        nombre_campo = pregunta['nombre_variable']
        if tipo != 'casilla':
          if tipo == 'telefono':
            file.write(f"            'prefijo_{nombre_campo}': 'Prefijo telefónico',\n")
          file.write(f"            '{nombre_campo}': '{titulo}',\n")

      file.write("        }\n")

    primera_fecha = True
    for pregunta in miDiccionario:
      if pregunta['tipo'] == 'fecha':
        nombre_campo = pregunta['nombre_variable']

        if primera_fecha:
          file.write("        widgets = {\n")
          file.write(f"            '{nombre_campo}': forms.DateInput(\n")
          primera_fecha = False
        
        else:
          file.write(f"            ,'{nombre_campo}': forms.DateInput(\n")

        # común
        file.write("                attrs={'type': 'date', 'class': 'form-control'\n")
        file.write("                })\n")

    if primera_fecha == False: # hay una fecha mínimo, cerramos widget
        file.write("        }\n")





def generar_views(miDiccionario):
  """
  Función que se encarga de generar el fichero views.py del proyecto.
  Args:
    miDiccionario (dict): Diccionario con las preguntas del formulario.
  """
  print('Creando vistas...')
  codigo = "from django.shortcuts import render, redirect\n"
  codigo += "from .forms import TuFormulario\n"
  codigo += "from .models import TuModelo\n\n"

  # vista para el home
  codigo += "def home(request):\n"
  codigo += "    return render(request, 'home.html')\n\n"

  codigo += "def mi_vista(request):\n"
  codigo += "    if request.method == 'POST':\n"
  codigo += "        form = TuFormulario(request.POST)\n"
  codigo += "        if form.is_valid():\n"

  codigo += "            # se combina el número de teléfono con el prefijo antes de guardar el contenido del formulario en la base de datos.\n"
  for pregunta in miDiccionario:
    if pregunta['tipo'] == 'telefono':
      titulo = pregunta.get("titulo", "")
      nombre_campo = pregunta['nombre_variable']
      codigo += f"            prefijo = request.POST.get('prefijo_{nombre_campo}')\n"
      codigo += f"            numero_telefono = request.POST.get('{nombre_campo}')\n"
      codigo += f"            numero_completo = f\"{{prefijo}} {{numero_telefono}}\"\n"
      codigo += "             # Guarda el número de teléfono completo en el formulario\n"
      codigo += f"            form.instance.{nombre_campo} = numero_completo\n"  
  
  codigo += "            form.save()\n"
  codigo += "            return redirect('vista_enviar')\n"

  codigo += "    else:\n"
  codigo += "        form = TuFormulario()\n"
  codigo += "    return render(request, 'mi_template.html', {'form': form})\n"

  # vista para después de enviar el formulario.
  codigo += "def vista_enviar(request):\n"
  codigo += "    return render(request, 'enviar.html')\n"

  # Escribir el código en el archivo
  with open("views.py", "w", encoding="utf-8") as f:
      f.write(codigo)




def generar_templates():
  """
  Función que se encarga de generar el fichero mi_template.html del proyecto.
  """
  print('Creando templates...')

  mi_template = ""
  mi_home = ""
  mi_enviar = ""

  with open("../../../../src/templates/mi_template.html", "r", encoding="utf-8") as file:
    mi_template = file.read()
  
  with open("../../../../src/templates/home.html", "r", encoding="utf-8") as file:
    mi_home = file.read()

  with open("../../../../src/templates/enviar.html", "r", encoding="utf-8") as file:
    mi_enviar = file.read()


  # Escribir el código en el archivo
  with open("mi_template.html", "w", encoding="utf-8") as f:
    f.write(mi_template)

  with open("home.html", "w", encoding="utf-8") as f:
    f.write(mi_home)

  with open("enviar.html", "w", encoding="utf-8") as f:
    f.write(mi_enviar)



def modificar_urls_py():
  """
  Función encargada de actualizar el archivo urls.py del proyecto.
  """
  print('Modificando urls.py...')
  codigo = """from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('formulario/', views.mi_vista, name='mi_vista'),
    path('admin/', admin.site.urls),
    path('enviar/', views.vista_enviar, name='vista_enviar')
]
"""
  # Escribir el código en el archivo
  with open("urls.py", "w", encoding="utf-8") as f:
    f.write(codigo)
      

def modificar_settings_py():

  print('Modificando settings.py...')

  #* Se abre el fichero en modo lectura
  with open("settings.py", "r", encoding="utf-8") as f:
    lineas = f.readlines() # Leemos las líneas del fichero

  # Recorremos las líneas en busca de la lista INSTALLED_APPS
  for i, linea in enumerate(lineas):
    #* Si encontramos la línea, le añadimos 'mysite' a la lista
    if 'INSTALLED_APPS' in linea:
      lineas[i] = "INSTALLED_APPS = [ 'mysite',\n"
    elif 'LANGUAGE_CODE' in linea:
      lineas[i] = "LANGUAGE_CODE = 'es-es'\n"

  # Escribir las líneas modificadas en el archivo
  with open("settings.py", "w", encoding="utf-8") as f:
    f.writelines(lineas)
    f.write('DATE_FORMAT = "%d/%m/%Y"\n')
    f.write("USE_L10N = False")


