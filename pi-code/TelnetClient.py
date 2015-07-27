import socket

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 4444                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close()