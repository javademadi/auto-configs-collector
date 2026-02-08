import requests
import re

PATTERN = re.compile(
    r'(vmess://[^\s<]+|vless://[^\s<]+|trojan://[^\s<]+|ss://[^\s<]+)'
)

def fetch_from_channel(url: str) -> list[str]:
    try:
        res = requests.get(url, timeout=20)
        if res.status_code != 200:
            return []
        return PATTERN.findall(res.text)
    except Exception:
        return []
