from collector.fetcher import fetch_all
from collector.parser import parse_protocols
import os

OUTPUT_DIR = "outputs"
RAW_FILE = f"{OUTPUT_DIR}/raw.txt"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Fetching sources...")
    texts = fetch_all()

    print("Parsing configs...")
    protocols = parse_protocols(texts)

    all_configs = []
    for items in protocols.values():
        all_configs.extend(items)

    all_configs = sorted(set(all_configs))

    with open(RAW_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(all_configs))

    print(f"Done. Total configs: {len(all_configs)}")

if __name__ == "__main__":
    main()
