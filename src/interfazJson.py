import tkinter as tk
from tkinter import filedialog



def crear_interfaz_insertar_json():
    def seleccionar_archivo():
        archivo_seleccionado = filedialog.askopenfilename()
        if archivo_seleccionado:
            root.destroy()


    root = tk.Tk()
    root.title("Seleccionar Archivo")
    root.geometry("500x200")
    root.configure(bg="white")

    # Añadir un título
    label = tk.Label(root, text="Selecciona un fichero en formato JSON con tu formulario", bg="white", font=("Arial", 14))
    label.pack(pady=10)

    # Crear un botón para seleccionar el archivo
    boton_seleccionar = tk.Button(root, text="Insertar fichero", command=seleccionar_archivo, bg="green", fg="white", font=("Arial", 12))
    boton_seleccionar.pack(pady=20)

    # Ejecutar el bucle principal de la interfaz
    root.mainloop()

