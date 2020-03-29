import socket

MAX_SIZE_BYTES = 65535
host = '127.0.0.1'
port = 3006

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientsocket.connect((host, port))

while True:
    message = input('Input message in lowercase:')
    data = message.encode('ascii')
    clientsocket.send(data)

    data = clientsocket.recv(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    print('The server replied with {!r}'.format(text))
