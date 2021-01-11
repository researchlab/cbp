
import requests

# url = 'https://www.lmonkey.com/'

url = 'https://www.xicidaili.com/nn'

#定义请求头信息
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

r = requests.get(url=url,headers=headers)

code = r.status_code 

print(code)

if code == 200:
    with open('./test.html','w') as fp:   #写入文件
        fp.write(r.text)