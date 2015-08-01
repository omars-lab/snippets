import socket
import select
# ----------------------------reactor loop ------------------------------------
# select call blocks until one or more of the sockets is ready for read I/O
# Usage:
# read sockets, write sockets, exceptional condition =
#       select.select(read object, write obj, exceptional objects)


def select_socket(ip='localhost', port=8080):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(ip, port)
    sock.setblocking(0)

sockets = [select_socket(), select_socket(), select_socket(), select_socket()]

while sockets:
    # this select call blocks until one or more of the
    # sockets is ready for read I/O
    rlist, _, _ = select.select(sockets, [], [])

    # rlist is the list of sockets with data ready to read
    for sock in rlist:
        print sock.recv(1024)
