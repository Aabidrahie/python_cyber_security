import socket
import threading

target = input("Enter target IP: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\n[*] Scanning {target} from port {start_port} to {end_port}\n")

lock = threading.Lock()

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            with lock:
                print(f"[+] Port {port} is OPEN")

        s.close()

    except socket.gaierror:
        print("Hostname could not be resolved")
    except socket.error:
        pass
    except Exception as e:
        print(f"Error on port {port}: {e}")

threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\n[*] Scanning complete.")
