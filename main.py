from collector.telegram_web import fetch_from_channel
from collector.dedup import deduplicate
from collector.exporters import export_raw, export_protocols
from collector.extractors import split_by_protocol
import os

def main():
    with open("channels.txt", encoding="utf-8") as f:
        channels = [c.strip() for c in f if c.strip()]

    all_configs = []

    for ch in channels:
        all_configs.extend(fetch_from_channel(ch))

    all_configs = deduplicate(all_configs)

    os.makedirs("outputs", exist_ok=True)

    # raw
    export_raw(all_configs, "outputs/raw.txt")

    # split by protocol
    protocols = split_by_protocol(all_configs)

    # dedup again per protocol
    for k in protocols:
        protocols[k] = deduplicate(protocols[k])

    export_protocols(protocols)

    print("Summary:")
    for k, v in protocols.items():
        print(f"{k}: {len(v)}")

if __name__ == "__main__":
    main()
