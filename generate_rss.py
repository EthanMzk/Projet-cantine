import requests
import re

url = "https://cantine-rapide-go.base44.app/rss"

response = requests.get(url)
html = response.text

# chercher le bloc RSS dans la page
match = re.search(r"<rss.*</rss>", html, re.DOTALL)

if match:
    rss = match.group(0)

    with open("cantine.xml", "w", encoding="utf-8") as f:
        f.write(rss)

    print("RSS extrait et mis à jour")
else:
    print("Erreur : aucun flux RSS trouvé")
