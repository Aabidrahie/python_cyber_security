import socket       

#This library allows Python to use operating system networking APIs.

# Create socket (IPv4, TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#This tells OS: Use IPv4 addressing.

#STREAM = TCP

#You are telling OS: Create a TCP socket that uses IPv4.

# Bind to all interfaces on port 5000
server.bind(("192.168.222.129", 5000))
#This is where the IP and Port are actually used

# Listen for 1 client
server.listen(1)

#This tells OS: Convert this socket into a listening (server) socket.

print("Server waiting for connection...")

# Accept connection
conn, addr = server.accept()

#When a client connects:TCP performs:

#3-way handshake
#SYN
#SYN-ACK
#ACK


print("Connected by:", addr)


#addr contains client IP and client port

# Send message
conn.send(b"Hello from Kali Server!")



# Close connection
conn.close()
server.close()
