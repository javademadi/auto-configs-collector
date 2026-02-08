from collector.telegram_web import fetch_from_channel
from collector.dedup import deduplicate
from collector.extractors import split_by_protocol
from collector.exporters import export_raw, export_protocols
from collector.vmess_decoder import decode_vmess, normalize_vmess
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

    protocols = split_by_protocol(all_configs)

    # decode + normalize vmess
    normalized_vmess = []
    for i, vm in enumerate(protocols["vmess"]):
        data = decode_vmess(vm)
        if data:
            normalized_vmess.append(normalize_vmess(data, i))

    protocols["vmess"] = normalized_vmess

    export_protocols(protocols)

    print("Summary:")
    for k, v in protocols.items():
        print(f"{k}: {len(v)}")

if __name__ == "__main__":
    main()
