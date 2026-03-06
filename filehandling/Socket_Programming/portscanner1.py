import socket

target_IP = input("Enter the target IP:	")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

for port in range(start_port, end_port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1)
	if s.connect_ex((target_IP, port)) == 0:
		print(f"Port number {port} is OPEN")
	else:
		print(f"Port number {port} is CLOSED")
	s.close()
print("*********************PORT SCANNING DONE************")
	
