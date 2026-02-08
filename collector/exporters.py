def export_raw(configs: list[str], path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(configs))
