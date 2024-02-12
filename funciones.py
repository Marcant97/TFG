from lectura import leerFichero
from configurador import crear_proyecto, instalar_django, borrar_proyecto


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





# # fichero = "./ejemplo.json"
# fichero = "";
# while fichero != "salir":
#   fichero = input("Introduce el nombre del fichero: ")
#   if fichero != "salir":
#     miDiccionario = leerFichero(fichero, tiposGenericos, tiposEspecificos)
#     print("imprimiendo diccionario:")
#     print(miDiccionario)
#   else: 
#     exit