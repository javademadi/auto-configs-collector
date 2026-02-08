import os
import json
import base64

def export_raw(configs: list[str], path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(configs))


def write_list(items: list[str], path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(items))


def export_protocols(data: dict, base_dir="outputs"):
    write_list(data.get("vmess", []), f"{base_dir}/vmess.txt")
    write_list(data.get("vless", []), f"{base_dir}/vless.txt")
    write_list(data.get("trojan", []), f"{base_dir}/trojan.txt")
    write_list(data.get("ss", []), f"{base_dir}/ss.txt")
