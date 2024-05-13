import socket
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Define the host and port you want to connect to
host = '192.168.30.200'
port = 1024
# Connect to the server
s.connect((host, port))

# Send data to the server
s.send(b'\x00\x01\x00') #return all finger to original/default position
#s.send(b'\x00\x01\x00')

# Receive data from the server
data = s.recv(1024)
print('Received:', data.decode('utf-8'))
# Close the socket connection
s.close()