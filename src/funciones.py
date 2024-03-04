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


# Función que se encarga de quitar los caracteres especiales y espacios de un string, para evitar problemas 
# con el nombre de los campos de las variables.
def limpiar_titulo(titulo):
    caracteres_validos = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
    titulo_sin_acentos = ''.join(c if c in caracteres_validos else '_' for c in titulo)
    return titulo_sin_acentos.lower().rstrip('_')


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




def generar_models(miDiccionario):
  # Procesamos el diccionario
  # de momento sólo las preguntas con tipo "text"
  print('Creando modelos...')
  codigo = "from django.db import models\n\n"
  codigo += "class TuModelo(models.Model):\n"
  for pregunta in miDiccionario:
    if pregunta['type'] == 'text':
      titulo_limpio = limpiar_titulo(pregunta['title'])
      campo = f"    {titulo_limpio} = models.CharField(max_length=100)\n"
      codigo += campo

  # Escribir el código en el archivo
  with open("models.py", "w") as f:
      f.write(codigo)

# LLAMADA PARA HACER PRUEBAS
# generar_modelo(diccionario)





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


# LLAMADA PARA HACER PRUEBAS
# generar_forms(diccionario)


def generar_views():
  print('Creando vistas...')
  codigo = "from django.shortcuts import render\n"
  codigo += "from .forms import TuFormulario\n"
  codigo += "from .models import TuModelo\n\n"

  codigo += "def mi_vista(request):\n"
  codigo += "    if request.method == 'POST':\n"
  codigo += "        form = TuFormulario(request.POST)\n"
  codigo += "        if form.is_valid():\n"
  codigo += "            form.save()\n"
  codigo += "            # Realiza acciones adicionales después de guardar el formulario\n"
  codigo += "    else:\n"
  codigo += "        form = TuFormulario()\n"
  codigo += "    return render(request, 'mi_template.html', {'form': form})\n"

  # Escribir el código en el archivo
  with open("views.py", "w") as f:
      f.write(codigo)

# LLAMADA PARA HACER PRUEBAS
# generar_views(diccionario)



def generar_template():
    print('Creando template...')
    codigo = """<!-- mi_template.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Formulario</title>
</head>
<body>
    <h2>Formulario</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
"""

    # Escribir el código en el archivo
    with open("mi_template.html", "w") as f:
        f.write(codigo)

# LLAMADA PARA HACER PRUEBAS
generar_template()




# LLAMADA PARA HACER PRUEBAS
generar_templates(diccionario)