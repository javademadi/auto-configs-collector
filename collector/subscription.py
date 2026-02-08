import base64

def build_subscription(configs: list[str], output_path: str):
    unique = list(dict.fromkeys([c.strip() for c in configs if c.strip()]))
    merged = "\n".join(unique)
    encoded = base64.b64encode(merged.encode()).decode()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(encoded)
