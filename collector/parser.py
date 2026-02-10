import base64
import json
from urllib.parse import urlparse


def is_valid_structure(config: str) -> bool:
    try:
        if config.startswith("vmess://"):
            payload = config.replace("vmess://", "")
            decoded = base64.b64decode(payload + "==").decode("utf-8")
            data = json.loads(decoded)

            return bool(
                data.get("add")
                and data.get("port")
                and data.get("id")
            )

        elif config.startswith(("vless://", "trojan://", "ss://")):
            url = urlparse(config)
            return bool(url.hostname and url.port)

        return False

    except Exception:
        return False
