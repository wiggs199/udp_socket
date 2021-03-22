import socket

# Mazimum size of a UDP datagram
MAX_SIZE_BYTES = 65535

# Schemes used ( family=type of address , type=transport layer)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3000
hostname = '127.0.0.1'
# Bind the socket to a port and IP address
s.bind((hostname, port))
# Printing the IP address and port of socket
print('Listening at {}'.format(s.getsockname()))

while True:
    # Receive at most 65535 bytes at once
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    upperCaseMessage = message.upper()
    print('The client at {} says {!r}'.format(clientAddress, message))
    data = upperCaseMessage.encode('ascii')
    s.sendto(data, clientAddress)
