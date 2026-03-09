import requests

url = "https://cantine-rapide-go.base44.app/rss"

response = requests.get(url)
response.raise_for_status()

rss = response.text

with open("cantine.xml", "w", encoding="utf-8") as f:
    f.write(rss)

print("RSS copié depuis Base44")
