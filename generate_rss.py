import requests

# 1️⃣ URL de l'API Base44
url = "https://cantine-rapide-go.base44.app/api/apps/69a563ac3aae8ad0e6d45ec7/entities/Classe?sort=ordre"

# 2️⃣ Récupération des données JSON
try:
    data = requests.get(url).json()
except Exception as e:
    print("Erreur lors de la récupération de l'API :", e)
    data = []

# 3️⃣ Début du RSS
xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Ordre du Self</title>
<description>Ordre de passage en temps réel</description>
<link>https://cantine-rapide-go.base44.app</link>
"""

# 4️⃣ Boucle sur chaque élément pour générer les items
for index, item in enumerate(data):
    ordre = item.get('ordre', '')
    # essaie différentes clés pour le nom de la classe
    classe = item.get('classe') or item.get('Classe') or item.get('nom', '')
    statut = item.get('statut', '')
    id_item = f"{index}-{item.get('id', '')}"  # format guid similaire à ton exemple

    xml += f"""
<item>
<title>{ordre} - {classe}</title>
<description>{statut}</description>
<guid>{id_item}</guid>
</item>
"""

# 5️⃣ Fin du RSS
xml += """
</channel>
</rss>
"""

# 6️⃣ Écriture dans cantine.xml
with open("cantine.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print("✅ RSS XML généré avec succès dans 'cantine.xml'")
