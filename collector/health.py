from collector.latency import test_latency

def filter_alive(configs: list[str], max_latency=1500):
    alive = []
    for c in configs:
        latency = test_latency(c)
        if latency and latency < max_latency:
            alive.append((latency, f"{c} ⏱{latency}ms"))
    alive.sort(key=lambda x: x[0])
    return [c for _, c in alive]
