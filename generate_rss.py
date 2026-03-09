import requests

url = "https://qtrypzzcjebvfcihiynt.supabase.co/storage/v1"

data = requests.get(url).json()

xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Ordre du Self</title>
<description>Ordre de passage en temps réel</description>
<link>https://cantine-rapide-go.base44.app</link>
"""

for item in data:
    xml += f"""
<item>
<title>{item['ordre']} - {item['classe']}</title>
<description>{item['statut']}</description>
<guid>{item['id']}</guid>
</item>
"""

xml += """
</channel>
</rss>
"""

with open("cantine.xml", "w", encoding="utf-8") as f:
    f.write(xml)
