from requests_html import HTMLSession 
import random 
import csv 
import json
import datetime

# 获取请求对象
session = HTMLSession()
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

def getTime():
    curtime = datetime.datetime.now()
    # 时间转字符串 strftime
    strtime = curtime.strftime('_%Y_%m_%d_%H_%M_%S')
    # 由字符串格式转化为日期格式的函数为: datetime.datetime.strptime()
    return strtime


class DxySARI(object):
    # “__init__()”方法，其是Python中的构造函数，构造函数用于初始化类的内部状态，为类的属性设置默认值
    def __init__(self):
        self.start = 0
        self.headers = {"User-Agent": random.choice(USER_AGENTS)}
        self.dxyurl = "https://3g.dxy.cn/newh5/view/pneumonia"
        self.items = []
        self.province_list = []
        self.city_list = []
        self.city_csv = '../data/city.csv'
        self.province_json = '../data/province'
    def get_html_page(self):
        response = session.get(self.dxyurl)
        # 01.完整页面
        page = response.html.html
        #print(page)
        # 02.目标内容
        # 得到start的索引
        start = page.find('window.getAreaStat = [')
        # 上面start的字符是22个 那么temp 是从start索引+22个字符索引之后开始
        # :表示取这个维度的全部值
        temp = page[start + 22:]
        # 结束位置的索引
        end = temp.find("]}catch(e){}")
        temp = temp[0:end]
        #print(temp)
        items = temp.split("]},")
        #print(items)
        # 03.最后一个元素, 特殊处理(尾部没有", "号)
        last = items[-1]
        #print(last)
        # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        items.pop()
        newitems = []
        for item in items:
            item = item + "]}"
            newitems.append(item)
            #print(item)
        # 04. 省市数据分布
        newitems.append(last)

        self.items = newitems
        return newitems

    # 数据结构化
    def get_detail_info(self, items):
        # 格式转换: 字符串->JSON
        for item in items:
            js = json.loads(item)
            #print(js)
            # 格式转换: JSON->字典
            dc = {}
            dc = dict(js)
            # 省份数据(含城市)
            self.province_list.append(dc)
            # 城市数据 (前缀增加省份)
            # pint(self.province_list)
            cities = dc["cities"]
            # 需要增加判断, 处理列表为空的情况(直辖市和特区的问题)
            if cities:
                for city in cities:
                    city["provinceName"] = dc["provinceName"]
                    self.city_list.append(city)
                    # print(city.keys())
            # 保存至文件
            # print(self.province_list)
            # print(self.city_list)
    # 省份数据写入json: 城市数据作为整体存储, 不使用
    def write_province_json(self):
        filename = self.province_json + getTime() + '.json'
        # print(filename)
        #header = ['provinceName', 'provinceShortName', 'confirmedCount',
        #        'suspectedCount', 'curedCount', 'deadCount', 'comment',
        #        'cities']
        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            try:
                json.dump(self.province_list, f)
            except Exception as e:
                print('Province数据写入异常' + e + ' 异常')

    # 城市数据写入csv
    def write_city_csv(self):
        filename = self.city_csv + getTime() + '.csv'
        header = ['cityName', 'confirmedCount', 'suspectedCount','curedCount', 'deadCount', 'provinceName']
        with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
            file_city = csv.writer(csvfile)
            file_city.writerow(header)
            try:
                for item in self.city_list:
                    #print(item)
                    #(x.get('name') is not None and x['name']) or 'default'
                    file_city.writerow([
                        (item.get('cityName') is not None and item['cityName'])
                        or 'unknown',
                        (item.get('confirmedCount') is not None and
                            item['confirmedCount']) or 0,
                        (item.get('suspectedCount') is not None and
                            item['suspectedCount']) or 0,
                        (item.get('curedCount') is not None and
                            item['curedCount']) or 0,
                        (item.get('deadCount') is not None and
                            item['deadCount']) or 0,
                        (item.get('provinceName') is not None and
                            item['provinceName']) or 0,
                        ])
            except Exception as e:
                print('City数据写入异常' + e + '异常')
if __name__ =='__main__':
    dxy = DxySARI()
    page = dxy.get_html_page()
    dxy.get_detail_info(page)
    dxy.write_province_json()
    dxy.write_city_csv()
