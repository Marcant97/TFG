# script python encargado de configurar el proyecto

import subprocess
import os
import shutil

# pip install -r requirements.txt
def instalar_django():
  try:
    # Instalar Django
    print("Instalando Django...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    print("Django instalado correctamente.")
  except Exception as e:
    print(f"Error al instalar Django: {str(e)}")


def crear_proyecto():
  try:
    # Crear proyecto Django
    print("Creando proyecto Django...")
    # Crear el directorio para el proyecto
    os.makedirs("django_test", exist_ok=True)
    # Cambiar al directorio del proyecto
    os.chdir("django_test")
    print("Directorio actual:", os.getcwd())
    # Iniciar el proyecto Django
    # python -m django startproject mytestsite
    subprocess.run(["python", "-m", "django", "startproject", "mysite"])
    # Cambiar al directorio del proyecto Django
    os.chdir("mysite")
    print("Proyecto Django creado correctamente.")
  except Exception as e:
    print(f"Error al crear el proyecto Django: {str(e)}")


def borrar_proyecto():
  try:
    # Obtener la ruta del directorio de trabajo actual
    directorio_actual = os.getcwd()
    print("Directorio actual:", directorio_actual)
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


