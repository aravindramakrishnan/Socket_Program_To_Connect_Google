import socket

s = socket.socket()

# Define the port to connect
port = 23456

s.connect(('127.0.0.1', port))

print(s.recv(1024).decode())

s.close()
