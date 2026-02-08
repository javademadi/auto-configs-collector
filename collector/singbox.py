import json

def export_singbox(configs, path):
    data = {
        "log": {"level": "warn"},
        "outbounds": configs
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
