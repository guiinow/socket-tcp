import socket

def send_message(sock, message):
    sock.sendall(message.encode())

def receive_message(sock):
    data = sock.recv(1024)
    return data.decode()

# Crie um cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecte-se ao servidor
server_address = ("localhost", 8081)
client.connect(server_address)

while True:
    # Exibir o menu
    menu = """
    1. Enviar mensagem
    2. Receber mensagem
    3. Sair
    """
    print(menu)

    choice = input("Escolha uma opção: ")

    if choice == "1":
        sender_name = input("Nome do remetente: ")
        receiver_name = input("Nome do destinatário: ")
        message = input("Digite a mensagem: ")
        data = f"from:{sender_name}:{client.getsockname()[0]}:{receiver_name}:{server_address[0]}:{message}"
        send_message(client, data)
    elif choice == "2":
        data = receive_message(client)
        print(f"Mensagem do servidor: {data}")
    elif choice == "3":
        break

# Feche a conexão com o servidor
client.close()
