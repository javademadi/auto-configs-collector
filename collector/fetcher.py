import requests
import re

# اینجا لینک منبع/کانال/ریپوهایی که قبلاً داشتی
SOURCES = [
    # مثال — اگر خودت لینک داری، اینها را نگه دار یا جایگزین کن
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge.txt",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_all():
    configs = []

    for url in SOURCES:
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            if r.status_code != 200:
                continue

            text = r.text.strip()

            # اگر base64 بود decode کن
            if is_base64(text):
                text = decode_base64(text)

            for line in text.splitlines():
                line = line.strip()
                if is_valid_config(line):
                    configs.append(line)

        except Exception:
            continue

    return configs


def is_valid_config(line: str) -> bool:
    return line.startswith((
        "vmess://",
        "vless://",
        "trojan://",
        "ss://"
    ))


def is_base64(s: str) -> bool:
    return re.fullmatch(r"[A-Za-z0-9+/=\s]+", s or "") is not None


def decode_base64(s: str) -> str:
    import base64
    try:
        return base64.b64decode(s).decode(errors="ignore")
    except Exception:
        return ""
