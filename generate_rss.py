import requests

# API Base44
url = "https://cantine-rapide-go.base44.app/api/apps/69a563ac3aae8ad0e6d45ec7/entities/Classe?sort=ordre"

# Récupération des données
data = requests.get(url).json()

# Début du RSS
xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Ordre du Self</title>
<description>Ordre de passage en temps réel</description>
<link>https://cantine-rapide-go.base44.app</link>
"""

# Boucle pour chaque élément
for item in data:
    xml += f"""
<item>
<title>{item['ordre']} - {item['classe']}</title>
<description>{item.get('statut', '')}</description>
<guid>{item['id']}</guid>
</item>
"""

# Fin du RSS
xml += """
</channel>
</rss>
"""

# Écriture dans le fichier
with open("cantine.xml", "w", encoding="utf-8") as f:
    f.write(xml)
