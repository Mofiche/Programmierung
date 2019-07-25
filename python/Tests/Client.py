import socket

### calc Primfaktoren

number = 8021

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.2.104', 1337))
client_socket.send(bytes(str(number), 'utf8'))
while True:
  #  (socket, addr) = client_socket.accept()
    msg = str(client_socket.recv(2**10), 'utf8')
    print(msg)
