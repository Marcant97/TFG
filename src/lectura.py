# En este fichero se alojará la lógica encargada de leer el fichero JSON de entrada

import json

def verificarJSON(contenido):
  try:
    json.loads(contenido)
    return True
  except json.JSONDecodeError:
    return False


# Función encargada de leer el fichero, pasarlo a diccionario y verificar que los tipos son correctos
def leerFichero(fichero, tiposGenericos, tiposEspecificos):
  # manejo de errores en la lectura del fichero
  try :
    mi_fichero = open(fichero, "r", encoding="utf-8")
    datos_fichero = json.load(mi_fichero)
    for campo in datos_fichero:
      if ((campo["type"] not in tiposGenericos) and (campo["type"] not in tiposEspecificos)):
        print(f"Tipo incorrecto para '{campo['type']}'")
      else:
        print(f"Tipo correcto para '{campo['type']}'")

    return datos_fichero


  except FileNotFoundError:
    print("El fichero no existe")
    exit
  except PermissionError:
    print("No tienes permisos para leer el fichero")
    exit
  except json.JSONDecodeError:
    print("El fichero no es un JSON válido")
    exit
  except Exception:
    print("Error desconocido")
    exit