import re

unique_ips = set()

ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

with open("auth.log", "r") as file:
    for line in file:
        ips = re.findall(ip_pattern, line)
        for ip in ips:
            unique_ips.add(ip)

print("--------------------")
print("Unique IPs found:", len(unique_ips))
