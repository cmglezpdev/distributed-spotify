import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.122.66', 8080))

sock.sendall(b'Jorgitooooo!')

data = sock.recv(1024)
print(data.decode('utf-8'))

sock.close()