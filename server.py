import socket
import threading


def handler(client_sock, client_addr):
    """ Handling client input """
    print('Connected by ', client_addr) # Client address printed on server
    while True:
        data = client_sock.recv(1024)   # Receive data from client socket
        if not data:
            break
        else:
            # Print who says what
            print(str(client_addr) + ':' + str(data.decode("utf-8")))
            client_sock.send(data)      # Send back the data


if __name__ == '__main__':

    host = 'localhost'        # Setting up localhost as the host
    port = 10000              # Arbitrary non-privileged port

    # Creating server socket and allowing address reuse
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))    # Binding the socket to the address (host, port)

    while True:
        s.listen(5)             # Listen to connections, queueing up to 5
        print('Server is listening...')
        client_sock, client_addr = s.accept()   # Accept connection
        # Start new thread for every connection
        new_thread = threading.Thread(target=handler, args=(client_sock, client_addr,))
        new_thread.start()
