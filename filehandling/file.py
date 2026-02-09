failed_attempts = {}

with open("auth.log") as file:
    for line in file:
        if "FAILED" in line:
            ip = line.split("IP=")[1].strip()
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

for ip, count in failed_attempts.items():
    if count >= 5:
        print(f"Brute-force suspected from {ip}")
