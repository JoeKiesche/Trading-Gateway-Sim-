import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connecting to server...\n")
client.connect(('127.0.0.1', 9999))

client.send('Client Connected!'.encode())
print(client.recv(1024).decode())