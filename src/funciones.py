from lectura import leerFichero
from configurador import crear_proyecto, instalar_django, borrar_proyecto, configurar_proyecto
import time
import os

tiposGenericos = ["text", "number", "multipleChoice", "dropdown", "checkbox"]
tiposEspecificos = ["email", "dni", "phoneNumber", "date", "specialField"]
miDiccionario = {}


def mi_switch(opcion):
  if opcion == 0:
    # terminar la ejecución del programa
    print("salir")
  elif opcion == 1:
    # utilizar las funciones del configurador.py
    print("configurar proyecto")
    instalar_django()
    crear_proyecto()
  elif opcion == 2:
    # leer el fichero
    print("Lectura de fichero")
  elif opcion == 3:
    # utilizar las funciones del configurador.py para borrar el proyecto
    print("Borrar proyecto django")
  elif opcion == 4:
    print("modo desarrollo")
    # 1.Instalar django
    # instalar_django()
    # 2.Crear proyecto
    crear_proyecto()
    # time.sleep(1) # Esperar 1 segundo para dar tiempo a la creación del proyecto.
    # 3. Leer fichero de entrada
    # leerFichero()
    # 4. Configurar proyecto
    configurar_proyecto()


    # leer fichero
    # fichero = "./examples/prueba1.json"
    # miDiccionario = leerFichero(fichero, tiposGenericos, tiposEspecificos)
    # print("imprimiendo diccionario:")
    # print(miDiccionario)
    # crear proyecto
    # crear_proyecto()
    # borrar proyecto
    # borrar_proyecto()









