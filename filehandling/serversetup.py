import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.222.129",9999))
server.listen(1)
print("Waiting for connection")

conn, addr = server.accept()
print("Connection established from: ", addr)
conn.send(b"There is a message from KALI Server")
conn.close()
server.close()