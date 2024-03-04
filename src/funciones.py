from lectura import leerFichero
# from configurador import crear_proyecto, instalar_django, borrar_proyecto, configurar_proyecto
import time
import os

tiposGenericos = ["text", "number", "multipleChoice", "dropdown", "checkbox"]
tiposEspecificos = ["email", "dni", "phoneNumber", "date", "specialField"]
miDiccionario = {}


# def mi_switch(opcion):
#   if opcion == 0:
#     # terminar la ejecución del programa
#     print("salir")
#   elif opcion == 1:
#     # utilizar las funciones del configurador.py
#     print("configurar proyecto")
#     instalar_django()
#     crear_proyecto()
#   elif opcion == 2:
#     # leer el fichero
#     print("Lectura de fichero")
#   elif opcion == 3:
#     # utilizar las funciones del configurador.py para borrar el proyecto
#     print("Borrar proyecto django")
#   elif opcion == 4:
#     print("modo desarrollo")
#     # 1.Instalar django
#     # instalar_django()
#     # 2.Crear proyecto
#     # crear_proyecto()
#     # time.sleep(1) # Esperar 1 segundo para dar tiempo a la creación del proyecto.
#     # 3. Leer fichero de entrada y guardar el diccionario obtenido.
#     miDiccionario = leerFichero("./examples/prueba1.json", tiposGenericos, tiposEspecificos)
#     print("imprimiendo diccionario:")
#     print(miDiccionario)
#     # 4. Configurar proyecto
#     # configurar_proyecto(miDiccionario)

#     # leer fichero
#     # fichero = "./examples/prueba1.json"
#     # miDiccionario = leerFichero(fichero, tiposGenericos, tiposEspecificos)
#     # print("imprimiendo diccionario:")
#     # print(miDiccionario)
#     # crear proyecto
#     # crear_proyecto()
#     # borrar proyecto
#     # borrar_proyecto()


def limpiar_titulo(titulo):
    caracteres_validos = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
    titulo_sin_acentos = ''.join(c if c in caracteres_validos else '_' for c in titulo)
    return titulo_sin_acentos.lower().rstrip('_')


def generar_modelo(miDiccionario):
  # Procesamos el diccionario
  # de momento sólo las preguntas con tipo "text"
  print('Creando modelos...')
  codigo = """from django.db import models

class TuModelo(models.Model):\n"""
  for pregunta in diccionario:
    if pregunta['type'] == 'text':
      titulo_limpio = limpiar_titulo(pregunta['title'])
      campo = f"    {titulo_limpio} = models.CharField(max_length=100)\n"
      codigo += campo
  
      
  return codigo


# Ejemplo de uso con tu diccionario
diccionario = [
    {
        "type": "text",
        "title": "Introduce tu nombre completo:"
    },
    {
        "type": "text",
        "title": "Introduce tu dirección:"
    }
]

# codigo_generado = generar_modelo(diccionario)

# with open("models.py", "w") as f:
#     f.write(codigo_generado)



def generar_forms(miDiccionario):
  print('Creando formularios...')
  with open("forms.py", "w", encoding="utf-8") as file:
    file.write("from django import forms\n\n")
    file.write("class TuFormulario(forms.Form):\n")
    for pregunta in miDiccionario:
      tipo = pregunta.get("type", "")
      titulo = pregunta.get("title", "")
      nombre_campo = limpiar_titulo(titulo)
      if tipo == "text":
        file.write(f"    {nombre_campo} = forms.CharField(label='{titulo}', max_length=100)\n")
      # elif tipo == "number":
      #   f.write(f"    {nombre_campo} = forms.IntegerField(label='{titulo}')\n")
      # Agrega más tipos de campo según sea necesario
      else:
        print(f"Tipo de campo no válido para la pregunta: {titulo}")


generar_forms(diccionario)


  

#       with open("forms.py", "w") as f:
#       f.write("""
# from django import forms
# from .models import TuModelo

# class TuFormulario(forms.ModelForm):
#     class Meta:
#         model = TuModelo
#         fields = ['campo1', 'campo2']
# """)