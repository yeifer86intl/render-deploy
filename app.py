"""
Librerias y funciones: 
1. Flask: clase principal del framework Flask, para crear la app web.
    
    1.1 request: permite acceder a los datos enviados desde el navegador (como formularios).
    1.2 render_template: permite renderizar archivos HTML desde una carpeta llamada templates.

2. pickle: Permite cargar el modelo de Machine Learning previamente guardado.

3. numpy: Realizar manipulaciones matriciales.


4 gunicorn (Green Unicorn) es un servidor WSGI (Web Server Gateway Interface) para aplicaciones web en Python, 
especialmente diseñado para entornos de producción. 

Se utiliza comúnmente para desplegar aplicaciones desarrolladas con frameworks como Flask, Django u otros frameworks WSGI.
"""

from flask import Flask, request, render_template
import pickle
import numpy as np


# Se crea una instancia de la aplicación Flask, donde: __name__ es equivalente a  "__main__" .
app = Flask(__name__)

# Cargar modelo ya entrenado.
with open('modelo_iris.pkl', 'rb') as f:
    model = pickle.load(f)

#En Flask, @app.route('/') asocia una URL con una función de Python. Es decir:

#Cuando el navegador accede a la URL raíz del servidor (/), ejecuta la función home().

@app.route('/')
def home():
    return render_template('index.html')


#Define una ruta accesible desde el navegador al enviar el formulario (action="/predict").

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)
    prediction = model.predict(final_features)
    output = int(prediction[0])

    labels = ["Setosa", "Versicolor", "Virginica"]
    return render_template('index.html', prediction_text=f'La flor es: {labels[output]}')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)