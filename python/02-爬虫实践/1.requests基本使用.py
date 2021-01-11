import requests

url ='https://www.baidu.com/'

r = requests.get(url=url)

#print(r)  # <Response [200]>

# print(r.status_code) # 请求状态码 200

# print(r.content) # 二进制文本流

# print(r.content.decode('utf-8')) # 把二进制文本流按照utf-8 字符集转化为普通字符串

# print(r.text) # 获取响应的内容

# print(r.url) # 获取请求的地址

# print(r.request.headers) # 请求的头信息  {'User-Agent': 'python-requests/2.24.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

print(r.headers) # 响应头信息 

# {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Thu, 22 Oct 2020 05:41:36 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:23:55 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}


