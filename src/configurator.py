# script python encargado de configurar el proyecto

import subprocess
import platform
import os
import shutil

# pip install -r requirements.txt
# def instalar_django():




# def crear_proyecto():
#   # Crear proyecto Django
#   print("Creando proyecto Django...")
#   subprocess.run(["mkdir", "django_test"])
#   subprocess.run(["cd", "django_test"])
#   subprocess.run(["django-admin", "startproject", "mysite"])
#   subprocess.run(["cd", "mysite"])


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


# if __name__ == "__main__":
#   # 1. Instalar Django si no está instalado
#   instalar_django()

#   # 2. Comprobar versión de Django instalada
#   comprobar_version_django()

#   # 3. Crear proyecto Django
#   crear_proyecto()
    
borrar_proyecto()