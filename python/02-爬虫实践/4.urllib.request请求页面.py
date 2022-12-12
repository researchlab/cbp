import urllib.request 

url = "https://www.python.org/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)
print(response.geturl())
print(response.info())
### 打印请求状态码
print(response.getcode())
print(type(response))
