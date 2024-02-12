from funciones import mi_switch

tiposGenericos = ["text", "number", "multipleChoice", "dropdown", "checkbox"]
tiposEspecificos = ["email", "dni", "phoneNumber", "date", "specialField"]

miDiccionario = {}


def menu_principal():
  print("0. Salir")
  print("1. Configurar proyecto Django")
  print("2. Lectura de fichero JSON")
  print("3. Borrar proyecto Django")
  print("\nNOTA: Si no se ha configurado el proyecto Django, no se podrá leer el fichero JSON.\n")
  # Controlamos input, seguimos pidiendo hasta que se introduzca un número válido
  while True:
    try:
      opcion = int(input("Introduce una opción: "))
      if opcion >= 0 and opcion <= 3:
        return opcion
      else:
        print("Introduce una opción válida")
    except ValueError:
      print("Introduce una opción válida")




opcion = menu_principal()
mi_switch(opcion)