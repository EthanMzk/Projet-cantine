import requests

url = "https://cantine-rapide-go.base44.app/api/apps/69a563ac3aae8ad0e6d45ec7/entities/Classe?sort=ordre"
data = requests.get(url).json()

xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Ordre du Self</title>
<description>Ordre de passage en temps réel</description>
<link>https://cantine-rapide-go.base44.app</link>
"""

for item in data:
    ordre = item.get('ordre', '')
    classe = item.get('classe') or item.get('Classe') or item.get('nom', '')
    statut = item.get('statut', '')
    id_item = item.get('id', '')

    xml += f"""
<item>
<title>{ordre} - {classe}</title>
<description>{statut}</description>
<guid>{id_item}</guid>
</item>
"""

xml += """
</channel>
</rss>
"""

with open("cantine.xml", "w", encoding="utf-8") as f:
    f.write(xml)
