from collector.telegram_web import fetch_from_channel
from collector.dedup import deduplicate
from collector.exporters import export_raw
import os

def main():
    with open("channels.txt", encoding="utf-8") as f:
        channels = [c.strip() for c in f if c.strip()]

    all_configs = []

    for ch in channels:
        all_configs.extend(fetch_from_channel(ch))

    all_configs = deduplicate(all_configs)

    os.makedirs("outputs", exist_ok=True)
    export_raw(all_configs, "outputs/raw.txt")

    print(f"Collected {len(all_configs)} configs")

if __name__ == "__main__":
    main()
