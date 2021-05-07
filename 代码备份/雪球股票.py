import requests,json,time
def timestamp_to_date(time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
  # print(time_stamp)
  time_array = time.localtime(int(time_stamp))
  str_date = time.strftime(format_string, time_array)
  return str_date

a='''
'''

f=open("sp.csv","a", encoding="utf-8")
payload={}
headers = {
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Cookie': '',
  'DNT': '1',
  'Host': 'xueqiu.com',
  'Referer': 'https://xueqiu.com/P/SP1007418',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
}



for ss in ['SP1007418,银行螺丝钉的实盘','SP1003839,A股版全球投资','SP1037391,林奇法则的实盘','SP1001582,实盘-哲銘一期','SP1004293,误点开后关闭了','SP1005282,持有封基的实盘','SP1001626,认真你就输了','SP1005725,那一水的鱼的实盘','SP1010158,上海电力_的实盘','SP1001068,打新组合','SP1006747,熊猫山顶站岗补刀','SP1032376,新开的打新账户','SP1000078,江涛的实盘','SP1000057,小权的实盘','SP1011798,自由老木头的实盘','SP1037714,券商毅力哥的实盘','SP1037125,金融毅力哥的实盘','SP1036238,国金毅力哥的实盘','SP1036097,国金毅力哥的实盘','SP1036019,国金毅力哥的实盘','SP1035886,国金毅力哥的实盘','SP1035823,国金毅力哥的实盘','SP1035583,国金毅力哥的实盘','SP1035570,国金毅力哥的实盘','SP1035534,国金毅力哥的实盘','SP1035453,国金毅力哥的实盘','SP1035351,国金毅力哥的实盘','SP1035192,国金毅力哥的实盘','SP1034279,投资是永_的实盘','SP1004865,沈潜的实盘','SP1002434,马马m股市_的实盘','SP1008759,逍遥稳进成长','SP1031443,许志宏的实盘','SP1003634,群兽中的_的实盘']:
    sp=ss.split(",")[0]
    name=ss.split(",")[1]
    url = "https://xueqiu.com/service/tc/snowx/PAMID/cubes/rebalancing/history?cube_symbol="+sp+"&count=20&page="+str(1)
    print(url,"??")
    time.sleep(2)
    if url in a:
        continue
    response = requests.request("GET", url, headers=headers, data=payload)
    if '''"result_code":"79000"''' in response.text:
        time.sleep(2)
        response = requests.request("GET", url, headers=headers, data=payload)
        if '''"result_code":"79000"''' in response.text:
            time.sleep(2)
            response = requests.request("GET", url, headers=headers, data=payload)
    j1=json.loads(response.text, strict=False)
    maxpage=j1["maxPage"]
    for page in range(maxpage):
        page=page+1
        url="https://xueqiu.com/service/tc/snowx/PAMID/cubes/rebalancing/history?cube_symbol="+sp+"&count=20&page="+str(page)
        if url in a:
            continue
        time.sleep(2)
        response = requests.request("GET", url, headers=headers, data=payload)
        if '''"result_code":"79000"''' in response.text:
            time.sleep(2)
            response = requests.request("GET", url, headers=headers, data=payload)
            if '''"result_code":"79000"''' in response.text:
                time.sleep(2)
                response = requests.request("GET", url, headers=headers, data=payload)
        j1 = json.loads(response.text, strict=False)
        try:
            print(len(j1["list"]),url)
            for i in j1["list"]:
                category=i["category"]
                status=i["status"]
                updated_at=timestamp_to_date(str(i["updated_at"])[:10])
                proactive=i["rebalancing_histories"][0]["proactive"]
                id=i["rebalancing_histories"][0]["id"]
                stock_name=i["rebalancing_histories"][0]["stock_name"]
                stock_symbol=i["rebalancing_histories"][0]["stock_symbol"]
                stock_type=i["rebalancing_histories"][0]["stock_type"]
                stock_label=str(i["rebalancing_histories"][0]["stock_label"]).replace("[","").replace("]","").replace("'","")
                price=i["rebalancing_histories"][0]["price"]
                target_weight=i["rebalancing_histories"][0]["target_weight"]
                prev_weight_adjusted=i["rebalancing_histories"][0]["prev_weight_adjusted"]
                # updated_at1=i["rebalancing_histories"][0]["updated_at"]
                f.write(sp+","+name+","+str(category).replace(",","")+","+str(status).replace(",","")+","+str(updated_at).replace(",","")+","+str(proactive).replace(",","")+","+str(id).replace(",","")+","+str(stock_name).replace(",","")+","+str(stock_symbol).replace(",","")+","+str(stock_type).replace(",","")+","+str(stock_label).replace(",","")+","+str(price).replace(",","")+","+str(target_weight).replace(",","")+","+str(prev_weight_adjusted)+"\r")

        except:
            print(url)
