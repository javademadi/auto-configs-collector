def deduplicate(items: list[str]) -> list[str]:
    seen = set()
    result = []
    for i in items:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result
