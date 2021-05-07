#-*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import html2text
# Ignore converting links from HTML
h = html2text.HTML2Text()
h.ignore_links = True

payload={}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Cookie': '',
  'DNT': '1',
  'Host': 'weixin.sogou.com',
  'Referer': 'https://weixin.sogou.com/weixin?type=2&s_from=input&query=%E8%8C%85%E5%8F%B0+%E8%82%A1&ie=utf8&_sug_=n&_sug_type_=',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

name="茅台 股"
maxpage=2
for page in range(maxpage):
  page=page+1
  url = "https://weixin.sogou.com/weixin?type=2&s_from=input&query="+name+"&_sug_type_=&s_from=input&_sug_=n&type=2&page="+str(page)+"&ie=utf8"
  print(url,"\r")
  time.sleep(5)
  response = requests.request("POST", url, headers=headers, data=payload)
  soup = BeautifulSoup(response.text, 'lxml')
  for k in soup.find_all("div",class_="txt-box"):
      print("标题：",h.handle(str(k.h3.a)).replace(" ","").replace("_","").replace("\r","").replace("\n",""))
      print("描述：",h.handle(str(k.p)).replace("_","").replace(" ","").replace("\r","").replace("\n",""))
      print("链接：","https://weixin.sogou.com"+str(k.h3.a["href"]))
      print()
