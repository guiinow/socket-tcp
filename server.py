import socket

# Crie uma lista para armazenar as conexões
connections = []

# Crie um objeto socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincule o soquete a uma porta
server_address = ("localhost", 8081)
sock.bind(server_address)

# Ouça conexões
sock.listen()

def send_message(connection, message):
    connection.sendall(message.encode())

def receive_message(connection):
    data = connection.recv(1024)
    return data.decode()

print("Aguardando conexões...")

while True:
    connection, client_address = sock.accept()
    connections.append(connection)
    print(f"Conexão estabelecida com {client_address}")

    data = receive_message(connection)

    if data.startswith("from:"):
        parts = data.split(":")
        sender_name = parts[1]
        sender_ip = parts[2]
        receiver_name = parts[3]
        receiver_ip = parts[4]
        message = ":".join(parts[5:])
        for conn in connections:
            if conn != connection:
                send_message(conn, data)

    elif data.startswith("register:"):
        client_name, client_ip = data.split(":")[1:]
        connections.append((client_name, client_ip))
        send_message(connection, "Registered!")

    else:
        print(data)

    connection.close()

# Feche o soquete
sock.close()
