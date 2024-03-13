from lectura import leerFichero, comprobarDiccionario
from configurador import crear_proyecto, instalar_django, borrar_proyecto, configurar_proyecto

tiposGenericos = ["text", "number", "multipleChoice", "dropdown", "checkbox"]
tiposEspecificos = ["email", "dni", "phoneNumber", "date", "specialField"]
miDiccionario = {}


def mi_switch(opcion):
  if opcion == 0:
    # terminar la ejecución del programa
    print("salir")

  elif opcion == 1:
    # utilizar las funciones del configurador.py
    print("configurar proyecto")
    instalar_django()
    crear_proyecto()

  elif opcion == 2:
    # leer el fichero
    print("Lectura de fichero")
    miDiccionario = leerFichero("./examples/prueba1.json", tiposGenericos, tiposEspecificos)
    print(miDiccionario)

  elif opcion == 3:
    # utilizar las funciones del configurador.py para borrar el proyecto
    print("Borrar proyecto django")

  elif opcion == 4:
    print("Entrando en modo desarrollo del switch")
    # 1.Instalar django
    # instalar_django()
    borrar_proyecto()
    # 3. Leer fichero de entrada y guardar el diccionario obtenido.

    # He puesto primero la lectura del fichero por que al crear el proyecto se cambia la ruta. Lo ideal es ubicarme siempre en la raíz.
    miDiccionario = leerFichero("./examples/prueba5.json", tiposGenericos, tiposEspecificos)
    comprobarDiccionario(miDiccionario)

    # 2.Crear proyecto
    crear_proyecto()

    # 4. Configurar proyecto
    configurar_proyecto(miDiccionario)


