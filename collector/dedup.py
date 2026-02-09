def deduplicate(configs: list[str]) -> list[str]:
    return list(dict.fromkeys(configs))
