# Generador de Código para la Automatización de la Creación de Formularios en Desarrollos Python
Este repositorio contiene la herramienta desarrollada para el Trabajo de Fin de Grado del Grado en Ingeniería Informática.
Se realizará un generador de código para la automatización de la creación de formularios en desarrollos Python.

#### Alumno: **Marco Antonio Barroso Hormiga**
#### Tutora: **María Elena Sánchez Nielsen**

### Descripción:

La herramienta desarrollada permite:
1. Insertar un fichero en formato JSON con las preguntas del formulario siguiendo un formato determinado.
2. Generar de forma interactiva un formulario

Todo ello se realiza a través de una interfaz simple desarrollada con la librería Tkinter.
El formulario se genera en un proyecto Django, que se crea y configura de forma automática. Por último, se arranca un servidor en modo desarrollo y una ventana del navegador con el formulario generado para poder visualizarlo.

### Rutas disponibles:

- **/home**: Página de inicio
- **/formulario**: Página donde se aloja el formulario creado.
- **/admin**: Página de administración de Django. Credenciales del superusuario creado por defecto: Usuario: _admin_, Contraseña: _adminpass_
- **/enviar**: Página de confirmación de envío del formulario.


## Campos disponibles:

**Tipos genéricos:**
- [x] Campo de texto
- [x] Campo numérico
- [x] Desplegable
- [x] Casilla de verificación
- [x] Casilla de selección múltiple

**Tipos específicos:**
- [x] Correo electrónico
- [x] DNI
- [x] Teléfono
- [x] Fecha
- [x] Campo especial