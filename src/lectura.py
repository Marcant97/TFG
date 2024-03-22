# En este fichero se aloja la lógica encargada de leer el fichero JSON de entrada y comprobar que es correcto.

import json

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



def comprobarDiccionario(miDiccionario, tiposGenericos, tiposEspecificos):
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
  for pregunta in miDiccionario:

    #* COMPROBACIONES INICIALES
    print('\n')
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
        
    #? Campo de opcion múltiple --> todavía no sé si lo haré
    # elif pregunta["tipo"] == "opcionMultiple":
    #   # Procesar campos de la pregunta
    #   opcionMultiple = pregunta.get('opcionMultiple', None)
    #   # Comprobamos que opcionMultiple sea true o false
    #   if opcionMultiple != None and type(opcionMultiple) != bool:
    #     print("opcionMultiple debe ser un booleano")
    #     return -1
    #   TrueAnswerFound = False
    #   # Comprobamos que hay un campo opciones 
    #   if 'opciones' not in pregunta:
    #     print("Falta el campo opciones")
    #     return -1
    #   for campo in pregunta:
    #     if campo == "tipo" or campo == "titulo" or campo == 'opcionMultiple':
    #       print(f"Campo {campo} procesado")
    #     elif campo == 'opciones':
    #       print (f"Campo {campo} procesado")
    #       for opcion in pregunta['opciones']:
    #         if 'opcion' not in opcion or 'answer' not in opcion:
    #           print("Falta opcion o answer en un campo de opciones")
    #           return -1
    #         if opcionMultiple == False:
    #           if opcion['answer'] == True and TrueAnswerFound == False:
    #             TrueAnswerFound = True
    #           elif opcion['answer'] == True and TrueAnswerFound == True: 
    #             print("Solo puede haber una respuesta correcta, ya que opcionMultiple está a False")
    #             return -1
              
    #     else:
    #       print(f"Campo {campo} no válido")
    #       return -1
    
    
    #? Campo desplegable
    elif pregunta["tipo"] == "desplegable":
      for campo in pregunta:
        if campo == "tipo" or campo == "titulo" or campo == 'opciones':
          print(f"Campo {campo} procesado")
        else:
          print(f"Campo {campo} no válido")
          return -1
        
    #? Campo casilla
    elif pregunta["tipo"] == "casilla":
      for campo in pregunta:
        if campo == "tipo" or campo == "titulo" or campo == 'obligatorio':
          print(f"Campo {campo} procesado")
        else:
          print(f"Campo {campo} no válido")
          return -1
        


    elif pregunta["tipo"] in tiposEspecificos:
      print(f"Procesando campo de tipo específico {pregunta['tipo']}")

      # ! PENDIENTE DE HACER
        
    
    else:
      print(f"Tipo de campo no válido para la pregunta: {pregunta['titulo']}")
      return -1

  return 0
  
