import socket
import time


tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.bind(('0.0.0.0', 8080))
tcp_sock.listen(1)

while True:
    conn, addr = tcp_sock.accept()
    with conn:
        data = conn.recv(1024)
        print(f'I have received from the customer: {data.decode("utf-8")}')
        
        conn.sendto(b'Hello customer!', addr)
        time.sleep(1)