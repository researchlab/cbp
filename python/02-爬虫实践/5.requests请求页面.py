import requests 
res = requests.get('https://www.python.org/')
print(res.status_code)
print(res.text)
# print(res.content)
