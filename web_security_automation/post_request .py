import urllib.request
import urllib.parse

url = "https://httpbin.org/post"

# Data to send
data = {
    "username": "admin",
    "password": "1234"
}

# Encode data
encoded_data = urllib.parse.urlencode(data).encode()

# Add headers
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Create request
req = urllib.request.Request(url, data=b"test", headers=headers)

# Send request
response = urllib.request.urlopen(req)

# Output
print(response.read().decode())
