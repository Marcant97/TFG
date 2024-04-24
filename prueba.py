import tkinter as tk
from tkinter import ttk
import json

tipos_pregunta = ["texto", "numero", "desplegable", "casilla", "email", "dni", "telefono", "fecha", "campoEspecial"]


def agregar_pregunta():
    # Crear nuevos campos de entrada para una nueva pregunta
    nueva_pregunta_frame = tk.Frame(root)
    nueva_pregunta_frame.pack(fill="x", padx=5, pady=5, anchor="w")

    nueva_pregunta_label = tk.Label(nueva_pregunta_frame, text="Pregunta:")
    nueva_pregunta_label.grid(row=0, column=0, padx=5, pady=5)
    nueva_pregunta_entry = tk.Entry(nueva_pregunta_frame)
    nueva_pregunta_entry.grid(row=0, column=1, padx=5, pady=5)

    nueva_tipo_pregunta_label = tk.Label(nueva_pregunta_frame, text="Tipo de pregunta:")
    nueva_tipo_pregunta_label.grid(row=1, column=0, padx=5, pady=5)
    nueva_tipo_pregunta_combobox = ttk.Combobox(nueva_pregunta_frame, values=tipos_pregunta)
    nueva_tipo_pregunta_combobox.grid(row=1, column=1, padx=5, pady=5)

    # Guardar los widgets en la lista para acceder a ellos más tarde
    preguntas_widgets.append((nueva_pregunta_entry, nueva_tipo_pregunta_combobox))



def convertir_a_json():
    # Crear una lista para almacenar las preguntas
    preguntas = []

    # Recorrer los widgets para obtener los datos de cada pregunta
    for pregunta_entry, tipo_pregunta_combobox in preguntas_widgets:
        pregunta = pregunta_entry.get()
        tipo_pregunta = tipo_pregunta_combobox.get()
        preguntas.append({"pregunta": pregunta, "tipo_pregunta": tipo_pregunta})

    # Convertir la lista de preguntas a JSON
    datos_json = json.dumps(preguntas)

    # Mostrar el JSON en la etiqueta de resultado
    resultado_label.config(text=datos_json)


# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Formularios")
root.geometry("600x400")  # Establece el tamaño inicial de la ventana


# Botón para agregar una nueva pregunta
agregar_pregunta_button = tk.Button(root, text="Agregar pregunta", command=agregar_pregunta)
agregar_pregunta_button.pack(pady=5)

# Botón para generar el JSON
convertir_button = tk.Button(root, text="Generar JSON", command=convertir_a_json)
convertir_button.pack(pady=5)
# Crear etiquetas y campos de entrada para la pregunta inicial
preguntas_widgets = []
pregunta_frame = tk.Frame(root)
pregunta_frame.pack(fill="x", padx=5, pady=5, anchor="w")

pregunta_label = tk.Label(pregunta_frame, text="Pregunta:")
pregunta_label.grid(row=0, column=0, padx=5, pady=5)
pregunta_entry = tk.Entry(pregunta_frame)
pregunta_entry.grid(row=0, column=1, padx=5, pady=5)

tipo_pregunta_label = tk.Label(pregunta_frame, text="Tipo de pregunta:")
tipo_pregunta_label.grid(row=1, column=0, padx=5, pady=5)
tipo_pregunta_combobox = ttk.Combobox(pregunta_frame, values=tipos_pregunta)
tipo_pregunta_combobox.grid(row=1, column=1, padx=5, pady=5)

# Guardar los widgets en la lista para acceder a ellos más tarde
preguntas_widgets.append((pregunta_entry, tipo_pregunta_combobox))

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=5)

# Ejecutar el bucle principal
root.mainloop()
