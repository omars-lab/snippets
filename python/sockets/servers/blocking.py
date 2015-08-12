import socket
import random
import time

# A blocking server that simply sends hello to anyone who conncets to it


def blocking_server(bind='0.0.0.0', port=8080, queued_connections=5):
    """
    This sets up a blocking socket. We will be listening for incomming
    conncetions
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((bind, port))
    sock.listen(queued_connections)  # max num of queued connections
    return sock


def handle_connections(server):
    """
    To accept connections and send data on a server socket that is alerady set
    up. Accepting a connection creates a seperate socker with the server we
    accepted to connect to.
    """
    # Accept a connection. The socket must be bound to an address and listening
    # for connections. The return value is a pair (conn, address) where conn is
    # a new socket object usable to send and receive data on the connection,
    # and address is the address bound to the socket on the other end of the
    # connection.
    sock, addr = server.accept()  # this is a blocking call
    time.sleep(random.randint(1,5))
    sock.sendall("Hello")  # this is a blocking call
    sock.close()

server = blocking_server()
while True:
    handle_connections(server)
