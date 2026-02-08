import base64
import re

def export_per_country(configs, output_dir="outputs"):
    buckets = {}

    for c in configs:
        m = re.search(r"#(.+)$", c)
        country = m.group(1).replace(" ", "_") if m else "Unknown"
        buckets.setdefault(country, []).append(c)

    for country, items in buckets.items():
        encoded = base64.b64encode("\n".join(items).encode()).decode()
        with open(f"{output_dir}/subscribe_{country}.txt","w",encoding="utf-8") as f:
            f.write(encoded)
