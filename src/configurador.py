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
  Función encargada de crear el proyecto Django.
  """
  try:
    print("\nCreando proyecto Django...")
    
    os.makedirs("django_test", exist_ok=True) # Crear el directorio para el proyecto
    os.chdir("django_test") # Cambiar al directorio del proyecto
    
    # python -m django startproject mytestsite
    subprocess.run(["python", "-m", "django", "startproject", "mysite"])
    
    os.chdir("mysite") # Cambiar al directorio del proyecto Django
    print("Proyecto Django creado correctamente.")


  except Exception as e:
    raise Exception(f"Error al crear el proyecto Django: {str(e)}")



def configurar_proyecto(miDiccionario):
  """
  Función encargada de configurar el proyecto Django.
  Args:
    miDiccionario (dict): diccionario con los datos del fichero JSON
  """

  try:
    
    print("\nConfigurando proyecto Django...")
    os.chdir("mysite")  # se cambias al directorio del proyecto Django "./django_test/mysite/mysite"

    
    generar_models(miDiccionario) #? 1. Crear y rellenar models.py
    generar_forms(miDiccionario)  #? 2. Crear y rellenar forms.py
    generar_views(miDiccionario)  #? 3. Crear y rellenar views.py

    #* 4. Se crea la subcarpeta /templates y nos movemos dentro de ella.
    os.makedirs("templates", exist_ok=True)
    os.chdir("templates")

    generar_templates()      #? 5. Se crea y rellena /templates/mi_template.html.
    os.chdir("..")           #* Volvemos al directorio raíz del proyecto.

    modificar_urls_py()      #? 6. Modificar urls.py
    modificar_settings_py()  #? 7. Modificar settings.py, se añade 'mysite' a INSTALLED_APPS.


    #? 8. Aplicar migraciones
      #* 8.1 cambiar de directorio a la raíz del proyecto, que es donde está el fichero manage.py
    os.chdir("..")
      
      #* 8.2 python manage.py makemigrations mysite
    subprocess.run(["python", "manage.py", "makemigrations", "mysite"])
      
      #* 8.3 python manage.py migrate
    subprocess.run(["python", "manage.py", "migrate"])


    #? PASO OPCIONAL --> Arrancar servidor en modo desarrollo ("python manage.py runserver")
    print("Arrancando servidor en modo desarrollo...")
    comando = 'start cmd /c "python manage.py runserver"'
    subprocess.run(comando, shell=True)
    
    time.sleep(2) # esperar 2 segundos, para que el servidor arranque.

    #? Abrir navegador y entrar en la dirección con "http://127.0.0.1:8000/formulario"
    url = "http://127.0.0.1:8000/formulario"
    webbrowser.open(url)

    #? 9. Crear superusuario (opcional)
    #? 9.1 se crea el superusuario
    # ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
    subprocess.run(["python", "manage.py", "shell", "-c", "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"])

    #? 9.2 se crea el fichero admin.py
    with open("mysite/admin.py", "w") as f:
      f.write("from django.contrib import admin\n")
      f.write("from .models import TuModelo\n")
      f.write("admin.site.register(TuModelo)")

    # El último paso necesario consiste en añadir la ruta de la aplicación al fichero urls.py del proyecto.
    # Este paso ya se realiza durante la configuración del proyecto, por lo tanto, no es necesario repetirlo.




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