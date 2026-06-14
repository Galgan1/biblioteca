import urllib.request
import os

url = "https://www.sogipa.com.br/web/imgs/arquivos/a-arte-da-guerra5e8e0e84.pdf"
dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads", "a-arte-da-guerra.pdf")
os.makedirs(os.path.dirname(dest), exist_ok=True)

print(f"Downloading to {dest}...")
urllib.request.urlretrieve(url, dest)
print(f"Done! File size: {os.path.getsize(dest)} bytes")
