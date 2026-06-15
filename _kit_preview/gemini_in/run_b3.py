import json
from gen_b3 import get_b3

with open("gen_b3.json", "w", encoding="utf-8") as f:
    json.dump(get_b3(), f, ensure_ascii=False, indent=2)
