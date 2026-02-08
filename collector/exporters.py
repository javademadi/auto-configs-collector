import os

def export_raw(configs: list[str], path: str):
    if not configs:
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(configs))


def write_list(items: list[str], path: str):
    if not items:
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(items))


def export_protocols(data: dict, base_dir="outputs"):
    os.makedirs(base_dir, exist_ok=True)

    write_list(data.get("vmess", []), f"{base_dir}/vmess.txt")
    write_list(data.get("vless", []), f"{base_dir}/vless.txt")
    write_list(data.get("trojan", []), f"{base_dir}/trojan.txt")
    write_list(data.get("ss", []), f"{base_dir}/ss.txt")
