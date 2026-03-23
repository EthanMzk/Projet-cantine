import requests

url = "https://qtrypzzcjebvfcihiynt.supabase.co/rest/v1/ordre"

headers = {
    "apikey": "TA_SUPABASE_KEY",
    "Authorization": "Bearer TA_SUPABASE_KEY"
}

data = requests.get(url, headers=headers).json()

xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Ordre du Self</title>
<description>Ordre de passage</description>
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

xml += "</channel></rss>"

with open("cantine.xml", "w", encoding="utf-8") as f:
    f.write(xml)
