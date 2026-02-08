import yaml
import json

def export_raw(configs, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(configs))


def export_clash(configs, path):
    data = {
        "proxies": [{"name": f"node-{i}", "type": "vmess", "server": "example.com"} for i, _ in enumerate(configs)]
    }
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)


def export_singbox(configs, path):
    data = {
        "outbounds": [{"type": "vmess", "tag": f"node-{i}"} for i, _ in enumerate(configs)]
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
