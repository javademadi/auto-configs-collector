from collector.telegram_web import fetch_from_channel
from collector.dedup import deduplicate
from collector.exporters import export_raw, export_clash, export_singbox
from collector.alive_filter import filter_alive_configs


MAX_CONFIGS_PER_CHANNEL = 40
MAX_TOTAL_CONFIGS = 900
ENABLE_ALIVE_CHECK = True


def main():
    with open("channels.txt", encoding="utf-8") as f:
        channels = [line.strip() for line in f if line.strip()]

    configs = []

    for ch in channels:
        try:
            channel_configs = fetch_from_channel(
                ch,
                max_configs=MAX_CONFIGS_PER_CHANNEL
            )
            configs.extend(channel_configs)
        except Exception:
            continue

    # حذف تکراری
    configs = deduplicate(configs)

    # تست alive (روش ۱ + ۲)
    if ENABLE_ALIVE_CHECK:
        configs = filter_alive_configs(configs, timeout=1.2)

    # محدودسازی خروجی
    configs = configs[:MAX_TOTAL_CONFIGS]

    export_raw(configs, "outputs/raw.txt")
    export_clash(configs, "outputs/clash.yaml")
    export_singbox(configs, "outputs/sing-box.json")

    print(f"Collected {len(configs)} alive configs")


if __name__ == "__main__":
    main()
