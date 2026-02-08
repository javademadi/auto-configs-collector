from collector.fetcher import fetch_all
from collector.parser import parse_protocols
from collector.exporters import export_raw, export_protocols
from collector.subscription import build_subscription
from collector.country import tag_country
from collector.health import filter_alive
from collector.per_country import export_per_country
from collector.qrcode_gen import make_qr

import os

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    # 1. Fetch raw configs
    raw_configs = fetch_all()

    # 2. Save raw
    export_raw(raw_configs, f"{OUTPUT_DIR}/raw.txt")

    # 3. Parse by protocol
    protocols = parse_protocols(raw_configs)

    # 4. Tag country
    for proto in protocols:
        protocols[proto] = [tag_country(c) for c in protocols[proto]]

    # 5. Filter alive + latency sort
    for proto in protocols:
        protocols[proto] = filter_alive(protocols[proto])

    # 6. Export per-protocol lists
    export_protocols(protocols, OUTPUT_DIR)

    # 7. Merge all configs
    all_configs = (
        protocols.get("vmess", []) +
        protocols.get("vless", []) +
        protocols.get("trojan", []) +
        protocols.get("ss", [])
    )

    # 8. Build main subscription
    build_subscription(all_configs, f"{OUTPUT_DIR}/subscribe.txt")

    # 9. Build per-country subscriptions
    export_per_country(all_configs, OUTPUT_DIR)

    # 10. Generate QR code for main subscription
    with open(f"{OUTPUT_DIR}/subscribe.txt", "r", encoding="utf-8") as f:
        make_qr(f.read(), f"{OUTPUT_DIR}/subscribe_qr.png")

    print("✅ Collection completed successfully")
    print(f"Total configs: {len(all_configs)}")

if __name__ == "__main__":
    main()
