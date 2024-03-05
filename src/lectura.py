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





def comprobarDiccionario(miDiccionario):
  print("Comprobando diccionario")
  print(miDiccionario)
  for pregunta in miDiccionario:
    print('\n')
    if "title" not in pregunta:
      print("Falta el título de la pregunta")
      return -1
    if "type" not in pregunta:
      print("Falta el tipo de la pregunta")
      return -1

    # Campo de texto
    if pregunta["type"] == "text":
      # Procesar campos de la pregunta
      for campo in pregunta:
        if campo == "type" or campo == "title" or campo == 'limit':
          print(f"Campo {campo} procesado")
        else:
          print(f"Campo {campo} no válido")
          return -1
        
    # Campo numérico
    elif pregunta["type"] == "number":
      # Procesar campos de la pregunta
      for campo in pregunta:
        if campo == "type" or campo == "title":
          print(f"Campo {campo} procesado")
        # Comprobamos que minValue y maxValue sean enteros
        elif campo == 'minValue' or campo == 'maxValue':
          if type(pregunta[campo]) != int:
            print(f"El campo {campo} debe ser un entero")
            return -1
        else:
          print(f"Campo {campo} no válido")
          return -1
        

    elif pregunta["type"] == "multipleChoice":
      # Procesar campos de la pregunta
      multipleAnswers = pregunta.get('multipleAnswers', None)
      # Comprobamos que multipleAnswers sea true o false
      if multipleAnswers != None and type(multipleAnswers) != bool:
        print("multipleAnswers debe ser un booleano")
        return -1
      TrueAnswerFound = False
      # Comprobamos que hay un campo choices 
      if 'choices' not in pregunta:
        print("Falta el campo choices")
        return -1
      for campo in pregunta:
        if campo == "type" or campo == "title" or campo == 'multipleAnswers':
          print(f"Campo {campo} procesado")
        elif campo == 'choices':
          print (f"Campo {campo} procesado")
          for choice in pregunta['choices']:
            if 'choice' not in choice or 'answer' not in choice:
              print("Falta choice o answer en un campo de choices")
              return -1
            if multipleAnswers == False:
              if choice['answer'] == True and TrueAnswerFound == False:
                TrueAnswerFound = True
              elif choice['answer'] == True and TrueAnswerFound == True: 
                print("Solo puede haber una respuesta correcta, ya que multipleAnswers está a False")
                return -1
              
        else:
          print(f"Campo {campo} no válido")
          return -1
      

    elif pregunta["type"] == "dropdown":
      for campo in pregunta:
        if campo == "type" or campo == "title" or campo == 'choices':
          print(f"Campo {campo} procesado")
        else:
          print(f"Campo {campo} no válido")
          return -1
        
    
    elif pregunta["type"] == "checkbox":
      for campo in pregunta:
        if campo == "type" or campo == "title" or campo == 'content':
          print(f"Campo {campo} procesado")
        else:
          print(f"Campo {campo} no válido")
          return -1
        
    
    else:
      print(f"Tipo de campo no válido para la pregunta: {pregunta['title']}")
      return -1

  return 0
  
