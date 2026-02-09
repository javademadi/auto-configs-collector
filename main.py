from collector.telegram_web import fetch_from_channel
from collector.dedup import deduplicate
from collector.exporters import export_raw, export_clash, export_singbox

def main():
    with open("channels.txt", encoding="utf-8") as f:
        channels = [line.strip() for line in f if line.strip()]

    configs = []
    for ch in channels:
        configs.extend(fetch_from_channel(ch))

    configs = deduplicate(configs)

    export_raw(configs, "outputs/raw.txt")
    export_clash(configs, "outputs/clash.yaml")
    export_singbox(configs, "outputs/sing-box.json")

    print(f"Collected {len(configs)} configs")

if __name__ == "__main__":
    main()
