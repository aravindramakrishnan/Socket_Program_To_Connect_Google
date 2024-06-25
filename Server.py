import socket

# Create a socket object
s = socket.socket()
print("Socket created Successfully")

# Reserve a port on pc
port = 23456

# Bind to the port
s.bind(('', port))
print("socket binded to port %s " %port)

# Put socket in listening mode
s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print("Got connection from ", addr)

    c.send("Thank you for connecting".encode())

    c.close()

    break


