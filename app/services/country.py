import pycountry

def extract_countries(text: str) -> list:
    country_names = [country.name.lower() for country in pycountry.countries]
    mentioned = [name.title() for name in country_names if name in text.lower()]
    return sorted(set(mentioned))
