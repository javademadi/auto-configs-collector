import requests

def fetch_all():
    texts = []

    with open("channels.txt", "r", encoding="utf-8") as f:
        sources = [l.strip() for l in f if l.strip()]

    for url in sources:
        print("Fetching:", url)
        try:
            r = requests.get(url, timeout=15)
            texts.append(r.text)
        except Exception as e:
            print("Failed:", url, e)

    return texts
