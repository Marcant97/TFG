# En este fichero se alojará la lógica encargada de leer el fichero JSON de entrada

import json


tiposGenericos = ["text", "number", "multipleChoice", "dropdown", "checkbox"]
tiposEspecificos = ["email", "dni", "phoneNumber", "date", "specialField"]

miDiccionario = {}
mi_fichero = open("./ejemplo.json", "r")

# Función encargada de leer el fichero
def leerFichero():
  datos_fichero = json.load(mi_fichero)
  for campo in datos_fichero:
    if campo["type"] == "text":
      print("text encontrado")
    


leerFichero()

# Función encaragda de verificar que los tipos son correctos


# Función encargada de verificar que los campos son correctos