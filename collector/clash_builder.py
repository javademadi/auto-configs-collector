import yaml

def build_clash(vmess_links: list[str], out="outputs/clash.yaml"):
    proxies = []

    for i, link in enumerate(vmess_links):
        proxies.append({
            "name": f"vmess-{i}",
            "type": "vmess",
            "server": "example.com",
            "port": 443,
            "uuid": "00000000-0000-0000-0000-000000000000",
            "alterId": 0,
            "cipher": "auto",
            "tls": True
        })

    config = {
        "port": 7890,
        "socks-port": 7891,
        "mode": "rule",
        "proxies": proxies,
        "proxy-groups": [{
            "name": "AUTO",
            "type": "select",
            "proxies": [p["name"] for p in proxies]
        }],
        "rules": ["MATCH,AUTO"]
    }

    with open(out, "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True)
