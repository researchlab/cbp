import requests 
from lxml import etree
import pandas as pd 
from time import sleep
import random 

# cookie 
cookie='user_trace_token=20220804100029-7f8dc42b-2462-4d00-9829-5d640433620e;__lg_stoken__=9189062711e72be27f0aa05a5db3f4a816c5736824ee0c904e15a6fb953c8bfa4f8093bb0fba10067625df3bc37dd23f9b8a82574ede251ca8af84f34390838c1f614d514992;JSESSIONID=ABAAABAABAGABFA61C17486A7D7336A05E3A63C2F267C13;sajssdk_2015_cross_new_user=1;Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1659578430;_ga=GA1.2.1618320529.1659578430; _gid=GA1.2.1916537438.1659578430;LGUID=20220804100031-e3b52082-bda1-4d0a-a0aa-81b0c81cdc89;gate_login_token=1c7fba76ab641259f64f59e98e78e0790b6b67b95d837968;LG_LOGIN_USER_ID=512ac42c1181881b79a827c8ecc697bbbf48a86cb224762a;LG_HAS_LOGIN=1; _putrc=4883EBF2E7179D45; login=true; unick=%E6%9D%8E%E7%BA%A2;showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1;hasDeliver=8;WEBTJ-ID=20220804100531-1826699cabbdc-0fb8ab75dc178e-1c525635-2073600-1826699cabc58e;RECOMMEND_TIP=true; __SAFETY_CLOSE_TIME__3403370=1; privacyPolicyPopup=false;sensorsdata2015session=%7B%7D; TG-TRACK-CODE=index_navigation;index_location_city=%E5%85%A8%E5%9B%BD;LGSID=20220804140358-b080b4e3-44a8-44ad-bba1-079fdab6ccb0; PRE_UTM=; PRE_HOST=;PRE_SITE=https%3A%2F%2Fwww.lagou.com; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F;X_MIDDLE_TOKEN=8c4ba18bbe5cb7421ab54fe0fcddd62d;SEARCH_ID=6e01594c19d9432dbffd6fb85fc03c15;X_HTTP_TOKEN=a895f502bce538cd41839595618f1e863aef3b9ce7;Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1659594010; _gat=1;LGRID=20220804142012-c0fe27aa-715a-4949-99ab-bf10413206c4;sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%223403370%22%2C%22%24device_id%22%3A%221826695311ab6a-002ff698b31b9a-1c525635-2073600-1826695311bacf%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22103.0.0.0%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22first_id%22%3A%221826695311ab6a-002ff698b31b9a-1c525635-2073600-1826695311bacf%22%7D'

url0='https://www.lagou.com/wn/jobs?kd=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&city=%E5%85%A8%E5%9B%BD'
url1='https://www.lagou.com/zhaopin/jiqixuexi/?filterOption=3'
url11='https://www.lagou.com/zhaopin/jiqixuexi/?filterOption=3'
url2='https://www.lagou.com/zhaopin/jiqixuexi/{}/?filterOption=3'
# headers 
headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie':cookie
        }


for i in range(1, 6):
    #sleep(random.randint(3,10))
    url=url2.format(i)
    if (i== 1):
        url = url1
    print('正在抓取第{}页...'.format(i),url)
    # 请求网络解析
    con = etree.HTML(requests.get(url=url, headers=headers).text)
    # 使用xpath表达式抽取各目标字段
    job_name=[i for i in con.xpath("//a[@class='position_link']/h3/text()")]
    job_address=[i for i in
            con.xpath("//a[@class='position_link']/span/em/text()")]
    job_company=[i for i in con.xpath("//div[@class='company_name']/a/text()")]
    job_salary=[i for i in con.xpath("//span[@class='money']/text()")]
    job_exp_edu=[i for i in con.xpath("//div[@class='li_b_l']/text()")]
    job_exp_edu2=[i for i  in [i.strip() for i in job_exp_edu] if i !='']
    job_industry=[i for i in con.xpath("//div[@class='industry']/text()")]
    job_tempation=[i for i in
            con.xpath("//div[@class='list_item_bot']/div[@class='li_b_r']/text()")]
    job_links = [i for i in con.xpath("//div[@class='p_top']/a/@href")]

    # 获取详情页链接后采集详情页岗位描述信息
    job_des = []
    for link in job_links:
        sleep(random.randint(3,10))
        #print(link)
        con2 = etree.HTML(requests.get(url=link, headers=headers).text)
        des=[[i.xpath('string(.)') for i in con2.xpath("//dd[@class='job_bt']/div/p")]]
        if len(des):
            des=[[i.xpath('string(.)') for i in con2.xpath("//dd[@class='job_bt']/div")]]
        job_des += des
    break

# 对数据进行字典封装
dataset = {
        '岗位名称':job_name,
        '工作地址': job_address,
        '公司':job_company,
        '薪资': job_salary,
        '经历学历':job_exp_edu2,
        '所属行业':job_industry,
        '岗位福利':job_tempation,
        '任职要求':job_des
        }

#转化为数据框并保存为csv
data = pd.DataFrame(dataset)
#print(data)
data.to_csv('machine_learning_job.csv')
