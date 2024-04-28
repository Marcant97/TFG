import tkinter as tk

root = tk.Tk()
root.title("Interfaz Principal")
root.geometry("500x200")
root.configure(bg="white")

# Añadir un título
label = tk.Label(root, text="Bienvenido al generador de formularios", bg="white", font=("Arial", 20))
label.pack(pady=10)

boton_crear_formulario = tk.Button(root, text="Crear Formulario", bg="green", fg="white", font=("Arial", 12))
boton_crear_formulario.pack(side="top", padx=10, pady=10)

boton_insertar_json = tk.Button(root, text="Insertar JSON", bg="blue", fg="white", font=("Arial", 12))
boton_insertar_json.pack(side="top", padx=10, pady=10)

# Evitar que el usuario cambie el tamaño de la ventana
root.resizable(False, False)

# Centrar la ventana en la pantalla
root.eval('tk::PlaceWindow . center')

# Iniciar el bucle principal de la interfaz
root.mainloop()
