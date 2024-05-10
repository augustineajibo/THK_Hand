import socket
import random
import string

if __name__ == "__main__":
    #creating a socket instance
    server_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    #Connecting to the localhost
    ip_address = "192.168.30.201"
    port = 555
    server_object.bind((ip_address, port))
    server_object.listen()
    print("...connected to port ", port)

    #Once the client connects to the given port, the server starts to accept request
    #print(server_object.accept())
    connection_object, _ = server_object.accept()

    print(connection_object)

    if connection_object:
        #Connected to client successfully
        print("Server connected to client")

        # sending initial message to the client
        connection_object.send(b"type the message")

        # receiving message from the client
        data_receive = connection_object.recv(1024)

        while data_receive != b'stop':
            print("{}: {}".format("CLIENT MESSAGE: ", data_receive.decode('utf-8')))
            server_input = random.choice(string.ascii_letters)
            connection_object.send(server_input.encode('utf-8'))
            data_receive = connection_object.recv(1024)



