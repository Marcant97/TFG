# Generador de Código para la Automatización de la Creación de Formularios en Desarrollos Python
Este repositorio contiene el código de la herramienta desarrollada para el Trabajo Fin de Grado del Grado en Ingeniería Informática.

#### Alumno: **Marco Antonio Barroso Hormiga**
#### Tutora: **María Elena Sánchez Nielsen**

### Descripción:

El objetivo de este Trabajo Fin de Grado es la implementación de una herramienta que automatice la generación de código Python/Django para la creación de formularios. Esta aplicación toma como entrada ficheros en formato JSON. La herramienta desarrollada no solo se encargará de leer y procesar el fichero JSON
de entrada, sino que también creará y configurará un proyecto Django al completo, inclu-
yendo todos los componentes necesarios para que el formulario funcione correctamente.
Esto incluye la creación de modelos, vistas y plantillas, así como la configuración de rutas
y validaciones necesarias.

Todo ello se realiza a través de una interfaz gráfica simple desarrollada con la librería Tkinter. Por último, se inicia un servidor en modo desarrollo y se abre el navegador web por defecto para visualizar el formulario creado de forma automática.

### Rutas disponibles:

- **/home**: Página de inicio
- **/formulario**: Página donde se aloja el formulario creado.
- **/admin**: Página de administración de Django. Credenciales del superusuario creado por defecto: Usuario: _admin_, Contraseña: _adminpass_
- **/enviar**: Página de confirmación de envío del formulario.


### Instrucciones de uso:
Para usar el generador se dispone de 2 alternativas:

1. En el directorio _/dist/inicio_ se encuentra el ejecutable de la aplicación. Para usarlo es necesario clonar la carpeta _\_internal_ así como el ejecutable.

2. La otra opción consiste en clonar la carpeta _/src_ y ejecutar el archivo _inicio.py_.

Para ambas opciones es necesario tener instalada una versión reciente de Python instalada en el sistema, así como una versión de Django. Además, sólo funciona para sistemas Windows.


### Formularios de prueba y proyectos ya generados:

En _/ejemplos_ se encuentra una serie de formularios diferentes a modo de ejemplo. Además, en _/dist/inicio\_proyecto\_django_ se encuentran los proyectos generados a partir de los formularios de ejemplo.


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