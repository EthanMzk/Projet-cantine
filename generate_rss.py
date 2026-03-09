import requests

url = "https://cantine-rapide-go.base44.app/rss"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/rss+xml, application/xml"
}

response = requests.get(url, headers=headers)
content = response.text

# garder seulement le flux RSS
start = content.find("<rss")
end = content.find("</rss>")

if start != -1 and end != -1:
    rss = content[start:end+6]

    with open("cantine.xml", "w", encoding="utf-8") as f:
        f.write(rss)

    print("RSS mis à jour depuis Base44")
else:
    print("Flux RSS non trouvé")
