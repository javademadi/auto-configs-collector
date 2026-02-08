import os
from datetime import datetime

STAMP = f"# generated at {datetime.utcnow().isoformat()}"

def write_file(path: str, lines: list[str]):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(STAMP + "\n")
        if lines:
            f.write("\n".join(lines))
        else:
            f.write("# empty\n")


def export_raw(configs: list[str], path: str):
    write_file(path, configs)


def export_protocols(data: dict, base_dir="outputs"):
    write_file(f"{base_dir}/vmess.txt", data.get("vmess", []))
    write_file(f"{base_dir}/vless.txt", data.get("vless", []))
    write_file(f"{base_dir}/trojan.txt", data.get("trojan", []))
    write_file(f"{base_dir}/ss.txt", data.get("ss", []))
