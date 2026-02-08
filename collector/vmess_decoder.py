import base64
import json

def decode_vmess(vmess_link: str) -> dict | None:
    try:
        raw = vmess_link.replace("vmess://", "")
        padded = raw + "=" * (-len(raw) % 4)
        decoded = base64.b64decode(padded).decode("utf-8")
        data = json.loads(decoded)
        return data
    except Exception:
        return None


def normalize_vmess(data: dict, index: int) -> str:
    data["ps"] = f"vmess-{index}"
    encoded = base64.b64encode(json.dumps(data, ensure_ascii=False).encode()).decode()
    return "vmess://" + encoded
