from collector.parser import is_valid_structure
from collector.alive import is_alive_network


def filter_alive_configs(configs, timeout=1.5):
    alive = []

    for c in configs:
        # مرحله ۱: تست ساختاری
        if not is_valid_structure(c):
            continue

        # مرحله ۲: تست شبکه
        if not is_alive_network(c, timeout=timeout):
            continue

        alive.append(c)

    return alive
