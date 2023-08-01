import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ("localhost", 8080)
sock.connect(server_address)

# Send data to the server
data = "Hello from the client!".encode()
sock.sendall(data)

# Receive data from the server
data = sock.recv(1024)

# Print the data
print(data.decode())

# Close the connection
sock.close()