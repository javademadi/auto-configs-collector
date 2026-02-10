from collector.telegram_web import fetch_from_channel
from collector.dedup import deduplicate
from collector.exporters import export_raw, export_clash, export_singbox


# حداکثر تعداد کانفیگ از هر کانال
MAX_CONFIGS_PER_CHANNEL = 40

# حداکثر تعداد کل کانفیگ خروجی
MAX_TOTAL_CONFIGS = 1000


def main():
    # خواندن لیست کانال‌ها
    with open("channels.txt", encoding="utf-8") as f:
        channels = [line.strip() for line in f if line.strip()]

    configs = []

    # جمع‌آوری کانفیگ‌ها
    for ch in channels:
        try:
            channel_configs = fetch_from_channel(
                ch,
                max_configs=MAX_CONFIGS_PER_CHANNEL
            )
            configs.extend(channel_configs)
        except Exception:
            # اگر یک کانال مشکل داشت، کل برنامه نخوابه
            continue

    # حذف کانفیگ‌های تکراری (ترتیب حفظ می‌شود)
    configs = deduplicate(configs)

    # محدود کردن حجم خروجی نهایی
    configs = configs[:MAX_TOTAL_CONFIGS]

    # خروجی‌ها
    export_raw(configs, "outputs/raw.txt")
    export_clash(configs, "outputs/clash.yaml")
    export_singbox(configs, "outputs/sing-box.json")

    print(f"Collected {len(configs)} configs")


if __name__ == "__main__":
    main()
