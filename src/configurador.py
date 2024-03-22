# script python encargado de configurar el proyecto
import subprocess
import os
import shutil
# pip install -r requirements.txt
import subprocess
import webbrowser
import time

from generadores import generar_models, generar_forms, generar_views, generar_template, modify_urls_py, modify_settings_py


def instalar_django():
  """
  Función encargada de comprobar la instalación de Django y, en caso de no estar instalado, instalarlo.
  """
  try:
    # Verificar si Django ya está instalado
    print("Verificando si Django ya está instalado...")
    subprocess.run(["pip", "show", "Django"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

  except subprocess.CalledProcessError:
    # Si hay un error, significa que Django no está instalado, entonces lo instalamos
    try:
      # Instalar Django
      print("Instalando Django...")
      subprocess.run(["pip", "install", "Django==5.0.1", "--user"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
      print("Django instalado correctamente.")
    except Exception as e:
      print(f"Error al instalar Django: {str(e)}")
      raise
    
  else:
    print("Django ya está instalado.")


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
    print(f"Error al crear el proyecto Django: {str(e)}")
    raise


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
    generar_forms(miDiccionario) #? 2. Crear y rellenar forms.py
    generar_views(miDiccionario) #? 3. Crear y rellenar views.py

    #* 4. Se crea la subcarpeta /templates y nos movemos dentro de ella.
    os.makedirs("templates", exist_ok=True)
    os.chdir("templates")

    generar_template() #? 5. Se crea y rellena /templates/mi_template.html.
    os.chdir("..")  #* Volvemos al directorio raíz del proyecto.

    modify_urls_py() #? 6. Modificar urls.py
    modify_settings_py() #? 7. Modificar settings.py, se añade 'mysite' a INSTALLED_APPS.


    #? 8. Aplicar migraciones
      #* 8.1 cambiar de directorio a la raíz del proyecto, que es donde está el fichero manage.py
    os.chdir("..")
      
      #* 8.2 python manage.py makemigrations mysite
    subprocess.run(["python", "manage.py", "makemigrations", "mysite"])
      
      #* 8.3 python manage.py migrate
    subprocess.run(["python", "manage.py", "migrate"])


    #!! PASO OPCIONAL --> Arrancar servidor en modo desarrollo ("python manage.py runserver")
    print("Arrancando servidor en modo desarrollo...")
    comando = 'start cmd /c "python manage.py runserver"'
    subprocess.run(comando, shell=True)
    
    time.sleep(2) # esperar 2 segundos, para que el servidor arranque.

    #? Abrir navegador y entrar en la dirección con "http://127.0.0.1:8000/formulario"
    url = "http://127.0.0.1:8000/formulario"
    webbrowser.open(url)

    # 9. Crear superusuario (opcional)



  except Exception as e:
    print(f"Error al configurar el proyecto Django: {str(e)}")
    raise





# Sin probar demasiado, no la he utilizado casi.
def borrar_proyecto():
  """
  Función encargada de borrar el proyecto Django.
  """
  try:
    # Obtener la ruta del directorio de trabajo actual
    directorio_actual = os.getcwd()
    # print("Directorio actual para borrar:", directorio_actual)
    # Borrar el proyecto Django
    print("Borrando proyecto Django...")
    proyecto_dir = os.path.join(directorio_actual, "django_test")  # Reemplaza con el nombre del proyecto
    shutil.rmtree(proyecto_dir)
    print("Proyecto Django borrado correctamente.")
  except Exception as e:
    print(f"Error al borrar el proyecto Django: {str(e)}")



# FUNCIONES SIN UTILIZAR.


# def arrancar_servidor():
#   # Arrancar servidor de desarrollo
#   print("Arrancando servidor de desarrollo...")
#   subprocess.run(["python", "manage.py", "runserver"])


# def desinstalar_django():
#   try:
#     # Desinstalar Django
#     print("Desinstalando Django...")
#     subprocess.run(["pip", "uninstall", "-y", "django"])
#     print("Django desinstalado correctamente.")
#   except Exception as e:
#     print(f"Error al desinstalar Django: {str(e)}")


