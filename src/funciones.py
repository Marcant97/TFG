from lectura import leerFichero
from configurador import crear_proyecto, instalar_django, borrar_proyecto


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
  elif opcion == 2:
    # leer el fichero
    print("Lectura de fichero")
  elif opcion == 3:
    # utilizar las funciones del configurador.py para borrar el proyecto
    print("Borrar proyecto django")
  elif opcion == 4:
    print("modo desarrollo")
    # leer fichero
    fichero = "./examples/prueba1.json"
    miDiccionario = leerFichero(fichero, tiposGenericos, tiposEspecificos)
    print("imprimiendo diccionario:")
    print(miDiccionario)
    # crear proyecto
    crear_proyecto()
    # borrar proyecto
    borrar_proyecto()









