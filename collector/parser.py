from collections import defaultdict

def parse_protocols(configs: list[str]) -> dict:
    """
    Split configs by protocol
    """
    protocols = defaultdict(list)

    for c in configs:
        c = c.strip()
        if not c:
            continue

        if c.startswith("vmess://"):
            protocols["vmess"].append(c)
        elif c.startswith("vless://"):
            protocols["vless"].append(c)
        elif c.startswith("trojan://"):
            protocols["trojan"].append(c)
        elif c.startswith("ss://"):
            protocols["ss"].append(c)

    return protocols

