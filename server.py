import socket

# Create a list to store the connections
connections = []

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
server_address = ("localhost", 8080)
sock.bind(server_address)

# Listen for connections
sock.listen(1)

while True:

    # Accept a connection
    connection, client_address = sock.accept()

    # Add the connection to the list
    connections.append(connection)

    # Receive data from the client
    data = connection.recv(1024)

    # Print the data
    print(data.decode())

    # Send data back to the client
    connection.sendall("Hello from the server!".encode())

    # Send the data to all the other connections
    for other_connection in connections:
        if other_connection != connection:
            other_connection.sendall(data)

    # Close the connection
    connection.close()