import urllib.request

url = "https://httpbin.org/get"

response = urllib.request.urlopen(url)

data = response.read()
print(data.decode())
