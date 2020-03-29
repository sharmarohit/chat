import socket

# Max size of a UDP datagram
MAX_SIZE_BYTES = 65535

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3006
hostname = '127.0.0.1'
# binding to an IP and a port
serversocket.bind((hostname, port))
print('Listening at {}'.format(serversocket.getsockname()))

#Listen indefinitely
while True:
    data, clientAddress = serversocket.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    print('The Client at {} says {!r}'.format(clientAddress, message))
    msg_to_send = input('Input message to send to Client:')
    data = msg_to_send.encode('ascii')
    serversocket.sendto(data, clientAddress)