from lectura import leerFichero, comprobarDiccionario
from configurador import crear_proyecto, verificar_django, borrar_proyecto, configurar_proyecto
from generadores import generar_variables

tiposGenericos = ["texto", "numero", "opcionMultiple", "desplegable", "casilla"]
tiposEspecificos = ["email", "dni", "telefono", "fecha", "campoEspecial"]
miDiccionario = {}


def funcion_principal(archivo_seleccionado):

  try:
    # 1. Comprobar instalación de django
    verificar_django()

    # 2. Borrar proyecto anterior si lo hay, si se queda bloqueado abortar.
    borrar_proyecto()

    # 3. Leer fichero de entrada y guardar el diccionario obtenido.
    # He puesto primero la lectura del fichero por que al crear el proyecto se cambia la ruta. Lo ideal es ubicarme siempre en la raíz.
    miDiccionario = leerFichero(archivo_seleccionado)

    # 4. Comprobar diccionario
    comprobarDiccionario(miDiccionario)

    # 5. Generar variables para cada pregunta.
    generar_variables(miDiccionario)

    # 6.Crear proyecto
    crear_proyecto()

    # 7. Configurar proyecto
    configurar_proyecto(miDiccionario)
  
  except Exception as e:
    print(f"Error: {str(e)}")
    raise


