import socket

# 1. Diccionario de países y capitales
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá',
    'Perú': 'Lima',
    'Venezuela': 'Caracas',
    'Bolivia' : 'Sucre',
    'Uruguay' : 'Montevideo',
    'Paraguay' : 'Asunción'
}

# 2. Función para buscar la capital de un país
def obtener_capital(pais):
    return paises_capitales.get(pais, 'País no encontrado')

# 3. Configuración del servidor
host = '127.0.0.1'
port = 8080

# 4. Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 5. Vincular el socket al host y puerto
server_socket.bind((host, port))

# 6. Escuchar conexiones entrantes (máximo 3 clientes en este ejemplo)
server_socket.listen(3)

print("El servidor esta escuchando en " + str(host) + " " + str(port))

# 7. Aceptar una conexión entrante
client_socket, client_address = server_socket.accept()

while True:
    # 8. Recibir el país enviado por el cliente
    pais = client_socket.recv(1024).decode('utf-8')
    if not pais:
        break  # Si no hay datos, terminar la conexión

    # 9. Buscar la capital y enviarla de vuelta al cliente
    capital = obtener_capital(pais)
    client_socket.send(capital.encode('utf-8'))

# 10. Cerrar la conexión
client_socket.close()