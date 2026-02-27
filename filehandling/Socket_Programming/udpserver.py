import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("192.168.222.129", 40000))

print("Server ready...")

while True:
    data, addr = server.recvfrom(1024)
    print("Received:", data.decode())
    server.sendto(b"Hello Student!", addr)
    print(addr)
