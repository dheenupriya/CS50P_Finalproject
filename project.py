# Project: Caller Tune
# Supported for few Countries: India, Japan, US, Korean, Singapore

import random
import re
import webbrowser
import cowsay
import requests


class Caller:

    def __init__(self, mobileno):
        self.mobileno = mobileno

COUNTRY_PATTERNS = {
    "91": r"^\+91[6-9][0-9]{9}$",
    "81": r"^\+81(70|80|90)[0-9]{8}$",
    "1": r"^\+1[0-9]{10}$",
    "82": r"^\+8210[0-9]{7,8}$",
    "65": r"^\+65[89][0-9]{7}$"
}

def main():
    while True:
        cowsay.kitty("Enter your mobile number: ")
        mobileno = input("> ")
        mobileno = mobileno.strip().replace(" ","").replace("-","")
        caller = Caller(mobileno)
        if is_mobile_no(caller.mobileno):
            countryCode = extract_country_code(caller.mobileno)
            if countryCode:
                break
            else:
                cowsay.dragon("Country code not found. Please enter a valid mobile number with country code.")
        else:
            cowsay.dragon("Enter a valid MOBILE NUMBER !!!")
    country = find_the_country(countryCode)
    play_country_music(country)


def is_mobile_no(number):
    for pattern in COUNTRY_PATTERNS.values():
        if re.match(pattern, number):
            return True
    return False

def extract_country_code(number):
    for code in COUNTRY_PATTERNS:
        if number.startswith("+" + code):
            return code
    return None

def find_the_country(countryCode):
    country_codes = {
        "91": "IN",
        "81": "JP",
        "1": "US",
        "82": "KR",
        "65": "SG"
    }

    return country_codes.get(countryCode)

def play_country_music(country):
    try:
        if country not in ["IN", "JP", "US", "KR", "SG"]:
            raise Exception("Unsupported country")

        url = "https://itunes.apple.com/search"
        params = {
            "term": "music",
            "country": country,
            "media": "music",
            "limit": 10
        }
        response = requests.get(url, params=params)
        data = response.json()
        if not data.get("results"):
            cowsay.dragon("No music found for this country.")
            return
        song = random.choice(data["results"])
        cowsay.kitty(f"Playing {song['trackName']} by {song['artistName']} from {country}!")
        url = song['previewUrl']
        if url:
            webbrowser.open(url)
        else:
            cowsay.dragon("Sorry, no preview available for this song.")
    except Exception as e:
        cowsay.dragon(str(e))
        raise


if __name__ == "__main__":
    main()
