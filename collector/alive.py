import socket
from urllib.parse import urlparse


def is_alive_network(config: str, timeout=1.2) -> bool:
    try:
        url = urlparse(config)
        host = url.hostname
        port = url.port

        if not host or not port:
            return False

        socket.gethostbyname(host)

        with socket.create_connection((host, port), timeout=timeout):
            return True

    except Exception:
        return False
