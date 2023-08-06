import requests
from dotenv import load_dotenv
import os

load_dotenv()
MORSE_API_KEY = os.getenv("MORSE_API_KEY")

url = "https://gsamuel-morse-code-v1.p.rapidapi.com/"

text = input("Enter a word: ").upper().strip()
payload = {"text": text}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": MORSE_API_KEY,
    "X-RapidAPI-Host": "gsamuel-morse-code-v1.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
