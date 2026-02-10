import requests
import re

PATTERN = re.compile(
    r'(vmess://[^\s<]+|vless://[^\s<]+|trojan://[^\s<]+|ss://[^\s<]+)'
)

MAX_HTML_SIZE = 120_000

def fetch_from_channel(url: str, max_configs=40) -> list[str]:
    try:
        res = requests.get(url, timeout=20)
        if res.status_code != 200:
            return []

        html = res.text[:MAX_HTML_SIZE]
        configs = PATTERN.findall(html)

        return configs[:max_configs]

    except Exception:
        return []
