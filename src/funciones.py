from lectura import leerFichero, comprobarDiccionario
from configurador import crear_proyecto, verificar_django,  configurar_proyecto
from generadores import generar_variables

tiposGenericos = ["texto", "numero", "opcionMultiple", "desplegable", "casilla"]
tiposEspecificos = ["email", "dni", "telefono", "fecha", "campoEspecial"]
miDiccionario = {}


def funcion_principal(archivo_seleccionado):
  """
  Función encargada de manejar el flujo principal del programa.
  """
  try:
    # 1. Comprobar instalación de django
    verificar_django()

    # 2. Leer fichero de entrada y guardar el diccionario obtenido.
    # Primero se lleva a cabo la lectura del fichero porque al crear el proyecto se cambia la ruta.
    miDiccionario = leerFichero(archivo_seleccionado)

    # 3. Comprobar diccionario
    comprobarDiccionario(miDiccionario)

    # 4. Generar variables para cada pregunta.
    generar_variables(miDiccionario)

    # 5.Crear proyecto
    nombre_proyecto = crear_proyecto()

    # 6. Configurar proyecto
    configurar_proyecto(miDiccionario, nombre_proyecto)
  
  except Exception as e:
    print(f"Error: {str(e)}")
    raise # seguimos propagando el error para mostrar en la interfaz
    


