import requests

url = "https://raw.githubusercontent.com/ASHINI04/Hello-python/main/hello.py"
response = requests.get(url)

print(response.text)
