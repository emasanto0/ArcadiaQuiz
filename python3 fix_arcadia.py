“””
fix_arcadia.py
Esegui con: python3 fix_arcadia.py
Corregge il file index.html sostituendo il carattere … (ellissi unicode U+2026)
con i tre punti … necessari per il JavaScript (spread operator).
“””

import os

INPUT = “index.html”   # <– cambia il nome se il tuo file si chiama diversamente
OUTPUT = “index.html”  # sovrascrive lo stesso file

if not os.path.exists(INPUT):
print(f”❌ File ‘{INPUT}’ non trovato. Mettilo nella stessa cartella di questo script.”)
exit(1)

with open(INPUT, “r”, encoding=“utf-8”) as f:
content = f.read()

count = content.count(”…”)

if count == 0:
print(“✅ Nessun problema trovato — il file è già corretto.”)
exit(0)

fixed = content.replace(”…”, “…”)

with open(OUTPUT, “w”, encoding=“utf-8”) as f:
f.write(fixed)

print(f”✅ Corrette {count} occorrenze di ‘…’ → ‘…’”)
print(f”   File salvato: {OUTPUT}”)