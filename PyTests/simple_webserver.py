# simple webserver

import socket
import sys

import pyconsole
pyconsole.start_console_server()

HOST, PORT = '', 8888

# Create a socket (SOCK_STREAM means a TCP socket)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Bind the socket to the port
    sock.bind((HOST, PORT))
    # Listen on the socket
    sock.listen(1)
    print('Serving HTTP on port {port} ...'.format(port=PORT))
    while True:
        # Wait for a connection
        connection, client_address = sock.accept()
        try:
            data = connection.recv(1024)
            print(data)
            connection.sendall(b'HTTP/1.0 200 OK\n\nHello World')
        finally:
            connection.close()
