from concurrent.futures import ThreadPoolExecutor, as_completed
from collector.parser import is_valid_structure
from collector.alive import is_alive_network


def _check_one(config, timeout):
    # مرحله ۱: تست ساختاری
    if not is_valid_structure(config):
        return None

    # مرحله ۲: تست شبکه
    if not is_alive_network(config, timeout):
        return None

    return config


def filter_alive_configs(
    configs,
    timeout=1.2,
    max_workers=20
):
    alive = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(_check_one, c, timeout)
            for c in configs
        ]

        for future in as_completed(futures):
            result = future.result()
            if result:
                alive.append(result)

    return alive
