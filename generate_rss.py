import requests

# 1️⃣ URL de l'API Base44
url = "https://cantine-rapide-go.base44.app/api/apps/69a563ac3aae8ad0e6d45ec7/entities/Classe?sort=ordre"

# 2️⃣ Récupération des données JSON
data = requests.get(url).json()

# 3️⃣ Début du RSS
xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Ordre du Self</title>
<link>https://cantine-rapide-go.base44.app</link>
<description>Ordre de passage en temps réel</description>
"""

# 4️⃣ Génération des items
for item in data:
    # Détecte automatiquement les champs (nom de la classe, statut, id)
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

# 5️⃣ Fin du RSS
xml += """
</channel>
</rss>
"""

# 6️⃣ Écriture dans cantine.xml
with open("cantine.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print("RSS XML généré avec succès !")
