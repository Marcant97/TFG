import tkinter as tk
from tkinter import ttk
import json

tipos_pregunta = ["texto", "numero"]
campos_adicionales = {}  # Definir campos_adicionales como una variable global


def mostrar_campos_adicionales(tipo_seleccionado):
    # Limpiar cualquier widget anterior
    for widget in campos_adicionales_frame.winfo_children():
        widget.destroy()

    if tipo_seleccionado == "texto":
        # Campo opcional para el límite
        limite_label = tk.Label(campos_adicionales_frame, text="limite:")
        limite_label.grid(row=0, column=0, padx=5, pady=5)
        limite_entry = tk.Entry(campos_adicionales_frame)
        limite_entry.grid(row=0, column=1, padx=5, pady=5)
        campos_adicionales["limite"] = limite_entry

    elif tipo_seleccionado == "numero":
        # Campo opcional para el límite superior
        limite_superior_label = tk.Label(campos_adicionales_frame, text="limite superior:")
        limite_superior_label.grid(row=0, column=0, padx=5, pady=5)
        limite_superior_entry = tk.Entry(campos_adicionales_frame)
        limite_superior_entry.grid(row=0, column=1, padx=5, pady=5)
        campos_adicionales["limite_superior"] = limite_superior_entry

        # Campo opcional para el límite inferior
        limite_inferior_label = tk.Label(campos_adicionales_frame, text="limite inferior:")
        limite_inferior_label.grid(row=1, column=0, padx=5, pady=5)
        limite_inferior_entry = tk.Entry(campos_adicionales_frame)
        limite_inferior_entry.grid(row=1, column=1, padx=5, pady=5)
        campos_adicionales["limite_inferior"] = limite_inferior_entry

def agregar_pregunta():
    tipo_seleccionado = tipo_pregunta_combobox.get()
    pregunta = pregunta_entry.get()
    campos_adicionales = {}

    # Recoger datos de los campos adicionales según el tipo seleccionado
    if tipo_seleccionado == "texto":
        if campos_adicionales.get("limite"):
            limite = campos_adicionales["limite"].get()
            if limite:
                campos_adicionales["limite"] = limite

    elif tipo_seleccionado == "numero":
        if campos_adicionales.get("limite_superior"):
            limite_superior = campos_adicionales["limite_superior"].get()
            if limite_superior:
                campos_adicionales["limite_superior"] = limite_superior

        if campos_adicionales.get("limite_inferior"):
            limite_inferior = campos_adicionales["limite_inferior"].get()
            if limite_inferior:
                campos_adicionales["limite_inferior"] = limite_inferior

    # Agregar la pregunta con sus campos adicionales a la lista
    preguntas.append({"pregunta": pregunta, "tipo_pregunta": tipo_seleccionado, **campos_adicionales})

    # Limpiar campos de entrada
    pregunta_entry.delete(0, tk.END)
    for entry in campos_adicionales.values():
        entry.delete(0, tk.END)

def convertir_a_json():
    # Convertir la lista de preguntas a JSON
    datos_json = json.dumps(preguntas, indent=4)

    # Mostrar el JSON en la etiqueta de resultado
    resultado_label.config(text=datos_json)






#####? PROGRAMA PRINCIPAL #####

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Formularios")
root.geometry("800x600")

#Crear el contenedor para la etiqueta y el combobox
tipo_pregunta_container = tk.Frame(root)
tipo_pregunta_container.pack(padx=5, pady=5, anchor="w")
# Etiqueta para el tipo de pregunta
tipo_pregunta_label = tk.Label(tipo_pregunta_container, text="Tipo de pregunta:")
tipo_pregunta_label.grid(row=0, column=0, padx=5, pady=5)
# Combobox para seleccionar el tipo de pregunta
tipo_pregunta_combobox = ttk.Combobox(tipo_pregunta_container, values=tipos_pregunta, state="readonly")
tipo_pregunta_combobox.grid(row=0, column=1, padx=5, pady=5)


# Crear el contenedor para la etiqueta y el campo de entrada de la pregunta
pregunta_container = tk.Frame(root)
pregunta_container.pack(padx=10, pady=10, anchor="w")
# Etiqueta para la pregunta
pregunta_label = tk.Label(pregunta_container, text="Pregunta:")
pregunta_label.grid(row=0, column=0, padx=5, pady=5)
# Campo de entrada para la pregunta
pregunta_entry = tk.Entry(pregunta_container)
pregunta_entry.grid(row=0, column=1, padx=5, pady=5)


# Dependiendo del tipo de pregunta seleccionado, se mostrarán campos adicionales
tipo_pregunta_combobox.bind("<<ComboboxSelected>>", lambda event: mostrar_campos_adicionales(tipo_pregunta_combobox.get()))

# Frame para los campos adicionales dependiendo del tipo de pregunta seleccionado
campos_adicionales_frame = tk.Frame(root)
campos_adicionales_frame.pack(fill="x", padx=5, pady=5, anchor="w")

# Botón para agregar una nueva pregunta
agregar_pregunta_button = tk.Button(root, text="Agregar pregunta", command=agregar_pregunta)
agregar_pregunta_button.pack(pady=5, anchor="w")

# Botón para generar el JSON
convertir_button = tk.Button(root, text="Generar JSON", command=convertir_a_json)
convertir_button.pack(pady=5, anchor="w")

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=5, anchor="w")

# Lista para almacenar las preguntas
preguntas = []

# Ejecutar el bucle principal
root.mainloop()

