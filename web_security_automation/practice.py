import urllib.request
import urllib.parse

url = "https://httpbin.org/post"

data = {
		"username":"admin",
			"password":"12345"
	}
	
encoded_data = urllib.parse.urlencode(data).encode()

headers = {
			"User-Agent":"Mozila/5.0"
			}

request = urllib.request.Request(url,data=encoded_data,headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode())
