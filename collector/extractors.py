import re

def clean_link(link: str) -> str:
    return link.strip().replace("\u200b", "").replace("\n", "")


def split_by_protocol(configs: list[str]) -> dict:
    result = {
        "vmess": [],
        "vless": [],
        "trojan": [],
        "ss": [],
    }

    for c in configs:
        c = clean_link(c)

        if c.startswith("vmess://"):
            result["vmess"].append(c)
        elif c.startswith("vless://"):
            result["vless"].append(c)
        elif c.startswith("trojan://"):
            result["trojan"].append(c)
        elif c.startswith("ss://"):
            result["ss"].append(c)

    return result
