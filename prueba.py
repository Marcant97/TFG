import tkinter as tk
from tkinter import ttk
import json

# tipos de preguntas disponibles
# tipos_pregunta = ["texto", "numero", "desplegable", "casilla", "email", "dni", "telefono", "fecha", "campoEspecial"]
tipos_pregunta = ["texto", "numero"]

limite_entry = None
limite_superior_entry = None
limite_inferior_entry = None

def mostrar_campos_adicionales(tipo_seleccionado):
    global limite_entry
    global limite_superior_entry
    global limite_inferior_entry

    # Limpiar cualquier widget anterior
    for widget in campos_adicionales_frame.winfo_children():
        widget.destroy()

    if tipo_seleccionado == "texto":
        # Campo opcional para el límite
        limite_label = tk.Label(campos_adicionales_frame, text="limite:")
        limite_label.grid(row=0, column=0, padx=5, pady=5)
        limite_entry = tk.Entry(campos_adicionales_frame)
        limite_entry.grid(row=0, column=1, padx=5, pady=5)

    elif tipo_seleccionado == "numero":
        # campo opcional para el límite superior
        limite_superior_label = tk.Label(campos_adicionales_frame, text="limite superior:")
        limite_superior_label.grid(row=0, column=0, padx=5, pady=5)
        limite_superior_entry = tk.Entry(campos_adicionales_frame)
        limite_superior_entry.grid(row=0, column=1, padx=5, pady=5)

        # campo opcional para el límite inferior
        limite_inferior_label = tk.Label(campos_adicionales_frame, text="limite inferior:")
        limite_inferior_label.grid(row=1, column=0, padx=5, pady=5)
        limite_inferior_entry = tk.Entry(campos_adicionales_frame)
        limite_inferior_entry.grid(row=1, column=1, padx=5, pady=5)



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
        limite_superior = limite_superior_entry.get()
        if limite_superior:
            campos_adicionales["limite_superior"] = limite_superior

        limite_inferior = limite_inferior_entry.get()
        if limite_inferior:
            campos_adicionales["limite_inferior"] = limite_inferior

    # Guardar la pregunta y los campos adicionales en la lista
    preguntas.append({"pregunta": pregunta, "tipo_pregunta": tipo_seleccionado, **campos_adicionales})

    # Limpiar campos de entrada
    tipo_pregunta_combobox.set("")
    pregunta_entry.delete(0, tk.END)
    if tipo_seleccionado == "texto":
        limite_entry.delete(0, tk.END)
    elif tipo_seleccionado == "numero":
        limite_superior_entry.delete(0, tk.END)
        limite_inferior_entry.delete(0, tk.END)



def convertir_a_json():
    # Convertir la lista de preguntas a JSON
    datos_json = json.dumps(preguntas, indent=4)
    print(datos_json)
    # Mostrar el JSON en la etiqueta de resultado
    resultado_label.config(text=datos_json)

######## PROGRAMA PRINCIPAL ########

root = tk.Tk()
root.title("Generador de Formularios")
root.geometry("800x600")

pregunta_label = tk.Label(root, text="Pregunta:")
pregunta_label.pack(padx=5, pady=5)
pregunta_entry = tk.Entry(root)
pregunta_entry.pack(padx=5, pady=5)

tipo_pregunta_label = tk.Label(root, text="Tipo de pregunta:")
tipo_pregunta_label.pack(padx=5, pady=5)
tipo_pregunta_combobox = ttk.Combobox(root, values=tipos_pregunta, state="readonly")
tipo_pregunta_combobox.pack(padx=5, pady=5)

campos_adicionales_frame = tk.Frame(root)
campos_adicionales_frame.pack(padx=5, pady=5, fill="x")

tipo_pregunta_combobox.bind("<<ComboboxSelected>>", lambda event: mostrar_campos_adicionales(tipo_pregunta_combobox.get()))

agregar_pregunta_button = tk.Button(root, text="Agregar pregunta", command=agregar_pregunta)
agregar_pregunta_button.pack(pady=5)

convertir_button = tk.Button(root, text="Generar JSON", command=convertir_a_json)
convertir_button.pack(pady=5)

preguntas = []

resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=5)

root.mainloop()