def split_by_protocol(configs: list[str]) -> dict:
    result = {
        "vmess": [],
        "vless": [],
        "trojan": [],
        "ss": [],
    }

    for c in configs:
        c = c.strip()
        if c.startswith("vmess://"):
            result["vmess"].append(c)
        elif c.startswith("vless://"):
            result["vless"].append(c)
        elif c.startswith("trojan://"):
            result["trojan"].append(c)
        elif c.startswith("ss://"):
            result["ss"].append(c)

    return result
