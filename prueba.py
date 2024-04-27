import tkinter as tk
from tkinter import ttk
import json

# tipos de preguntas disponibles
# tipos_pregunta = ["texto", "numero", "desplegable", "casilla", "email", "dni", "telefono", "fecha", "campoEspecial"]
tipos_pregunta = ["texto", "numero"]

limite_entry = None
valor_maximo_entrada = None
valor_minimo_entrada = None



def mostrar_campos_adicionales(tipo_seleccionado):
    global limite_entry
    global valor_maximo_entrada
    global valor_minimo_entrada

    # Limpiar cualquier widget anterior
    for widget in campos_adicionales_frame.winfo_children():
        widget.destroy()

    if tipo_seleccionado == "texto":
        # Campo opcional para el límite
        limite_label = tk.Label(campos_adicionales_frame, text="Límite de caracteres:")
        limite_label.grid(row=0, column=0, padx=5, pady=5)
        limite_entry = tk.Entry(campos_adicionales_frame)
        limite_entry.grid(row=0, column=1, padx=5, pady=5)

        limite_label.configure(bg=root.cget('bg')) # fondo

    elif tipo_seleccionado == "numero":

        # campo opcional para el límite inferior
        valor_minimo_label = tk.Label(campos_adicionales_frame, text="Valor mínimo:")
        valor_minimo_label.grid(row=1, column=0, padx=5, pady=5)
        valor_minimo_entrada = tk.Entry(campos_adicionales_frame)
        valor_minimo_entrada.grid(row=1, column=1, padx=5, pady=5)

        valor_minimo_label.configure(bg=root.cget('bg')) # fondo

        # campo opcional para el límite superior
        valor_maximo_label = tk.Label(campos_adicionales_frame, text="Valor máximo:")
        valor_maximo_label.grid(row=0, column=0, padx=5, pady=5)
        valor_maximo_entrada = tk.Entry(campos_adicionales_frame)
        valor_maximo_entrada.grid(row=0, column=1, padx=5, pady=5)

        valor_maximo_label.configure(bg=root.cget('bg')) # fondo





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
            campos_adicionales["valorMinimo"] = int(valor_maximo)

        valor_minimo = valor_minimo_entrada.get()
        if valor_minimo:
            campos_adicionales["valorMaximo"] = int(valor_minimo)

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




def convertir_a_json():
    # Convertir la lista de preguntas a JSON
    datos_json = json.dumps(preguntas, indent=4)
    print(datos_json)
    # Mostrar el JSON en la etiqueta de resultado
    resultado_label.config(text=datos_json)




#?#######################################################################
########?################# PROGRAMA PRINCIPAL ###########################
#?#######################################################################




# Se crea la ventana principal.
root = tk.Tk()
root.title("Generador de Formularios")
root.geometry("800x600")
root.configure(bg="white")


# campo tipo
tipo_pregunta_label = tk.Label(root, text="Tipo de pregunta:*")
tipo_pregunta_label.pack(padx=5, pady=5)
tipo_pregunta_combobox = ttk.Combobox(root, values=tipos_pregunta, state="readonly")
tipo_pregunta_combobox.pack(padx=5, pady=5)

tipo_pregunta_label.configure(bg=root.cget('bg')) # fondo

# campo pregunta
pregunta_label = tk.Label(root, text="Pregunta:*")
pregunta_label.pack(padx=5, pady=5)
pregunta_entry = tk.Entry(root)
pregunta_entry.pack(padx=5, pady=5)

pregunta_label.configure(bg=root.cget('bg')) # fondo


# Frame para los campos adicionales
campos_adicionales_frame = tk.Frame(root)
campos_adicionales_frame = tk.Frame(root, bg=root.cget('bg')) # fondo
campos_adicionales_frame.pack(padx=5, pady=5, fill="x")

# Asociar la función mostrar_campos_adicionales al evento de selección de un elemento en el Combobox
tipo_pregunta_combobox.bind("<<ComboboxSelected>>", lambda event: mostrar_campos_adicionales(tipo_pregunta_combobox.get()))

# Botón para agregar pregunta
agregar_pregunta_button = tk.Button(root, text="Agregar pregunta", command=agregar_pregunta)
agregar_pregunta_button.pack(pady=5)

# Botón para convertir a JSON
convertir_button = tk.Button(root, text="Generar JSON", command=convertir_a_json)
convertir_button.pack(pady=5)

# Lista para almacenar las preguntas
preguntas = []

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=5)
resultado_label.configure(bg=root.cget('bg')) # fondo

# Iniciar la aplicación
root.mainloop()