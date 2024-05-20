# script python encargado de configurar el proyecto
import subprocess
import os
import shutil
import subprocess
import webbrowser
import time

from generadores import generar_models, generar_forms, generar_views, generar_templates, modificar_urls_py, modificar_settings_py


def verificar_django():
  """
  Función encargada de comprobar la instalación de Django y, en caso de no estar instalado, devolver un error.
  """
  try:
    # Intentamos importar Django
    import django
  except ImportError:
    mensaje_error = "Django no está instalado. Por favor, instale Django antes de continuar."
    raise Exception(mensaje_error)


def crear_proyecto():
    """
    Función encargada de crear el proyecto Django con nombre único.
    """
    directorio_base = "proyecto_django"
    nombre_base = "mi_sitio"
    contador = 1

    try:
      print("\nCreando proyecto Django...")

      # Crear el directorio base si no existe
      os.makedirs(directorio_base, exist_ok=True)
      os.chdir(directorio_base)  # Cambiar al directorio base

      # Generar un nombre único para el proyecto
      nombre_unico = nombre_base
      while os.path.exists(nombre_unico):
          nombre_unico = f"{nombre_base}_{contador}"
          contador += 1

      # Crear el proyecto Django
      subprocess.run(["python", "-m", "django", "startproject", nombre_unico])

      os.chdir(nombre_unico)  # Cambiar al directorio del proyecto Django
      print(f"Proyecto Django '{nombre_unico}' creado correctamente.")

      return nombre_unico

    except Exception as e:
      raise Exception(f"Error al crear el proyecto Django: {str(e)}")



def configurar_proyecto(miDiccionario, nombre_proyecto):
  """
  Función encargada de configurar el proyecto Django.
  Args:
    miDiccionario (dict): diccionario con los datos del fichero JSON
  """

  try:
    
    print("\nConfigurando proyecto Django...")
    os.chdir(nombre_proyecto)  # se cambias al directorio del proyecto Django "./django_test/nombre_proyecto/nombre_proyecto"

    
    generar_models(miDiccionario) #? 1. Crear y rellenar models.py
    generar_forms(miDiccionario)  #? 2. Crear y rellenar forms.py
    generar_views(miDiccionario)  #? 3. Crear y rellenar views.py

    #* 4. Se crea la subcarpeta /templates y nos movemos dentro de ella.
    os.makedirs("templates", exist_ok=True)
    os.chdir("templates")

    generar_templates()      #? 5. Se crea y rellena /templates/mi_template.html.
    os.chdir("..")           #* Volvemos al directorio raíz del proyecto.

    modificar_urls_py()      #? 6. Modificar urls.py
    modificar_settings_py(nombre_proyecto)  #? 7. Modificar settings.py, se añade 'nombre_proyecto' a INSTALLED_APPS.


    #? 8. Aplicar migraciones
      #* 8.1 cambiar de directorio a la raíz del proyecto, que es donde está el fichero manage.py
    os.chdir("..")
      
      #* 8.2 python manage.py makemigrationsnombre_proyecto
    subprocess.run(["python", "manage.py", "makemigrations", nombre_proyecto])
      
      #* 8.3 python manage.py migrate
    subprocess.run(["python", "manage.py", "migrate"])


    #? 9. Crear superusuario (opcional)
    #? 9.1 se crea el superusuario
    # ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
    subprocess.run(["python", "manage.py", "shell", "-c", "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"])

    #? 9.2 se crea el fichero admin.py
    # "nombre_proyecto/admin.py"
    ruta = os.path.join(nombre_proyecto, "admin.py")
    with open(ruta, "w") as f:
      f.write("from django.contrib import admin\n")
      f.write("from .models import TuModelo\n\n")
      f.write("admin.site.register(TuModelo)")

    # El último paso necesario consiste en añadir la ruta de la aplicación al fichero urls.py del proyecto.
    # Este paso ya se realiza durante la configuración del proyecto, por lo tanto, no es necesario repetirlo.

    
    #? PASO OPCIONAL --> Arrancar servidor en modo desarrollo ("python manage.py runserver")
    print("Arrancando servidor en modo desarrollo...")
    comando = 'start cmd /c "python manage.py runserver"'
    subprocess.run(comando, shell=True)
    
    time.sleep(2) # esperar 2 segundos, para que el servidor arranque.

    #? Abrir navegador y entrar en la dirección con "http://127.0.0.1:8000/formulario"
    url = "http://127.0.0.1:8000/formulario"
    webbrowser.open(url)

  except Exception as e:
    print(f"Error al configurar el proyecto Django: {str(e)}")
    raise



def borrar_proyecto():
  """
  Función encargada de borrar el proyecto Django.
  """
  try:
    # Obtener la ruta del directorio de trabajo actual
    directorio_actual = os.getcwd()
    
    # Construir la ruta del directorio del proyecto
    proyecto_dir = os.path.join(directorio_actual, "django_test")  # Reemplaza con el nombre del proyecto
    
    # Verificar si el directorio del proyecto existe
    if os.path.exists(proyecto_dir):
      # Borrar el proyecto Django si existe
      print("Borrando proyecto Django...")
      shutil.rmtree(proyecto_dir)
      print("Proyecto Django borrado correctamente.")
          
  except Exception as e:
    mensaje_error = f"Error al borrar el proyecto Django: {str(e)}"
    raise Exception(mensaje_error)