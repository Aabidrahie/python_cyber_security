import re
count = 0
# Proper IP regex pattern
ip_pattern = r"\b\d+\.\d+\.\d+\.\d+\b"
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
