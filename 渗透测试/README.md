# 一些渗透测试的东西
## 常见工具的指令
### xray
.\xray_windows_amd64.exe webscan --listen 127.0.0.1:7778 --html-output 202103231009.html


xray_windows_amd64.exe webscan --url https://xxxn:39090/  --json-output 1.json
xray_windows_amd64.exe webscan --url http://xxx/app/?id=tracing.5g.mec.app  --html-output 202011250931.html

### vulmap
C:\Users\xxx\PycharmProjects\untitled\venv\Scripts\python.exe C:\scan\vulmap\vulmap.py -u  hxtp://xxxxx/

### sqlmap
C:\Users\xxx\AppData\Local\Programs\Python\Python37\python.exe  sqlmap.py -u "http://xxxxxx/search?text=1&fieldName=name"  -cookie="xxx=xxx-xxx-xxx-xxx-xxx"  -b --current-db --current-user
C:\Users\xxx\AppData\Local\Programs\Python\Python37\python.exe sqlmap.py   -r 3_Request.txt --level=3 --risk=3 --batch --flush-session

### dirmap
C:\Users\xxx\AppData\Local\Programs\Python\Python37\python.exe dirmap.py -i http://xxx.xxx.xxx.xxx:xxx/ -lcf

### hydra
hydra -l postgres -P pa -M iplist -o rdpresult -vV postgres

## 渗透测试流程
https://github.com/lazyyeah/files/blob/master/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E6%B5%81%E7%A8%8B.md

## 安全检测清单
https://github.com/lazyyeah/files/blob/master/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/%E5%AE%89%E5%85%A8%E6%A3%80%E6%9F%A5%E9%A1%B9%E6%B8%85%E5%8D%95.md

## 研发流程
https://github.com/lazyyeah/files/blob/master/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/%E7%A0%94%E5%8F%91%E6%B5%81%E7%A8%8B.png

