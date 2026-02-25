import socket

target = input("Enter the target IP: ")
start_port = int(input("Enter the start port:  "))
end_port = int(input("Enter the end port:  "))

for port in range(start_port,end_port + 1):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1)
	result = s.connect_ex((target,port))
	
	if result == 0:
		print(f"Port number {port} is open")
	else:
		print(f"Port number {port} is closed")
		
	s.close()
