import socket

#1. Configuración del cliente
host = '127.0.0.1'  # Dirección IP del servidor
port = 8080       # Puerto del servidor

#2. Crear un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#3. Conectar al servidor
client_socket.connect((host, port))

while True:
    pais = input("Escriba el nombre de un país (o 'exit' para salir): ")
    if pais == 'exit':
        break

    #4. Enviar el nombre del país al servidor
    client_socket.send(pais.encode('utf-8'))

    #5. Recibir la capital del servidor y mostrarla
    capital = client_socket.recv(1024).decode('utf-8')
    print(f"La capital de {pais} es {capital}")

#6. Cerrar la conexión
client_socket.close()