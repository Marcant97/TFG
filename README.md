# Generador de Código para la Automatización de la Creación de Formularios en Desarrollos Python
Este repositorio contiene la herramienta desarrollada para el Trabajo de Fin de Grado del Grado en Ingeniería Informática.
Se realizará un generador de código para la automatización de la creación de formularios en desarrollos Python.

#### Alumno: **Marco Antonio Barroso Hormiga**
#### Tutora: **María Elena Sánchez Nielsen**


### Pasos:
1. Se inicia una interfaz gráfica que permite elegir un fichero de entrada en formato JSON o construir un formulario desde cero.
2. Se comprueba la versión de django instalada en el sistema.
********3. Se borra el proyecto anterior si existe.
3. A partri del fichero seleccionado o generado, se lee, se obtiene el contenido y se verifica que sea correcto.
4. Se crea y configura un proyecto django por completo
5. Se crea un superusuario al que se puede acceder en /admin con user: admin, pass: adminpass.
4. Se arranca el servidor en modo desarrollo y se abre el formulario en el navegador.

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