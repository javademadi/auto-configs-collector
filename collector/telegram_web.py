import requests
import re
from bs4 import BeautifulSoup

PATTERN = re.compile(
    r'(vmess://[^\s"<]+|vless://[^\s"<]+|trojan://[^\s"<]+|ss://[^\s"<]+)'
)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_from_channel(url: str) -> list[str]:
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        if r.status_code != 200:
            return []

        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text(separator=" ")

        return PATTERN.findall(text)
    except Exception:
        return []
