import socket
target_IP = input("Enter the target IP:	")
port = int(input("Enter the port number:	"))

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	if s.connect_ex((target_IP, port)) == 0:
		s.send(b"HEAD / HTTP/1.1\r\n\r\n")
		banner = s.recv(1024)
		print(banner.decode("utf-8"))
	else:
		print("Port is closed or filtered")
	s.close()
	
except Exception as e:
	print("Error",e)
