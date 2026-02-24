import socket

target = input("Enter target IP: ")
port = int(input("Enter target port: "))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)

    if s.connect_ex((target, port)) == 0:
        print(f"\n[+] Connected to {target}:{port}")

        # Send HTTP request (optional)
        s.send(b"HEAD / HTTP/1.1\r\n\r\n")

        banner = s.recv(1024)
        print("[+] Response:")
        print(banner.decode(errors="ignore"))
    else:
        print("[-] Port closed or filtered.")

    s.close()

except Exception as e:
    print("Error:", e)
