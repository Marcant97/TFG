# script python encargado de configurar el proyecto

import subprocess
import os
import shutil

# pip install -r requirements.txt
import subprocess

def instalar_django():
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
  else:
    print("Django ya está instalado.")



def crear_proyecto():
  try:
    # Crear proyecto Django
    print("Creando proyecto Django...")
    # Crear el directorio para el proyecto
    os.makedirs("django_test", exist_ok=True)
    # Cambiar al directorio del proyecto
    os.chdir("django_test")
    # print("Directorio actual:", os.getcwd())
    # Iniciar el proyecto Django
    # python -m django startproject mytestsite
    subprocess.run(["python", "-m", "django", "startproject", "mysite"])
    # Cambiar al directorio del proyecto Django
    os.chdir("mysite")
    print("Proyecto Django creado correctamente.")
    # os.chdir("../..") # Volvemos al directorio de trabajo original, para que no afecte al resto de funciones
  except Exception as e:
    print(f"Error al crear el proyecto Django: {str(e)}")


def configurar_proyecto():
  # Esta función se ejecutará después de crear proyecto, por lo que ya estaremos dentro del directorio indicado.
  try:
    # Configurar el proyecto Django
    print("Configurando proyecto Django...")
    os.chdir("./django_test/mysite/mysite")  # Cambiar al directorio del proyecto Django

    # 1. Crear y rellenar models.py
    with open("models.py", "w") as f:
      f.write("# Aquí va el código de los modelos")
      print("models creado correctamente.")

    # 2. Crear y rellenar forms.py
    with open("forms.py", "w") as f:
      f.write("# Aquí va el código de los formularios")

    # 3. Crear y rellenar views.py
    with open("views.py", "w") as f:
      f.write("# Aquí va el código de las vistas")

    # 4. Crear /templates y moverse dentro del directorio
    os.makedirs("templates", exist_ok=True)
    os.chdir("templates")

    # 5. Crear dentro de /templates un archivo mi_template.html, rellenarlo y salir de /templates
    with open("mi_template.html", "w") as f:
      f.write("<!-- Aquí va el código HTML -->")

    os.chdir("..")  # Salir de /templates

    # 6. Modificar urls.py


    # 7. Modificar settings.py, añadir 'mysite' a INSTALLED_APPS


    # 8. Aplicar migraciones


      # 8.1 python manage.py makemigrations mysite
    

      # 8.2 python manage.py migrate
    

    # 9. Crear superusuario (opcional)



  except Exception as e:
    print(f"Error al configurar el proyecto Django: {str(e)}")






def borrar_proyecto():
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


