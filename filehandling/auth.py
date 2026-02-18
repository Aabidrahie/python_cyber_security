import re

pattern = r"\b\d+\.\d+\.\d+\.\d+\b"

with open("auth.log","r") as file:
    for line in file:
        ip_list = re.findall(pattern,line)
        for ip in ip_list:
            print(ip)