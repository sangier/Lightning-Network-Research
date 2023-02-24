import requests

page = requests.get("https://1ml.com/testnet/")
page

print(page.status_code)
print(page.content)