from collector.telegram_web import fetch_from_channel
from collector.dedup import deduplicate
from collector.extractors import split_by_protocol
from collector.exporters import export_raw, export_protocols
from collector.vmess_decoder import decode_vmess, normalize_vmess
from collector.clash_builder import build_clash
from collector.singbox_builder import build_singbox
from collector.subscription import build_subscription
from collector.clash import export_clash
from collector.singbox import export_singbox
from collector.country import tag_country
from collector.health import filter_alive
from collector.per_country import export_per_country











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

    vmess_norm = []
    for i, vm in enumerate(protocols["vmess"]):
        data = decode_vmess(vm)
        if data:
            vmess_norm.append(normalize_vmess(data, i))

    protocols["vmess"] = vmess_norm
    for k in protocols:
        protocols[k] = [tag_country(c) for c in protocols[k]]
        
    export_protocols(protocols)

    build_clash(vmess_norm)
    build_singbox(vmess_norm)
    export_clash(all_configs, "outputs/clash.yaml")
    export_singbox(all_configs, "outputs/singbox.json")

    print("=== SUMMARY ===")
    for k, v in protocols.items():
        print(f"{k}: {len(v)}")

    all_configs = (
        protocols["vmess"]
        + protocols["vless"]
        + protocols["trojan"]
        + protocols["ss"]
    )
    for k in protocols:
        protocols[k] = filter_alive(protocols[k])
    build_subscription(all_configs, "outputs/subscribe.txt")
    export_per_country(all_configs)

if __name__ == "__main__":
    main()
