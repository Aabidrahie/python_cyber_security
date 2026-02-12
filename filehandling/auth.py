import re 

pattern = r"\b\d+\.\d+\.\d+\.\d+\b"

with open("auth.log","r") as file:
    for line in file:
        if "from" in line:
            ips = re.findall(pattern,line)
            for ip in ips:
                print(ip)