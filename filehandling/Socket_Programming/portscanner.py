import socket

# Take input from user
target = input("Enter target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print("\nScanning started...\n")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Timeout of 1 second

    result = s.connect_ex((target, port))   
#Python → OS → TCP → Network.
#inet_pton comes into play
#Steps
#Kernel does:
#Convert IP to binary
#Validate port
#Lookup routing table
#Resolve MAC (ARP if needed)
#Assign source port
#Create TCP control block
#Send SYN
#Wait for reply
#Update TCP state
#Return status code

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    s.close()

print("\nScanning completed.")