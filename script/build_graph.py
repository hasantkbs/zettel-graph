import os
import re
import json

# 🔁 Klasörleri otomatik olarak belirle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(BASE_DIR, "notes")
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "graph.json")

nodes = []
edges = []
seen = set()

# 🔍 Notları oku
for filename in os.listdir(NOTES_DIR):
    if not filename.endswith(".md"):
        continue
    note_id = filename.replace(".md", "")
    nodes.append({"id": note_id, "label": note_id})
    seen.add(note_id)

# 🔗 Bağlantıları tara
for filename in os.listdir(NOTES_DIR):
    if not filename.endswith(".md"):
        continue
    note_id = filename.replace(".md", "")
    with open(os.path.join(NOTES_DIR, filename), 'r') as f:
        content = f.read()
    links = re.findall(r'\[\[([^\[\]]+)\]\]', content)
    for link in links:
        if link in seen:
            edges.append({"source": note_id, "target": link})

graph_data = {"nodes": nodes, "links": edges}

# 💾 JSON dosyasını oluştur
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, "w") as f:
    json.dump(graph_data, f, indent=2)

print("✅ Graph JSON created at", OUTPUT_FILE)
