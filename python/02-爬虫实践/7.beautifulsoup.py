import requests 
import pandas as pd
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
url='https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=0&limit=20&strategy=1&ext={%22pool%22:[%22top%22],%22is_filter%22:7,%22check_type%22:true}'
res = requests.get(url, headers=headers)
#print(res.json())
datas = res.json()['data']['list']
data_list = []
for i in datas:
    data_dict={}
    data_dict['标题'] = i['title']
    data_dict['分类']=i['category_cn']
    data_dict['网址'] =i['url']
    data_list.append(data_dict)

df = pd.DataFrame(data_list)
print(df)

