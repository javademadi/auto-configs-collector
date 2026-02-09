from collector.latency import test_latency

MAX_TEST = 120      # حداکثر تست
MAX_LATENCY = 1500 # ms

def filter_alive(configs: list[str]):
    alive = []
    tested = 0

    for c in configs:
        if tested >= MAX_TEST:
            break

        latency = test_latency(c)
        tested += 1

        if latency and latency < MAX_LATENCY:
            alive.append((latency, f"{c} ⏱{latency}ms"))

    alive.sort(key=lambda x: x[0])
    return [c for _, c in alive]
