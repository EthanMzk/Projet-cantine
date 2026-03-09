import requests

url = "https://cantine-rapide-go.base44.app/rss"

response = requests.get(url)

with open("cantine.xml", "w", encoding="utf-8") as f:
    f.write(response.text)

print("RSS mis à jour")
