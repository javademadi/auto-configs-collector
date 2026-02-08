import json

def build_singbox(vmess_links: list[str], out="outputs/singbox.json"):
    outbounds = []

    for i, _ in enumerate(vmess_links):
        outbounds.append({
            "type": "vmess",
            "tag": f"vmess-{i}",
            "server": "example.com",
            "server_port": 443,
            "uuid": "00000000-0000-0000-0000-000000000000",
            "security": "auto"
        })

    config = {
        "log": {"level": "info"},
        "outbounds": outbounds or [{"type": "direct", "tag": "direct"}]
    }

    with open(out, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
