import json
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

cookie='user_trace_token=20220804100029-7f8dc42b-2462-4d00-9829-5d640433620e; __lg_stoken__=9189062711e72be27f0aa05a5db3f4a816c5736824ee0c904e15a6fb953c8bfa4f8093bb0fba10067625df3bc37dd23f9b8a82574ede251ca8af84f34390838c1f614d514992; JSESSIONID=ABAAABAABAGABFA61C17486A7D7336A05E3A63C2F267C13; sajssdk_2015_cross_new_user=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1659578430; _ga=GA1.2.1618320529.1659578430; _gid=GA1.2.1916537438.1659578430; LGUID=20220804100031-e3b52082-bda1-4d0a-a0aa-81b0c81cdc89; gate_login_token=1c7fba76ab641259f64f59e98e78e0790b6b67b95d837968; LG_LOGIN_USER_ID=512ac42c1181881b79a827c8ecc697bbbf48a86cb224762a; LG_HAS_LOGIN=1; _putrc=4883EBF2E7179D45; login=true; unick=%E6%9D%8E%E7%BA%A2; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=8; WEBTJ-ID=20220804100531-1826699cabbdc-0fb8ab75dc178e-1c525635-2073600-1826699cabc58e; RECOMMEND_TIP=true; __SAFETY_CLOSE_TIME__3403370=1; privacyPolicyPopup=false; sensorsdata2015session=%7B%7D; index_location_city=%E5%85%A8%E5%9B%BD; X_MIDDLE_TOKEN=8c4ba18bbe5cb7421ab54fe0fcddd62d; _gat=1; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGSID=20220804151141-d126cbde-a73f-4d7f-89fe-81a802be568b; PRE_SITE=; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%223403370%22%2C%22%24device_id%22%3A%221826695311ab6a-002ff698b31b9a-1c525635-2073600-1826695311bacf%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22103.0.0.0%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22first_id%22%3A%221826695311ab6a-002ff698b31b9a-1c525635-2073600-1826695311bacf%22%7D; TG-TRACK-CODE=index_search; SEARCH_ID=0964f435c4934f3a80e9ade3df9c7398; X_HTTP_TOKEN=a895f502bce538cd41179595618f1e863aef3b9ce7; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1659597112; LGRID=20220804151155-292697d1-85cc-4c30-a24f-555378a5edac'


#定义抓取主函数
def lagou_dynamic_crawl():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?px=default&city=%E5%85%A8%E5%9B%BD',
        'X-Anit-Forge-Code':'0',
        'X-Anit-Forge-Token':None,
        'X-Requested-With':'XMLHttpRequest',
        'Cookie': cookie 
    }

    #创建一个职位列表容器
    positions = []
    #30页循环遍历抓取
    for page in range(1, 31):
        print('正在抓取第{}页...'.format(page))
        #构建请求表单参数
        params = {
            'first':'true',
            'pn':page,
            'kd':'数据挖掘'
        }

        #构造请求并返回结果
        result = requests.post('https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false',
                                headers=headers, data=params)
        #将请求结果转为json
        json_result = result.json()
        #解析json数据结构获取目标信息
        position_info = json_result['content']['positionResult']['result']
        #循环当前页每一个职位信息，再去爬职位详情页面
        for position in position_info:
            #把我们要爬取信息放入字典
            position_dict = {
                'position_name':position['positionName'],
                'work_year':position['workYear'],
                'education':position['education'],
                'salary':position['salary'],
                'city':position['city'],
                'company_name':position['companyFullName'],
                'address':position['businessZones'],
                'label':position['companyLabelList'],
                'stage':position['financeStage'],
                'size':position['companySize'],
                'advantage':position['positionAdvantage'],
                'industry':position['industryField'],
                'industryLables':position['industryLables']
            }
            #找到职位 ID
            position_id = position['positionId']
            #根据职位ID调用岗位描述函数获取职位JD
            position_dict['position_detail'] = recruit_detail(position_id)
            positions.append(position_dict)

        time.sleep(4)
    print('全部数据采集完毕。')
    return positions


#定义抓取岗位描述函数
def recruit_detail(position_id):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?labelWords=&fromSearch=true&suginput=',
        'Upgrade-Insecure-Requests':'1',
        'Cookie': cookie
    }
    url = 'https://www.lagou.com/jobs/%s.html' % position_id
    result = requests.get(url, headers=headers)
    time.sleep(5)
    #解析职位要求text
    soup = BeautifulSoup(result.text, 'html.parser')
    job_jd = soup.find(class_="job_bt")

    #通过尝试发现部分记录描述存在空的情况
    #所以这里需要判断处理一下
    if job_jd != None:
        job_jd = job_jd.text
    else:
        job_jd = 'null'
    return job_jd


if __name__ == '__main__':
    positions = lagou_dynamic_crawl()
    data = pd.DataFrame(positions)
    data.to_csv('data_mining_job.csv')
