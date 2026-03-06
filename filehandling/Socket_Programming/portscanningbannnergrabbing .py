import socket

target = input("Enter the target IP: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")

            try:
                # First try receiving automatic banner
                banner = s.recv(1024)

                if banner:
                    print(f"    Banner: {banner.decode(errors='ignore').strip()}")

                else:
                    # Try HTTP request if no banner
                    request = f"HEAD / HTTP/1.1\r\nHost: {target}\r\n\r\n"
                    s.send(request.encode())

                    banner = s.recv(1024)

                    if banner:
                        print(f"    Response: {banner.decode(errors='ignore').strip()}")
                    else:
                        print("No banner received.")

            except:
                print("No banner received.")

        else:
            print(f"[-] Port {port} is CLOSED")

        s.close()

    except Exception as e:
        print(f"Error scanning port {port}: {e}")

print("\nPort scanning and banner grabbing completed.")
