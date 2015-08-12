import errno
import socket


def asyn_client(ip='localhost', port=8080):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(ip, port)
    sock.setblocking(0)
    try:
        new_data = sock.recv(1024)
    except socket.error, e:
        if e.args[0] == errno.EWOULDBLOCK:
            # This error code means we would have blocked if the socket was
            # blocking. Instead of blocking, we would atempt to itterate
            # through all the sockets we have.
            break
    else:
        if not new_data:
            break
        else:
            data += new_data

    return data

print asyn_client()
print asyn_client()
print asyn_client()
