from lectura import leerFichero 

tiposGenericos = ["text", "number", "multipleChoice", "dropdown", "checkbox"]
tiposEspecificos = ["email", "dni", "phoneNumber", "date", "specialField"]

miDiccionario = {}

# fichero = "./ejemplo.json"
fichero = "";
while fichero != "salir":
  fichero = input("Introduce el nombre del fichero: ")
  if fichero != "salir":
    miDiccionario = leerFichero(fichero, tiposGenericos, tiposEspecificos)
    print("imprimiendo diccionario:")
    print(miDiccionario)
  else: 
    exit
