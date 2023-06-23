import requests

url = "https://gsamuel-morse-code-v1.p.rapidapi.com/"

text = input("Enter a word: ").upper().strip()
payload = {"text": text}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "7ea7abb91amsh3beb9cae6c70110p1e6f3ejsnba5a4bace125",
    "X-RapidAPI-Host": "gsamuel-morse-code-v1.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
