# An example to google using socket

import socket
import sys

# ip = socket.gethostbyname('www.google.com')

# print(ip)

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Successfully Created")
except socket.error as err:
    print("Socket connection failed with error %s " % err)

# Default Port number

port = 80

try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("There was an error resolvint the host")
    sys.exit()

# Connect To Server
s.connect((host_ip, port))

print("The Socket is successfully connected to Google")