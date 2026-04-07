import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

# Step 1: Send request with headers (important for avoiding blocks)
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract key components

print("\n--- PAGE TITLE ---")
print(soup.title.text if soup.title else "No title found")

print("\n--- HEADINGS (h1 to h6) ---")
for i in range(1, 7):
    for tag in soup.find_all(f"h{i}"):
        print(f"h{i}: {tag.text.strip()}")

print("\n--- ALL LINKS ---")
for link in soup.find_all("a"):
    print(f"Text: {link.text.strip()} | URL: {link.get('href')}")

print("\n--- FORMS ---")
forms = soup.find_all("form")
for form in forms:
    print("\nForm action:", form.get("action"))
    print("Method:", form.get("method"))

    inputs = form.find_all("input")
    for inp in inputs:
        print(f"Input Name: {inp.get('name')} | Type: {inp.get('type')}")

print("\n--- IMAGES ---")
for img in soup.find_all("img"):
    print(img.get("src"))

print("\n--- META TAGS ---")
for meta in soup.find_all("meta"):
    print(meta.attrs)
