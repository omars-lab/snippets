import socket


def blocking_client(ip='localhost', port=8080):
    """
    A blocking client
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(ip, port)  # connect to a remote socket
    data = sock.recv(1024)  # blocking call
    sock.close()
    return data

print blocking_client()
