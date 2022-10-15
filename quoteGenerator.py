import requests
import random

QUOTES_URL = "https://zenquotes.io/api/quotes"
quotes = []

def initialize_quotes():
    r = requests.get(url=QUOTES_URL)
    data = r.json()
    global quotes
    quotes = [{"q":q["q"], "a": q["a"]} for q in data]

def get_random_quote():
    return quotes[random.randint(0, len(quotes)-1)]

if __name__ == "__main__":
    initialize_quotes()
    print(quotes)
