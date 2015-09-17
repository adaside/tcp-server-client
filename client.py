import socket

host = 'localhost'
port = 10000

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect((host, port))       # Connect to server

while True:
    data = input("> > ")            # Input data
    if not data:
        break
    else:
        client_sock.send(str.encode(data))      # Send data

        incoming = client_sock.recv(1024)       # Receive data
        if not incoming:
            break
        else:
            print(str(incoming.decode("utf-8")))
client_sock.close()
