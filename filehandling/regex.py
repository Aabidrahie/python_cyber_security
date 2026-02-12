import re
count = 0
# Proper IP regex pattern
ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
with open("auth.log", "r") as file:
    for line in file:
        if "from" in line:
            count += 1
            # Find all IP addresses in the line
            ips = re.findall(ip_pattern, line)
            for ip in ips:
                print(ip)
print("--------------------")
print("The number of IP's used are:", count)
