import socket
import time
import re

TIMEOUT = 2

def extract_host_port(config: str):
    match = re.search(r"@(.+?):(\d+)", config)
    if not match:
        return None, None
    return match.group(1), int(match.group(2))

def test_latency(config: str):
    host, port = extract_host_port(config)
    if not host:
        return None

    start = time.time()
    try:
        sock = socket.create_connection((host, port), timeout=TIMEOUT)
        sock.close()
        return int((time.time() - start) * 1000)
    except:
        return None
