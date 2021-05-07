import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from email.header import Header
import time

def send_mail(tittle,url):
    try:
        host_server = 'smtp.126.com'
        # sender_qq为发件人的邮126箱
        sender_qq = ''
        # pwd为126邮箱的授权码
        pwd = ''
        # 发件人的邮箱
        sender_qq_mail = ''
        # 收件人邮箱
        receiver = ",".join(['','@qq.com','@qq.com'])
        # 邮件的正文内容
        mail_content = '看看学校网站最新通知:'+tittle+url
        # 邮件标题
        mail_title = '看看学校网站最新通知'
        # ssl登录
        smtp = SMTP_SSL(host_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(1)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)
        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    while(1):
        f=open("hebeiyikedaxue.txt","r")
        txt=f.read()
        f.close()
        f = open("hebeiyikedaxue.txt", "a")
        r=requests.post("http://gschool.hebmu.edu.cn/xinwen.aspx?sectionid=50")
        soup=BeautifulSoup(r.text, 'lxml')
        for i in soup.find_all("tr"):
            try:
                for k in i.find_all("a"):

                        tittle=str(str(k.string).replace("\r\n","").replace(" ",""))
                        try:
                            href=k["href"]
                        except:
                            href=""
                        url=str("http://gschool.hebmu.edu.cn/"+href)
                if tittle not in "首页上一页下一页末页首页上一页下一页末页后台管理联系方式通知公告" and tittle+url not in txt:
                    f.write(tittle+url+"\r\n")
                    if send_mail(tittle,url):
                        print(tittle, url, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            except:
                print("error")
        f.close()
        time.sleep(60*30)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
