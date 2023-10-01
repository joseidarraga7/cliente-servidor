import socket
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultar', methods=['POST'])
def consultar():
    pais = request.form['pais']

    # Configuración del cliente
    host = '127.0.0.1'  # Dirección IP del servidor
    port = 8080       # Puerto del servidor

    # Crear un socket del cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor
    client_socket.connect((host, port))

    # Enviar el nombre del país al servidor
    client_socket.send(pais.encode('utf-8'))

    # Recibir la capital del servidor
    capital = client_socket.recv(1024).decode('utf-8')

    # Cerrar la conexión
    client_socket.close()

    return render_template('resultado.html', pais=pais, capital=capital)

if __name__ == '__main__':
    app.run()
