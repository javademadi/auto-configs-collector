import re

COUNTRIES = {
    # Europe
    "de": "🇩🇪 Germany",
    "nl": "🇳🇱 Netherlands",
    "fr": "🇫🇷 France",
    "uk": "🇬🇧 United Kingdom",
    "gb": "🇬🇧 United Kingdom",
    "it": "🇮🇹 Italy",
    "es": "🇪🇸 Spain",
    "se": "🇸🇪 Sweden",
    "fi": "🇫🇮 Finland",
    "no": "🇳🇴 Norway",
    "ch": "🇨🇭 Switzerland",
    "pl": "🇵🇱 Poland",
    "ro": "🇷🇴 Romania",
    "cz": "🇨🇿 Czech",
    "at": "🇦🇹 Austria",

    # America
    "us": "🇺🇸 USA",
    "ca": "🇨🇦 Canada",
    "br": "🇧🇷 Brazil",

    # Asia
    "jp": "🇯🇵 Japan",
    "kr": "🇰🇷 South Korea",
    "sg": "🇸🇬 Singapore",
    "hk": "🇭🇰 Hong Kong",
    "tw": "🇹🇼 Taiwan",
    "in": "🇮🇳 India",

    # Middle East
    "tr": "🇹🇷 Turkey",
    "ae": "🇦🇪 UAE",
    "ir": "🇮🇷 Iran",

    # Others
    "au": "🇦🇺 Australia",
    "ru": "🇷🇺 Russia",
}

def tag_country(config: str) -> str:
    lower = config.lower()
    for key, name in COUNTRIES.items():
        if re.search(rf"[\W_]{key}[\W_]", f"_{lower}_"):
            return f"{config} #{name}"
    return f"{config} #🌐 Unknown"
