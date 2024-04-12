# En este fichero se aloja la lógica encargada de leer el fichero JSON de entrada y comprobar que es correcto.

import json
import re

def validar_fecha(fecha):
    # Expresión regular para el formato dd/mm/aaaa
    patron = r"^(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/(\d{4})$"
    # Verificar si la cadena cumple con el patrón
    if re.match(patron, fecha):
        return True
    else:
        return False


def verificarJSON(contenido):
  """
  Función que verifica si el contenido pasado es un JSON válido
  Parámetros:
    contenido: 
  """
  try:
    json.loads(contenido)
    return True
  except json.JSONDecodeError:
    return False


#! pendiente de hacer un cambio
def leerFichero(fichero, tiposGenericos, tiposEspecificos):
  """
  Función encargada de leer el fichero, pasarlo a diccionario y verificar que los tipos son correctos
  Args:
    fichero (str): ruta del fichero a leer
    tiposGenericos (list): lista con los tipos genéricos
    tiposEspecificos (list): lista con los tipos específicos
  Returns:
    dict: diccionario con los datos del fichero
  """

  #! PENDIENTE DE HACER --> llamar a verificar json

  # manejo de errores en la lectura del fichero
  try :
    mi_fichero = open(fichero, "r", encoding="utf-8")
    datos_fichero = json.load(mi_fichero)
    for campo in datos_fichero:
      if ((campo["tipo"] not in tiposGenericos) and (campo["tipo"] not in tiposEspecificos)):
        print(f"Tipo incorrecto para '{campo['tipo']}'")
      else:
        print(f"Tipo correcto para '{campo['tipo']}'")

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



def comprobarDiccionario(miDiccionario):
  """
  Función encargada de comprobar que el diccionario pasado cumple con los requisitos
  Args:
    miDiccionario (dict): diccionario con los datos
    tiposGenericos (list): lista con los tipos genéricos
    tiposEspecificos (list): lista con los tipos específicos
  Returns:
    int: 0 si todo es correcto, -1 si hay algún error
  """

  print("Comprobando diccionario")
  print(miDiccionario)
  print('\n')
  for pregunta in miDiccionario:

    #* COMPROBACIONES INICIALES
    if "titulo" not in pregunta:
      print("Falta el título de la pregunta")
      return -1
    if "tipo" not in pregunta:
      print("Falta el tipo de la pregunta")
      return -1

    #? Campo de texto
    if pregunta["tipo"] == "texto":
      # Procesar campos de la pregunta
      for campo in pregunta:
        if campo == "tipo" or campo == "titulo" or campo == 'limite':
          print(f"Campo {campo} procesado")
        else:
          print(f"Campo {campo} no válido")
          return -1
        
    #? Campo numérico
    elif pregunta["tipo"] == "numero":
      # Procesar campos de la pregunta
      for campo in pregunta:
        if campo == "tipo" or campo == "titulo":
          print(f"Campo {campo} procesado")
        # Comprobamos que valorMinimo y valorMaximo sean enteros
        elif campo == 'valorMinimo' or campo == 'valorMaximo':
          if type(pregunta[campo]) != int:
            print(f"El campo {campo} debe ser un entero")
            return -1
        else:
          print(f"Campo {campo} no válido")
          return -1
    
    
    #? Campo desplegable
    elif pregunta["tipo"] == "desplegable":
      opciones = False
      for campo in pregunta:
        if campo == "tipo" or campo == "titulo":
          print(f"Campo {campo} procesado")

        elif campo == 'opciones': # se revisa que esté el campo de opciones (obligatorio)
          opciones = True
          # comprobamos que se trate de un array
          if type(pregunta[campo]) != list:
            print(f"El campo {campo} debe ser un array")
            return -1
        else:
          print(f"Campo {campo} no válido")
          return -1
      if not opciones:
        print("Falta el campo opciones, obligatorio para el tipo desplegable")
        return -1
      
        
    #? Campo casilla
    # el campo 'obligatorio' es opcional, si no se especifica se considera False
    elif pregunta["tipo"] == "casilla":
      for campo in pregunta:
        if campo == "tipo" or campo == "titulo" or campo == 'obligatorio':
          print(f"Campo {campo} procesado")
        else:
          print(f"Campo {campo} no válido")
          return -1
        

    #? campo email
    # el campo 'dominiosDisponibles' es opcional, si no se especifica se consideran todos los dominios de correo que cumplan con la expresión regular 
    elif pregunta["tipo"] == "email":
      for campo in pregunta:
        if campo == "tipo" or campo == "titulo" or campo == 'dominiosDisponibles':
          if campo == 'dominiosDisponibles':
            # comprobamos que se trate de un array
            if type(pregunta[campo]) != list:
              print(f"El campo {campo} debe ser un array")
              return -1
          print(f"Campo {campo} procesado")
        else:
          print(f"Campo {campo} no válido")
          return -1


    #? teléfono y dni
    elif pregunta["tipo"] == "telefono" or pregunta["tipo"] == "dni":
      for campo in pregunta:
        if campo == "tipo" or campo == "titulo":
          print(f"Campo {campo} procesado")
        else:
          print(f"Campo {campo} no válido")
          return -1
        

    #? campo fecha
    elif pregunta["tipo"] == "fecha":
      for campo in pregunta:
        if campo == "tipo" or campo == "titulo":
          print(f"Campo {campo} procesado")
        elif campo == 'primeraFecha' or campo == 'ultimaFecha':
          # comprobamos que se trate de un string y con formato dd/mm/aaaa
          if type(pregunta[campo]) != str:
            print(f"El campo {campo} debe ser una string")
            return -1
          if not validar_fecha(pregunta[campo]):
            print(f"El campo {campo} debe tener el formato dd/mm/aaaa")
            return -1
        else:
          print(f"Campo {campo} no válido")
          return -1

    #? campo especial
    elif pregunta["tipo"] == "campoEspecial":
      expresionRegular = False
      for campo in pregunta:
        if campo == "tipo" or campo == "titulo":
          print(f"Campo {campo} procesado")
        elif campo == 'expresionRegular':
          expresionRegular = True
          # comprobamos que se trate de un string
          if type(pregunta[campo]) != str:
            print(f"El campo {campo} debe ser una string")
            return -1
        else:
          print(f"Campo {campo} no válido")
          return -1
        
    
    else:
      print(f"Tipo de campo no válido para la pregunta: {pregunta['titulo']}")
      return -1

  return 0
  
