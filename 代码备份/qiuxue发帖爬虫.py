#-*- coding: UTF-8 -*-
import json,time
import requests
import html2text
# Ignore converting links from HTML
h = html2text.HTML2Text()
h.ignore_links = True
import re



def ree(start, end, f):
    start = re.escape(start)
    end = re.escape(end)
    pattern = re.compile(r'%s(?:.|\s)*?%s' % (start, end))
    s = f
    updated = ''.join(re.split(pattern, s))
    return updated


def timestamp_to_date(time_stamp):
  # print(time_stamp)
  format_string = "%Y-%m-%d %H:%M:%S"
  time_array = time.localtime(int(time_stamp))
  str_date = time.strftime(format_string, time_array)
  return str_date

def 爬虫(maxpage,id,name):
    if 1:

        for page in range(maxpage):
            if page==0 and maxpage!=1:
                continue
            # if page<19:
            #     continue
            time.sleep(1.5)
            url = "https://qiuxue.com/v4/statuses/user_timeline.json?page="+str(page+1)+"&user_id="+id
            print(maxpage,url)
            payload={}
            headers = {
                'Host': 'qiuxue.com',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'DNT': '1',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                'elastic-apm-traceparent': '00-f5fadb595a9b1d841ad70dd541522e50-adca3eb431c2988b-00',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://qiuxue.com/u/3079173340',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cookie': '',
                'Content-Type': 'text/plain'
            }

            response = requests.request("GET", url, headers=headers, data=payload)
            j=json.loads(response.text, strict=False)
            page=j["page"]
            maxPage=j["maxPage"]
            textlist=j["statuses"]
            for t in textlist:
                tid=t["id"]
                source=t["source"].replace(";","")
                retweet_count=t["retweet_count"]#转发
                reply_count=t["reply_count"]#评论
                fav_count=t["fav_count"]#收藏
                like_count=t["like_count"]#点赞
                if False:
                    text=ree("(https://xqimg.imedao.com",".jpg)",h.handle(str(t["text"])).replace("\[","").replace("\]","").replace(" **","").replace("** ","")).replace("[]","").replace("//assets.imedao.com/ugc/images/face/emoji_","").replace(".png","")
                else:
                    text = h.handle(str(t["text"])).replace("\[", "").replace("\]", "").replace(" **", "").replace(
                                   "** ", "").replace("[]", "").replace("//assets.imedao.com/ugc/images/face/emoji_","").replace(".png", "").replace("https://xqimg.imedao.com","").replace(".jpg","")
                text=text.replace(";","").replace("  ","").replace("\r","").replace("\n","").replace("(03_applaud)","").replace("(01_smile)","").replace("(23_blood)","").replace("(02_laughing)","").replace("(19_noodles)","").replace("(33_face)","").replace("(07_wonderful)","").replace("(29_think)","")
                retweet_status_id=t["retweet_status_id"]#转发id
                donate_count=t["donate_count"]
                donate_snowcoin=t["donate_snowcoin"]
                paid_mention=t["paid_mention"]
                created_at = timestamp_to_date(str(t["created_at"])[0:10])
                if retweet_status_id==0:
                    aaa.write(str(id)+";"+str(name)+";"+str(created_at)+";"+str(tid)+";"+str(retweet_status_id)+";"+str(source)+";"+"https://qiuxue.com/"+str(id)+"/"+str(tid)+";"+str(retweet_count)+";"+str(reply_count)+";"+str(fav_count)+";"+str(like_count)+";"+str(text)+";"+str(donate_count)+";"+str(donate_snowcoin)+";"+str(paid_mention)+"\r")
                else:
                    aaa.write(str(id)+";"+str(name)+";"+str(created_at)+";"+str(tid)+";"+str(retweet_status_id)+";"+str(source)+";"+"https://qiuxue.com/"+str(id)+"/"+str(tid)+"\r")
    return maxPage
if __name__ == '__main__':
    l0=['2054435398,唐史主任司马迁','8290096439,唐朝','2340719306,流水白菜']
    aaa = open("发帖3.txt", "a", encoding="utf-8")
    for i in l0:
        id=i.split(",")[0]
        name=i.split(",")[1]
        maxPage=爬虫(1,id,name)
        if maxPage>1:
            爬虫(maxPage,id,name)
