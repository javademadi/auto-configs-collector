import re

COUNTRIES = {
    "de": "🇩🇪 Germany",
    "nl": "🇳🇱 Netherlands",
    "fr": "🇫🇷 France",
    "us": "🇺🇸 USA",
    "uk": "🇬🇧 UK",
    "tr": "🇹🇷 Turkey",
}

def tag_country(config: str) -> str:
    lower = config.lower()
    for key, name in COUNTRIES.items():
        if re.search(rf"{key}", lower):
            return f"{config} #{name}"
    return f"{config} #🌐 Unknown"
