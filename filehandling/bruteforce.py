failed = {}
with open('auth.log', 'r') as file:
    for line in file:
        if 'Failed' in line and 'from' in line:
            parts = line.split()
            ip = parts[parts.index('from') + 1]
            failed[ip] = failed.get(ip, 0) + 1
            for ip, count in failed.items():
                if count >= 5:
                    print('Brute force suspected from', ip)

