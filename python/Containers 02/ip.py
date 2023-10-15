import requests


result = requests.get("https://api.ipify.org/?format=json").json()


print(result)
