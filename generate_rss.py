import requests
from bs4 import BeautifulSoup  # pour extraire proprement le XML

# URL Base44
url = "https://cantine-rapide-go.base44.app/rss"

# Récupère la page
response = requests.get(url)
response.raise_for_status()
html = response.text

# Utilise BeautifulSoup pour extraire le XML
soup = BeautifulSoup(html, "html.parser")

# Cherche la balise <rss> et récupère tout le contenu XML
rss_tag = soup.find("rss")
if rss_tag is None:
    raise ValueError("Pas de balise <rss> trouvée dans le flux Base44 !")

xml = str(rss_tag)  # contient <rss>...</rss>

# Écrit cantine.xml
with open("cantine.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print("RSS nettoyé et mis à jour")
