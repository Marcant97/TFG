import tkinter as tk
from tkinter import filedialog
from interfazFormulario import crear_interfaz_generador_formularios
from funciones import funcion_principal

def crear_interfaz():
    root.destroy()
    crear_interfaz_generador_formularios()

def generando_formulario(archivo_seleccionado):
    # destruir los elementos de la interfaz principal
    for widget in root.winfo_children():
        widget.destroy()

    # insertar los nuevos elementos
    # Añadir un título
    label = tk.Label(root, text="Generando formulario...", bg="white", font=("Arial", 14))
    label.pack(pady=10)

    # Añadir un mensaje
    label = tk.Label(root, text="Por favor, espere unos segundos", bg="white", font=("Arial", 12))
    label.pack(pady=10)

    # esperar 2 segundos
    root.after(2000, lambda: funcion_principal(archivo_seleccionado))




def seleccionar_archivo():
    archivo_seleccionado = filedialog.askopenfilename()
    if archivo_seleccionado:
        generando_formulario(archivo_seleccionado)

def insertar_json():
    # destruir los elementos de la interfaz principal
    for widget in root.winfo_children():
        widget.destroy()

    # insertar los nuevos elementos
    # Añadir un título
    label = tk.Label(root, text="Selecciona un fichero en formato JSON con tu formulario", bg="white", font=("Arial", 14))
    label.pack(pady=10)

    # Crear un botón para seleccionar el archivo
    boton_seleccionar = tk.Button(root, text="Insertar fichero", command=seleccionar_archivo, bg="green", fg="white", font=("Arial", 12))
    boton_seleccionar.pack(pady=20)
    

root = tk.Tk()
root.title("Interfaz Principal")
root.geometry("500x200")
root.configure(bg="white")

# Añadir un título
label = tk.Label(root, text="Bienvenido al generador de formularios", bg="white", font=("Arial", 20))
label.pack(pady=10)

boton_crear_formulario = tk.Button(root, text="Crear Formulario", bg="green", fg="white", font=("Arial", 12), command=crear_interfaz)
boton_crear_formulario.pack(side="top", padx=10, pady=10)

boton_insertar_json = tk.Button(root, text="Insertar JSON", bg="green", fg="white", font=("Arial", 12), command=insertar_json)
boton_insertar_json.pack(side="top", padx=10, pady=10)

# Evitar que el usuario cambie el tamaño de la ventana
root.resizable(False, False)

# Centrar la ventana en la pantalla
root.eval('tk::PlaceWindow . center')

# Iniciar el bucle principal de la interfaz
root.mainloop()
