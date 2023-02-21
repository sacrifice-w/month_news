import requests
# from bs4 import BeautifulSoup
from fake_useragent import UserAgent  #提供假的请求头
from lxml import etree
import json
import jsonpath
import datetime
import os
import codecs

def to_string(html):
    return etree.tostring(html,encoding='utf-8').decode('utf-8') #只能解析对象不能解析list

# 政策信息
def gov():
    url = "http://www.gov.cn/zhengce/zuixin.htm"
    header = {'User-Agent':str(UserAgent().random)}
    response = requests.get(url,headers = header)
    response.encoding = "utf-8"
    tree = etree.HTML(response.text)
    # 存放最终结果
    result = []
    for s in range(1,101):
        # 提取网页内容
        link = tree.xpath('//div[@class="news_box"]/div/ul/li['+str(s)+']/h4/a/@href')
        content = tree.xpath('//div[@class="news_box"]/div/ul/li['+str(s)+']/h4/a/text()')
        date = tree.xpath('//div[@class="news_box"]/div/ul/li['+str(s)+']/h4/span/text()')
        # 过滤空值
        if(link == [] or content == [] or date == []):continue
        # 数据处理
        link = str(link).replace("['","").replace("']","")
        if(not link.startswith("http")):
            link = "http://www.gov.cn" + link
        content = str(content).replace("['","").replace("']","")
        date = str(date).replace("['","").replace("']","").replace(" ","").replace(r"\r\n","")
        li = {'title':content,'date':date,'link':link}
        result.append(li)
    final_json = json.dumps(result, sort_keys=True, indent=4, ensure_ascii=False)
    txt_path = '../news_txt/gov'
    if os.path.exists(txt_path) is False:
        os.makedirs(txt_path)
    f = codecs.open((txt_path + '/' + 'chinaGov.json'), 'w', 'utf-8')
    f.write(final_json)
    f.close()

gov()