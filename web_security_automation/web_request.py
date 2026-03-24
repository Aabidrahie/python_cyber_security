import urllib.request

url = "https://httpbin.org/get"

# Add headers (VERY IMPORTANT for Google)
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Create request object
req = urllib.request.Request(url, headers=headers)

# Send request
response = urllib.request.urlopen(req)

# Read response
data = response.read()

print(data.decode('utf-8'))
