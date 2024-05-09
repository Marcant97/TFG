import tkinter as tk
from tkinter import ttk
import json
import re
import os
import time

from funciones import funcion_principal

# tipos de preguntas disponibles
tipos_pregunta = ["texto", "numero", "desplegable", "casilla de verificación", "correo electrónico", "DNI", "teléfono", "fecha", "campo especial"]

limite_entry = None
valor_maximo_entrada = None
valor_minimo_entrada = None
opciones_entry = None
obligatorio_entry = None
correo_entry = None
dominios_entry = None
primera_fecha_entry = None
ultima_fecha_entry = None
expresion_regular_entry = None




#########? FUNCIÓN PRINCIPAL ##########
 
def crear_interfaz_generador_formularios():

    def directorio_ejemplos():
        """
        Verifica si el directorio existe y lo crea si no existe.
        """
        directorio = "./ejemplos"
        if not os.path.exists(directorio):
            os.makedirs(directorio)


    def obtener_siguiente_numero():
        """
        Obtiene el siguiente número de formulario disponible.
        Esta función se utiliza para la generación de nombres de ficheros.
        """
        numero = 1
        while True:
            nombre_fichero = f"formulario{numero}.json"
            if not os.path.exists(nombre_fichero):
                return numero
            numero += 1

    def crear_formulario():
        root.destroy() # se destruye la ventana principal.
        
        # se crea una nueva ventana.
        root2 = tk.Tk()
        root2.title("Interfaz Principal")
        root2.geometry("500x200")
        root2.configure(bg="white")

        # Añadir un título
        label = tk.Label(root2, text="Generando formulario...", bg="white", font=("Arial", 14))
        label.pack(pady=10)

        # Añadir un mensaje
        label = tk.Label(root2, text="Por favor, espere unos segundos", bg="white", font=("Arial", 12))
        label.pack(pady=10)

        # forzamos la actualización de la interfaz gráfica antes de continuar.
        root2.update()

        try:
            # Convertir la lista de preguntas a JSON
            datos_json = json.dumps(preguntas, indent=4, ensure_ascii=False)
            print(datos_json)
            # Crear el directorio de ejemplos si no existe
            directorio_ejemplos()

            # entrar al directorio
            os.chdir("./ejemplos")

            # Obtener el siguiente número de formulario disponible
            numero_formulario = obtener_siguiente_numero()

            # Crear el nombre del formulario
            nombre_formulario = f"formulario{numero_formulario}.json"

            # Generar el fichero y guardarlo en la carpeta actual
            with open(nombre_formulario, "w", encoding="utf-8") as f:
                f.write(datos_json)

            # Obtener la ruta completa del fichero
            ruta_fichero = os.path.abspath(nombre_formulario)

            # Volver al directorio raíz
            os.chdir("..")

            # Llamar a la función principal, aquí comienza el programa principal por el flujo de "crear formulario".
            funcion_principal(ruta_fichero)
        
        except Exception as e:
            # borrar el contenido de la ventana
            for widget in root2.winfo_children():
                widget.destroy()

            print(e)
            # Mostrar mensaje de error
            label = tk.Label(root2, text="Ha ocurrido un error al generar el formulario.", bg="white", font=("Arial", 16), fg="red")
            label.pack(pady=10)

            # Mostrar el error
            label = tk.Label(root2, text=str(e), bg="white", font=("Arial", 12), fg="black", wraplength=400)
            label.pack(pady=10)

            # Actualizar la ventana
            root2.update()

    # Función para validar la expresión regular
    def validar_expresion_regular(expresion):
        """
        Función encargada de validar que la expresión regular es válida.
        """
        try:
            re.compile(expresion)
            return True
        except re.error:
            return False

    def validar_fecha(fecha):
        """
        Función encaragda de validar que el formato de las fechas es correcto.
        """
        # Expresión regular para el formato dd/mm/yyyy
        patron = r"^(3[01]|[12][0-9]|0?[1-9])(\/|-)(0?[1-9]|1[0-2])\2(\d{4})$" ## admite guiones y barras
        return re.match(patron, fecha) is not None

    def mostrar_json():
        """
        Función encargada de mostrar el JSON en el área de texto.
        """
        # Convertir la lista de preguntas a JSON
        datos_json = json.dumps(preguntas, indent=4, ensure_ascii=False)
        json_text.delete("1.0", tk.END)  # Limpiar contenido actual
        json_text.insert(tk.END, datos_json)

    def limpiar_mensaje():
        """
        Función encargada de limpiar el mensaje de confirmación.
        """
        mensaje_confirmacion.config(text="", fg="black")

    def mostrar_campos_adicionales(tipo_seleccionado):
        """
        Dependiendo del tipo de pregunta, se muestran sus campos adicionales (si los tiene).
        """
        global limite_entry
        global valor_maximo_entrada
        global valor_minimo_entrada
        global opciones_entry
        global obligatorio_entry
        global dominios_entry
        global primera_fecha_entry
        global ultima_fecha_entry
        global expresion_regular_entry

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
            opciones_label = tk.Label(campos_adicionales_frame, text="Opciones (separadas por ';') :*")
            opciones_label.grid(row=0, column=0, padx=5, pady=5)
            opciones_entry = tk.Entry(campos_adicionales_frame, borderwidth=2)
            opciones_entry.grid(row=1, column=0, padx=5, pady=5)
            opciones_label.configure(bg=root.cget('bg')) # fondo

        elif tipo_seleccionado == "casilla de verificación":
            obligatorio_label = tk.Label(campos_adicionales_frame, text="Indique si es obligatorio o no:*")
            obligatorio_label.grid(row=0, column=0, padx=5, pady=5)
            obligatorio_label.configure(bg=root.cget('bg')) # fondo
            # obligatorio_entry es un desplegable con si y no
            obligatorio_entry = ttk.Combobox(campos_adicionales_frame, values=["Sí", "No"], state="readonly")
            obligatorio_entry.grid(row=1, column=0, padx=5, pady=5)
            obligatorio_entry.set("No") # por defecto, no es obligatorio


        elif tipo_seleccionado == "correo electrónico":
            dominios_disponibles_label = tk.Label(campos_adicionales_frame, text="Dominios permitidos (separados por ';') :")
            dominios_disponibles_label.grid(row=0, column=0, padx=5, pady=5)
            dominios_disponibles_label.configure(bg=root.cget('bg'))

            dominios_entry = tk.Entry(campos_adicionales_frame, borderwidth=2)
            dominios_entry.grid(row=1, column=0, padx=5, pady=5)

        elif tipo_seleccionado == "DNI":
            pass # No tiene campos adicionales

        elif tipo_seleccionado == "teléfono":
            pass # No tiene campos adicionales

        elif tipo_seleccionado == "fecha":
            primera_fecha_label = tk.Label(campos_adicionales_frame, text="Primera fecha (dd/mm/yyyy):")
            primera_fecha_label.grid(row=0, column=0, padx=5, pady=5)
            primera_fecha_entry = tk.Entry(campos_adicionales_frame, borderwidth=2)
            primera_fecha_entry.grid(row=1, column=0, padx=5, pady=5)

            ultima_fecha_label = tk.Label(campos_adicionales_frame, text="Última fecha (dd/mm/yyyy):")
            ultima_fecha_label.grid(row=0, column=1, padx=5, pady=5)
            ultima_fecha_entry = tk.Entry(campos_adicionales_frame, borderwidth=2)
            ultima_fecha_entry.grid(row=1, column=1, padx=5, pady=5)

            primera_fecha_label.configure(bg=root.cget('bg')) # fondo
            ultima_fecha_label.configure(bg=root.cget('bg')) # fondo

        elif tipo_seleccionado == "campo especial":
            expresion_regular_label = tk.Label(campos_adicionales_frame, text="Expresión regular:*")
            expresion_regular_label.grid(row=0, column=0, padx=5, pady=5)
            expresion_regular_entry = tk.Entry(campos_adicionales_frame, borderwidth=2)
            expresion_regular_entry.grid(row=1, column=0, padx=5, pady=5)

            expresion_regular_label.configure(bg=root.cget('bg'))
            



    def agregar_pregunta():
        """
        Función encargada de agregar una pregunta a la lista de preguntas.
        """

        # se obtiene el tipo y la pregunta.
        tipo_seleccionado = tipo_pregunta_combobox.get()
        pregunta = pregunta_entry.get()
        campos_adicionales = {}

        # Validar que se haya seleccionado un tipo de pregunta
        if not tipo_seleccionado:
            mensaje_confirmacion.config(text="Por favor, seleccione primero un tipo de pregunta.", fg="red")
            return

        # Validar que se haya ingresado un título para la pregunta
        if not pregunta:
            mensaje_confirmacion.config(text="Por favor, ingrese un título para la pregunta.", fg="red")
            return

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
            
        elif tipo_seleccionado == "casilla de verificación":
            # modificamos el nombre del tipo
            tipo_seleccionado = "casilla"
            obligatorio = obligatorio_entry.get()
            if obligatorio == "Sí":
                campos_adicionales["obligatorio"] = True
            elif obligatorio == "No":
                campos_adicionales["obligatorio"] = False
            else:
                mensaje_confirmacion.config(text="Por favor, seleccione si la casilla es obligatoria o no.", fg="red")
                return
            
        elif tipo_seleccionado == "correo electrónico":
            tipo_seleccionado = "email" # modificamos el nombre del tipo
            dominios = dominios_entry.get()
            if dominios:
                dominios = dominios.split(";")
                campos_adicionales["dominiosDisponibles"] = dominios

        elif tipo_seleccionado == "DNI":
            tipo_seleccionado = "dni" # modificamos el nombre del tipo
            # no tiene campos adicionales.

        elif tipo_seleccionado == "teléfono":
            tipo_seleccionado = "telefono"
            # no tiene campos adicionales.

        elif tipo_seleccionado == "fecha":
            primera_fecha = primera_fecha_entry.get()
            ultima_fecha = ultima_fecha_entry.get()
            if primera_fecha:
                if not validar_fecha(primera_fecha):
                    mensaje_confirmacion.config(text="La primera fecha no tiene un formato válido (dd/mm/yyyy) ó (dd-mm-yyyy).", fg="red")
                    return
                campos_adicionales["primeraFecha"] = primera_fecha
            if ultima_fecha:
                if not validar_fecha(ultima_fecha):
                    mensaje_confirmacion.config(text="La última fecha no tiene un formato válido (dd/mm/yyyy) ó (dd-mm-yyyy).", fg="red")
                    return
                campos_adicionales["ultimaFecha"] = ultima_fecha

        elif tipo_seleccionado == "campo especial":
            tipo_seleccionado = "campoEspecial" # modificamos el nombre del tipo
            expresion_regular = expresion_regular_entry.get()
            if expresion_regular:
                # validar expresión regular
                if not validar_expresion_regular(expresion_regular):
                    mensaje_confirmacion.config(text="La expresión regular no es válida.", fg="red")
                    return
                campos_adicionales["expresionRegular"] = expresion_regular
            else:
                mensaje_confirmacion.config(text="Por favor, ingrese una expresión regular.", fg="red")
                return
                

            

        # Se almacena la pregunta y los campos adicionales en la lista
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
        elif tipo_seleccionado == "casilla" or tipo_seleccionado == "casilla de verificación":
            pass # No tiene campos adicionales
        elif tipo_seleccionado == "email" or tipo_seleccionado == "correo electrónico":
            dominios_entry.delete(0, tk.END)
        elif tipo_seleccionado == "dni":
            pass # No tiene campos adicionales
        elif tipo_seleccionado == "telefono":
            pass # No tiene campos adicionales
        elif tipo_seleccionado == "fecha":
            primera_fecha_entry.delete(0, tk.END)
            ultima_fecha_entry.delete(0, tk.END)
        elif tipo_seleccionado == "campoEspecial" or tipo_seleccionado == "campo especial":
            expresion_regular_entry.delete(0, tk.END)

        # Mostrar mensaje de confirmación
        mensaje_confirmacion.config(text="La pregunta se ha agregado correctamente.", fg="black")

        # Actualizar JSON en el área de texto
        mostrar_json()  



    #####? VENTANA PRINCIPAL #####

    # Se crea la ventana principal.
    root = tk.Tk()
    root.title("Generador de Formularios")
    root.geometry("800x600")
    root.configure(bg="white")

    root.columnconfigure(0, weight=1)  # Expand column 0 (for 'Tipo de pregunta' and 'Pregunta')
    root.columnconfigure(1, weight=1)  # Expand column 1 (for the Combobox and Entry)
    root.columnconfigure(2, weight=1)  # Expand column 2 (for the 'Campos adicionales' frame)

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
    agregar_pregunta_button = tk.Button(root, text="Agregar pregunta", command=agregar_pregunta, bg="green", fg="white")
    agregar_pregunta_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

    # Botón para convertir a JSON
    convertir_button = tk.Button(root, text="Generar formulario", command=crear_formulario, bg="green", fg="white")
    convertir_button.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="w")

    # Lista para almacenar las preguntas
    preguntas = []


    # Mostrar JSON
    json_text = tk.Text(root, height=20, width=50)
    json_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
    root.rowconfigure(4, weight=1)  # Hacer que la fila 4 se expanda
    root.columnconfigure(1, weight=1)  # Hacer que la columna 1 se expanda
    mostrar_json()  # Mostrar JSON inicialmente

    # Etiqueta para mostrar el mensaje de confirmación
    mensaje_confirmacion = tk.Label(root, text="")
    mensaje_confirmacion.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="w")
    mensaje_confirmacion.configure(bg=root.cget('bg')) # fondo

    # Iniciar la aplicación
    root.mainloop()
