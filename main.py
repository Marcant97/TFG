from lectura import leerFichero 

tiposGenericos = ["text", "number", "multipleChoice", "dropdown", "checkbox"]
tiposEspecificos = ["email", "dni", "phoneNumber", "date", "specialField"]

miDiccionario = {}

fichero = "./ejemplo.json"

leerFichero(fichero, tiposGenericos, tiposEspecificos)

