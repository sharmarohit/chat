import socket

MAX_SIZE_BYTES = 65535

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#print('The OS assigned the address {} to me'.format(clientsocket.getsockname()))
message = input('Input message in lowercase:')
data = message.encode('ascii')
clientsocket.sendto(data, ('127.0.0.1', 3006))

data, address = clientsocket.recvfrom(MAX_SIZE_BYTES)
text = data.decode('ascii')
print('The server {} replied with {!r}'.format(address, text))
