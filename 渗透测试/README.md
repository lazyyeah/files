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
