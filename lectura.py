# En este fichero se alojará la lógica encargada de leer el fichero JSON de entrada

import json

# Función encargada de leer el fichero, pasarlo a diccionario y verificar que los tipos son correctos
def leerFichero(fichero, tiposGenericos, tiposEspecificos):
  mi_fichero = open(fichero, "r")
  datos_fichero = json.load(mi_fichero)
  for campo in datos_fichero:
    if campo["type"] in tiposGenericos:
      print("Tipo generico correcto")
    elif campo["type"] in tiposEspecificos:
      print("Tipo especifico correcto")
    else:
      print("Tipo incorrecto")
    