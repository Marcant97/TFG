from lectura import leerFichero, comprobarDiccionario
from configurador import crear_proyecto, verificar_django, borrar_proyecto, configurar_proyecto

tiposGenericos = ["texto", "numero", "opcionMultiple", "desplegable", "casilla"]
tiposEspecificos = ["email", "dni", "telefono", "fecha", "campoEspecial"]
miDiccionario = {}


def mi_switch(opcion):
  if opcion == 0:
    # terminar la ejecución del programa
    print("salir")

  elif opcion == 1:
    try:
      # 1. Comprobar instalación de django
      verificar_django()
      # 2. Borrar proyecto anterior si lo hay, si se queda bloqueado abortar.
      borrar_proyecto()

      # 3. Leer fichero de entrada y guardar el diccionario obtenido.
      # He puesto primero la lectura del fichero por que al crear el proyecto se cambia la ruta. Lo ideal es ubicarme siempre en la raíz.
      miDiccionario = leerFichero("./examples/prueba5.json")

      #! me falta de aquí para abajo
      comprobarDiccionario(miDiccionario)

      # 3.Crear proyecto
      crear_proyecto()

      # 4. Configurar proyecto
      configurar_proyecto(miDiccionario)
    
    except Exception as e:
      print(f"Error: {str(e)}")
      raise


