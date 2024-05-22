# En este fichero se aloja la lógica encargada de leer el fichero JSON de entrada y comprobar que es correcto.

import json
import re

def validar_fecha(fecha):
    """
    Función que se encarga de validar el formato de las fechas del diccionario.
    """
    # Expresión regular para el formato dd/mm/aaaa ó dd-mm-aaaa (también admite para día y fecha sólo un dígito).
    patron = r"^(3[01]|[12][0-9]|0?[1-9])(\/|-)(0?[1-9]|1[0-2])\2(\d{4})$" ## admite guiones y barras
    
    # Verificar si la cadena cumple con el patrón
    if re.match(patron, fecha):
        return True
    else:
        return False


def leerFichero(fichero):
  """
  Función encargada de leer el fichero y pasarlo a diccionario.
  Además, comprueba que el json está correctamente construido.
  Args:
    fichero (str): ruta del fichero a leer
    
  Returns:
    dict: diccionario con los datos del fichero
  """

  # manejo de errores en la lectura del fichero
  try :
    mi_fichero = open(fichero, "r", encoding="utf-8")

    datos_fichero = json.load(mi_fichero)

    # Verificar si el JSON está vacío (lista vacía)
    if isinstance(datos_fichero, list) and not datos_fichero:
      raise ValueError("El JSON está vacío")
    
    return datos_fichero

  except FileNotFoundError:
    raise Exception("El fichero no existe")
  except PermissionError:
    raise Exception("No tienes permisos para leer el fichero")
  except json.JSONDecodeError:
    raise Exception("El contenido no es un JSON válido")
  except Exception as e:
    raise Exception(f"Error al leer el fichero: {str(e)}")


def comprobarDiccionario(miDiccionario):
  """
  Función encargada de comprobar que el diccionario pasado cumple con los requisitos
  Args:
    miDiccionario (dict): diccionario con los datos
  """

  print("Comprobando diccionario")
  try:
    for pregunta in miDiccionario:

      #* COMPROBACIONES INICIALES
      if "titulo" not in pregunta:
        raise Exception("Falta el título de la pregunta")
      if "tipo" not in pregunta:
        raise Exception("Falta el tipo de la pregunta")

      #? Campo de texto
      if pregunta["tipo"] == "texto":
        # Procesar campos de la pregunta
        for campo in pregunta:
          if campo == "tipo" or campo == "titulo" or campo == 'limite':
            # print(f"Campo {campo} procesado")
            continue
          else:
            # print(f"Campo {campo} no válido")
            raise Exception(f"Campo {campo} no válido")
          
      #? Campo numérico
      elif pregunta["tipo"] == "numero":
        # Procesar campos de la pregunta
        for campo in pregunta:
          if campo == "tipo" or campo == "titulo":
            # print(f"Campo {campo} procesado")
            continue
          # Comprobamos que valorMinimo y valorMaximo sean enteros
          elif campo == 'valorMinimo' or campo == 'valorMaximo':
            if type(pregunta[campo]) != int:
              # print(f"El campo {campo} debe ser un entero")
              raise Exception(f"El campo {campo} debe ser un entero")
          else:
            # print(f"Campo {campo} no válido")
            raise Exception(f"Campo {campo} no válido")
      
      
      #? Campo desplegable
      elif pregunta["tipo"] == "desplegable":
        opciones = False
        for campo in pregunta:
          if campo == "tipo" or campo == "titulo":
            # print(f"Campo {campo} procesado")
            continue

          elif campo == 'opciones': # se revisa que esté el campo de opciones (obligatorio)
            opciones = True
            # comprobamos que se trate de una lista
            if not isinstance(pregunta[campo], list):
              # print(f"El campo {campo} debe ser una lista")
              raise Exception(f"El campo {campo} debe ser una lista")

            # comprobamos que todos los elementos de la lista sean strings
            if not all(isinstance(item, str) for item in pregunta[campo]):
              # print(f"El campo {campo} debe ser una lista de strings")
              raise Exception(f"El campo {campo} debe ser una lista de strings")
            # print(f"Campo {campo} procesado")
          else:
            # print(f"Campo {campo} no válido")
            raise Exception(f"Campo {campo} no válido")
        if not opciones:
          # print("Falta el campo opciones, obligatorio para el tipo desplegable")
          raise Exception("Falta el campo opciones, obligatorio para el tipo desplegable")
        
          
      #? Campo casilla de verificación
      # el campo 'obligatorio' es opcional, si no se especifica se considera False
      elif pregunta["tipo"] == "casilla":
        opciones = False
        for campo in pregunta:
          if campo == "tipo" or campo == "titulo":
            # print(f"Campo {campo} procesado")
            continue
          elif campo == 'obligatorio':
            # comprobamos que se trate de un boolean
            if type(pregunta[campo]) != bool:
              # print(f"El campo {campo} debe ser un booleano")
              raise Exception(f"El campo {campo} debe ser un booleano")
            
            if pregunta[campo] == True:
              # si es obligatoria, le añadimos un asterisco para indicar que es obligatoria al usuario.
              pregunta["titulo"] += " *"

            # print(f"Campo {campo} procesado")
          else:
            # print(f"Campo {campo} no válido")
            raise Exception(f"Campo {campo} no válido")
          

      #? campo casilla de selección
      elif pregunta["tipo"] == "casillaSeleccion":
        for campo in pregunta:
          if campo == "tipo" or campo == "titulo":
            # print(f"Campo {campo} procesado")
            continue
          elif campo == 'opciones':
            opciones = True
            # comprobamos que se trate de una lista
            if not isinstance(pregunta[campo], list):
              # print(f"El campo {campo} debe ser una lista")
              raise Exception(f"El campo {campo} debe ser una lista")

            # comprobamos que todos los elementos de la lista sean strings
            if not all(isinstance(item, str) for item in pregunta[campo]):
              # print(f"El campo {campo} debe ser una lista de strings")
              raise Exception(f"El campo {campo} debe ser una lista de strings")
            # print(f"Campo {campo} procesado")
          else:
            # print(f"Campo {campo} no válido")
            raise Exception(f"Campo {campo} no válido")
          
        if not opciones:
          # print("Falta el campo opciones, obligatorio para el tipo casillas de selección")
          raise Exception("Falta el campo opciones, obligatorio para el tipo casillas de selección")


      #? campo email
      # el campo 'dominiosDisponibles' es opcional, si no se especifica se consideran todos los dominios de correo que cumplan con la expresión regular 
      elif pregunta["tipo"] == "email":
        for campo in pregunta:
          if campo == "tipo" or campo == "titulo" or campo == 'dominiosDisponibles':
            if campo == 'dominiosDisponibles':
              # comprobamos que se trate de una lista
              if not isinstance(pregunta[campo], list):
                # print(f"El campo {campo} debe ser una lista")
                raise Exception(f"El campo {campo} debe ser una lista")

              # comprobamos que todos los elementos de la lista sean strings
              if not all(isinstance(item, str) for item in pregunta[campo]):
                # print(f"El campo {campo} debe ser una lista de strings")
                raise Exception(f"El campo {campo} debe ser una lista de strings")
              
            # print(f"Campo {campo} procesado")

          else:
            # print(f"Campo {campo} no válido")
            raise Exception(f"Campo {campo} no válido")


      #? teléfono y dni
      elif pregunta["tipo"] == "telefono" or pregunta["tipo"] == "dni":
        for campo in pregunta:
          if campo == "tipo" or campo == "titulo":
            # print(f"Campo {campo} procesado")
            continue
          else:
            # print(f"Campo {campo} no válido")
            raise Exception(f"Campo {campo} no válido")
          

      #? campo fecha
      elif pregunta["tipo"] == "fecha":
        for campo in pregunta:
          if campo == "tipo" or campo == "titulo":
            # print(f"Campo {campo} procesado")
            continue

          elif campo == 'primeraFecha' or campo == 'ultimaFecha':
            # comprobamos que se trate de un string y con formato dd/mm/aaaa
            if type(pregunta[campo]) != str:
              # print(f"El campo {campo} debe ser una string")
              raise Exception(f"El campo {campo} debe ser una string")
            if not validar_fecha(pregunta[campo]):
              # print(f"El campo {campo} debe tener el formato dd/mm/aaaa")
              raise Exception(f"El campo {campo} debe tener el formato dd/mm/aaaa")
            # print(f"Campo {campo} procesado")
          else:
            # print(f"Campo {campo} no válido")
            raise Exception(f"Campo {campo} no válido")

      #? campo especial
      elif pregunta["tipo"] == "campoEspecial":
        expresionRegular = False
        for campo in pregunta:
          if campo == "tipo" or campo == "titulo":
            # print(f"Campo {campo} procesado")
            continue
          elif campo == 'expresionRegular':
            expresionRegular = True
            # comprobamos que se trate de un string
            if type(pregunta[campo]) != str:
              # print(f"El campo {campo} debe ser una string")
              raise Exception(f"El campo {campo} debe ser una string")
            
            # print(f"Campo {campo} procesado")
          else:
            # print(f"Campo {campo} no válido")
            raise Exception(f"Campo {campo} no válido")

        if not expresionRegular:
          # print("Falta el campo expresionRegular, obligatorio para el tipo campoEspecial")
          raise Exception("Falta el campo expresionRegular, obligatorio para el tipo campoEspecial")
      
      else:
        # print(f"Tipo de campo no válido para la pregunta: {pregunta['titulo']}")
        raise Exception(f"Tipo de campo no válido para la pregunta: {pregunta['titulo']}")
  
  except Exception as e:
    raise Exception(f"Error en la comprobación del diccionario: {str(e)}")
  
