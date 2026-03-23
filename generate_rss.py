import requests
from bs4 import BeautifulSoup

url = "https://cantine-rapide-go.base44.app/rss"

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

items = soup.find_all("item")

xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Ordre du Self</title>
<link>https://cantine-rapide-go.base44.app</link>
<description>Ordre de passage</description>
"""

for item in items:
    xml += str(item)

xml += "</channel></rss>"

with open("cantine.xml", "w", encoding="utf-8") as f:
    f.write(xml)
