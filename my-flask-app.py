#Flask es un framework de Python que permite construir aplicaciones web de manera sencilla y rápida.
from flask import Flask

#Flask() necesita un nombre que identifique la app.
#"MyFlaskApp" es solo una etiqueta interna (usualmente se usa __name__ en vez de un string, pero aquí es más didáctico).
#app será nuestro objeto principal para configurar rutas, correr el servidor, etc.

app = Flask("MyFlaskApp")


#Definimos la ruta con el método get.
@app.route('/', methods=['GET'])


#Función welcome.
def welcome():
    return "<h1>Hello MUNDOOOOOOOOOOOOOO</h1>"

#Si este archivo se ejecuta directamente, entonces:
if __name__ == '__main__':
    app.run()