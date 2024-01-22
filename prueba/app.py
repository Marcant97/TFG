from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])

    # Verificamos si la edad está dentro del rango
    if 1 <= edad <= 120:
        mensaje = f'Hola, {nombre}. Tu edad es {edad} años.'
    else:
        mensaje = 'Edad fuera del rango permitido.'
    return mensaje

if __name__ == '__main__':
    app.run(debug=True)
