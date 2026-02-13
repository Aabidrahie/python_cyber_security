failed = {}
with open("auth.log", "r") as file:
    count = 0
    for line in file:
        if "Failed password" in line and "from" in line:
            count += 1
            elements = line.split()
            if "from" in elements:
                ip = elements[elements.index("from") + 1]
                failed[ip] = failed.get(ip, 0) + 1
print("Brute Force Detection")
print("----------------------")
for ip, attempts in failed.items():
    if attempts >= 3:
        print("Brute force detected from IP:", ip)
print("\nTotal Failed Attempts:", count)
