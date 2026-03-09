import requests
import xml.etree.ElementTree as ET

url = "https://cantine-rapide-go.base44.app/rss"
response = requests.get(url)
content = response.text

# Vérifier si <rss> est dans le contenu
if "<rss>" not in content:
    print("Flux Base44 détecté comme texte, création RSS manuel...")
    
    # Exemple minimal : on crée un RSS simple
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    title = ET.SubElement(channel, "title")
    title.text = "Flux Base44"
    
    # Chaque ligne comme item
    for line in content.splitlines():
        line = line.strip()
        if line:
            item = ET.SubElement(channel, "item")
            item_title = ET.SubElement(item, "title")
            item_title.text = line
    
    tree = ET.ElementTree(rss)
    tree.write("rss_base44.xml", encoding="utf-8", xml_declaration=True)
else:
    # Traitement XML normal
    tree = ET.ElementTree(ET.fromstring(content))
    tree.write("rss_base44.xml", encoding="utf-8", xml_declaration=True)
