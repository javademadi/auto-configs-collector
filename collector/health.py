from collector.latency import test_latency

def filter_alive(configs: list[str], max_latency=1500):
    alive = []
    for c in configs:
        latency = test_latency(c)
        if latency and latency < max_latency:
            alive.append(f"{c} ⏱{latency}ms")
    return alive
