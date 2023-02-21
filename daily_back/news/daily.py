import requests
# from bs4 import BeautifulSoup
from fake_useragent import UserAgent  #提供假的请求头
import json
import jsonpath
import datetime
import os
import codecs

# 电子银行网
def get_ele_bank():
    # 因为电子银行网发送的数据都存在json里，所以直接访问json
    # 这个网站的逻辑，是首先有一个index.json,然后点一次加载，加载一个index_2.json，以此类型直到到昨天的新闻

    # 获取当日新闻
    # 首先获取当日日期
    now_time = datetime.datetime.now().strftime('%Y%m%d')

    # 存放当日新闻
    today_news_total = []
    for i in range(0,10):
        today_news = []
        if i == 0:
            url = "https://www.cebnet.com.cn/json/sy/index.json"
        else:
            url = "https://www.cebnet.com.cn/json/sy/index_%s.json"%(i+1)
        header = {'User-Agent':str(UserAgent().random)}

        # 通过get请求获取标题，链接，来源
        # get请求在第546行
        # 传入的数据在index.json里
        # data.url 和 data.title
        response = requests.get(url,headers = header)
        response.encoding = "utf-8"
        html = response.text
        data = json.loads(html)
        """ 
        json格式
        "list":[
            {
                "id":           文章id
                "title":        文章标题
                "summary":      文章简介
                "author":       文章作者
                "picLinks":     文章显示图
                "pubTime":      文章时间，不准
                "source":       文章来源
                "keyword":      文章关键词
                "articleLink"   文章
            }
        ]
        """
        #获取当日新闻的标题，来源，链接
        title = jsonpath.jsonpath(data, '$..title')
        source = jsonpath.jsonpath(data, '$..source')
        link = jsonpath.jsonpath(data, '$..articleLink')
        pubTime = jsonpath.jsonpath(data, '$..pubTime')

        for i in range(len(title)):
            pubTime_new = pubTime[i].split('-')
            news_time = pubTime_new[0]+pubTime_new[1] + pubTime_new[2].split(' ')[0]
            # 判断是不是今天的新闻
            if news_time == now_time:
            # 因为这个link传进来是json形式，得处理一下
                link_id = link[i].strip('https://www.cebnet.com.cn/json/').lstrip(now_time).lstrip('/')
                link_correct = 'https://www.cebnet.com.cn/' + now_time + '/' + link_id +'.html'
                today_new = {'title':title[i],'source':source[i],'link':link_correct}
                today_news.append(today_new)
        today_news_total.extend(today_news)

    final_json = json.dumps(today_news_total, sort_keys=True, indent=4, ensure_ascii=False)
    # print(final_json)
    # 存放每日新闻
    txt_path = '../news_txt/ele_bank'
    if os.path.exists(txt_path) is False:
        os.makedirs(txt_path)
    
    f = codecs.open((txt_path + '/' + '%s.json'%(now_time)), 'w', 'utf-8')
    f.write(final_json)
    f.close()
    
    # print(today_news_total)
    # print(len(today_news_total))

get_ele_bank()