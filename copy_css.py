import os
import re

base_dir = r"c:\Users\User\.gemini\antigravity\scratch\biblioteca\print"
master_file = os.path.join(base_dir, "00_visao_geral.html")

with open(master_file, "r", encoding="utf-8") as f:
    master_content = f.read()

style_match = re.search(r"<style>.*?</style>", master_content, re.DOTALL)
if not style_match:
    print("Style block not found in master")
    exit(1)

new_style = style_match.group(0)

for filename in os.listdir(base_dir):
    if filename.endswith(".html") and filename != "00_visao_geral.html":
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        updated_content = re.sub(r"<style>.*?</style>", new_style, content, flags=re.DOTALL)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"Updated {filename}")
