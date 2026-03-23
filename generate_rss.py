import requests

APP_ID = "69a563ac3aae8ad0e6d45ec7"

url = f"https://app.base44.com/api/apps/{APP_ID}/entities"

headers = {
    "Content-Type": "application/json"
}

data = requests.get(url, headers=headers).json()

xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Ordre du Self</title>
"""

for item in data:
    xml += f"""
<item>
<title>{item['ordre']} - {item['classe']}</title>
<description>{item['statut']}</description>
</item>
"""

xml += "</channel></rss>"

with open("cantine.xml", "w", encoding="utf-8") as f:
    f.write(xml)
