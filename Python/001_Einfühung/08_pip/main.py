import requests

response = requests.get("https://google.de")

if response.status_code != 200:
    print("Das hat leider nicht geklappt. Statuscode ist", response.status_code)
    exit()

print(response.text)

