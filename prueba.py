import tkinter as tk
from tkinter import ttk
import json

# tipos de preguntas disponibles
tipos_pregunta = ["texto", "numero", "desplegable"]

limite_entry = None
valor_maximo_entrada = None
valor_minimo_entrada = None

def mostrar_json():
    # Convertir la lista de preguntas a JSON
    datos_json = json.dumps(preguntas, indent=4)
    json_text.delete("1.0", tk.END)  # Limpiar contenido actual
    json_text.insert(tk.END, datos_json)

def limpiar_mensaje():
    mensaje_confirmacion.config(text="", fg="black")

def mostrar_campos_adicionales(tipo_seleccionado):
    global limite_entry
    global valor_maximo_entrada
    global valor_minimo_entrada
    global opciones_entry

    limpiar_mensaje() # limpiamos mensaje de pregunta añadida correctamente.

    # Limpiar cualquier widget anterior
    for widget in campos_adicionales_frame.winfo_children():
        widget.destroy()

    if tipo_seleccionado == "texto":
        # Campo opcional para el límite
        limite_label = tk.Label(campos_adicionales_frame, text="Límite de caracteres:")
        limite_label.grid(row=0, column=0, padx=5, pady=5)
        limite_entry = tk.Entry(campos_adicionales_frame, borderwidth=2)
        limite_entry.grid(row=1, column=0, padx=5, pady=5)

        limite_label.configure(bg=root.cget('bg')) # fondo

    elif tipo_seleccionado == "numero":

        # campo opcional para el límite inferior
        valor_minimo_label = tk.Label(campos_adicionales_frame, text="Valor mínimo:")
        valor_minimo_label.grid(row=0, column=0, padx=5, pady=5)
        valor_minimo_entrada = tk.Entry(campos_adicionales_frame, borderwidth=2)
        valor_minimo_entrada.grid(row=1, column=0, padx=5, pady=5)

        valor_minimo_label.configure(bg=root.cget('bg')) # fondo

        # campo opcional para el límite superior
        valor_maximo_label = tk.Label(campos_adicionales_frame, text="Valor máximo:")
        valor_maximo_label.grid(row=0, column=1, padx=5, pady=5)
        valor_maximo_entrada = tk.Entry(campos_adicionales_frame, borderwidth=2)
        valor_maximo_entrada.grid(row=1, column=1, padx=5, pady=5)

        valor_maximo_label.configure(bg=root.cget('bg')) # fondo


    elif tipo_seleccionado == "desplegable":
        opciones_label = tk.Label(campos_adicionales_frame, text="Opciones (separadas por ;):")
        opciones_label.grid(row=0, column=0, padx=5, pady=5)
        opciones_entry = tk.Entry(campos_adicionales_frame, borderwidth=2)
        opciones_entry.grid(row=1, column=0, padx=5, pady=5)
        opciones_label.configure(bg=root.cget('bg')) # fondo

def agregar_pregunta():
    tipo_seleccionado = tipo_pregunta_combobox.get()
    pregunta = pregunta_entry.get()
    campos_adicionales = {}

    # Recoger datos de los campos adicionales según el tipo seleccionado,
    # sólo se incluyen si se han rellenado.
    if tipo_seleccionado == "texto":
        limite = limite_entry.get()
        if limite:
            campos_adicionales["limite"] = limite

    elif tipo_seleccionado == "numero":
        valor_maximo = valor_maximo_entrada.get()
        if valor_maximo:
            campos_adicionales["valorMaximo"] = int(valor_maximo)

        valor_minimo = valor_minimo_entrada.get()
        if valor_minimo:
            campos_adicionales["valorMinimo"] = int(valor_minimo)

    elif tipo_seleccionado == "desplegable":
        opciones = opciones_entry.get()
        if opciones:
            opciones = opciones.split(";")  # Obtener opciones y dividirlas por comas
            campos_adicionales["opciones"] = opciones
        else:
            mensaje_confirmacion.config(text="Debe ingresar al menos una opción para el desplegable.", fg="red")
            return  # Salir de la función sin agregar la pregunta

    # Guardar la pregunta y los campos adicionales en la lista
    preguntas.append({"tipo": tipo_seleccionado, "titulo": pregunta, **campos_adicionales})

    # Limpiar campos de entrada
    tipo_pregunta_combobox.set("")
    pregunta_entry.delete(0, tk.END)
    if tipo_seleccionado == "texto":
        limite_entry.delete(0, tk.END)
    elif tipo_seleccionado == "numero":
        valor_maximo_entrada.delete(0, tk.END)
        valor_minimo_entrada.delete(0, tk.END)
    elif tipo_seleccionado == "desplegable":
        opciones_entry.delete(0, tk.END)

    # Mostrar mensaje de confirmación
    mensaje_confirmacion.config(text="La pregunta se ha agregado correctamente.", fg="black")

    mostrar_json()  # Actualizar JSON en el área de texto




def convertir_a_json():
    limpiar_mensaje() # limpiamos mensaje de pregunta añadida correctamente.
    # Convertir la lista de preguntas a JSON
    datos_json = json.dumps(preguntas, indent=4)
    print(datos_json)
    # Mostrar el JSON en la etiqueta de resultado
    # resultado_label.config(text=datos_json)




# Se crea la ventana principal.
root = tk.Tk()
root.title("Generador de Formularios")
root.geometry("600x600")
root.configure(bg="white")

# Campo tipo
tipo_pregunta_label = tk.Label(root, text="Tipo de pregunta:*")
tipo_pregunta_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
tipo_pregunta_combobox = ttk.Combobox(root, values=tipos_pregunta, state="readonly")
tipo_pregunta_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

tipo_pregunta_label.configure(bg=root.cget('bg')) # fondo

# Campo pregunta
pregunta_label = tk.Label(root, text="Pregunta:*")
pregunta_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
pregunta_entry = tk.Entry(root, borderwidth=2)
pregunta_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
pregunta_label.configure(bg=root.cget('bg')) # fondo

# Frame para los campos adicionales
campos_adicionales_frame = tk.Frame(root, bg=root.cget('bg'))
campos_adicionales_frame.grid(row=0, column=2, rowspan=2, padx=5, pady=5, sticky="n")

# Asociar la función mostrar_campos_adicionales al evento de selección de un elemento en el Combobox
tipo_pregunta_combobox.bind("<<ComboboxSelected>>", lambda event: mostrar_campos_adicionales(tipo_pregunta_combobox.get()))

# Botón para agregar pregunta
agregar_pregunta_button = tk.Button(root, text="Agregar pregunta", command=agregar_pregunta)
agregar_pregunta_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Botón para convertir a JSON
convertir_button = tk.Button(root, text="Generar JSON", command=convertir_a_json)
convertir_button.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="e")

# Lista para almacenar las preguntas
preguntas = []

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
resultado_label.configure(bg=root.cget('bg')) # fondo

# Mostrar JSON
json_text = tk.Text(root, height=20, width=50)
json_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
root.rowconfigure(4, weight=1)  # Hacer que la fila 4 se expanda
root.columnconfigure(1, weight=1)  # Hacer que la columna 1 se expanda
mostrar_json()  # Mostrar JSON inicialmente

# Etiqueta para mostrar el mensaje de confirmación
mensaje_confirmacion = tk.Label(root, text="")
mensaje_confirmacion.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="w")
mensaje_confirmacion.configure(bg=root.cget('bg')) # fondo

# Iniciar la aplicación
root.mainloop()
