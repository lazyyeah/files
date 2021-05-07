import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import time
# #读报告
# key="/api/v1/targets"
# api_url = 'https://192.168.105.225:13443/'+key
# headers = {
#     'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c744de80f3e81439ebbd6a9bcf0715da2',
#     'Content-type': 'application/json'
# }
# r = requests.get(url=api_url, headers=headers, verify=False)
# print(r.json())


# #添加目标
# key="/api/v1/targets"
# api_url = 'https://192.168.105.225:13443/'+key
# headers = {'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c744de80f3e81439ebbd6a9bcf0715da2','Content-type': 'application/json;charset=utf8'}
# data='''{"address":"http://www.sqlsec.com","description":"012020102817","criticality":"10"}'''
# r = requests.post(url=api_url, headers=headers,data=data, verify=False)
# print(r.json()["target_id"])
# '''
# 8b1cc27b-5a3a-40bb-b253-f87204ccf78a
# '''


# #扫描
# key="/api/v1/scans"
# api_url = 'https://192.168.105.225:13443/'+key
# headers = {
#     'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c744de80f3e81439ebbd6a9bcf0715da2',
#     'Content-type': 'application/json;charset=utf8'
# }
# target_id="8b1cc27b-5a3a-40bb-b253-f87204ccf78a"
# data='''{{
# "target_id":"{}",
# "profile_id":"11111111-1111-1111-1111-111111111111",
# "schedule":
#       {{"disable":false,
#        "start_date":null,
#        "time_sensitive":false
#        }}
# }}'''.format(target_id)
# r = requests.post(url=api_url, headers=headers,data=data, verify=False)
# print(r.json())
# '''
# {'profile_id': '11111111-1111-1111-1111-111111111111', 'schedule': {'disable': False, 'start_date': None, 'time_sensitive': False, 'triggerable': False}, 'target_id': '8b1cc27b-5a3a-40bb-b253-f87204ccf78a', 'incremental': False, 'max_scan_time': 0, 'ui_session_id': None}
# '''

# #获取扫描状态
# target_id="8b1cc27b-5a3a-40bb-b253-f87204ccf78a"
# key="/api/v1/scans?l=20&q=target_id:{}".format(target_id)
# api_url = 'https://192.168.105.225:13443/'+key
# headers = {
#     'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c744de80f3e81439ebbd6a9bcf0715da2',
#     'Content-type': 'application/json;charset=utf8'
# }
# r = requests.get(url=api_url, headers=headers,verify=False)
# print(r.json())
# '''
# {'pagination': {'count': 1, 'cursor_hash': '895b764c9d5e54804018099f4eb399f3', 'cursors': [None], 'sort': None}, 'scans': [{'criticality': 10, 'current_session': {'event_level': 1, 'progress': 100, 'scan_session_id': 'eb68d332-9e4d-4be6-85a6-3e82df7a2c77', 'severity_counts': {'high': 0, 'info': 65, 'low': 7, 'medium': 1}, 'start_date': '2020-11-12T09:08:42.974917+00:00', 'status': 'completed', 'threat': 2}, 'incremental': False, 'max_scan_time': 0, 'next_run': None, 'profile_id': '11111111-1111-1111-1111-111111111111', 'profile_name': 'Full Scan', 'report_template_id': None, 'scan_id': 'ddf02da4-f172-4f9d-9fc9-79fe532387ef', 'schedule': {'disable': False, 'history_limit': None, 'recurrence': None, 'start_date': None, 'time_sensitive': False, 'triggerable': False}, 'target': {'address': 'http://www.sqlsec.com', 'criticality': 10, 'description': '012020102817', 'type': 'default'}, 'target_id': '8b1cc27b-5a3a-40bb-b253-f87204ccf78a'}]}
# '''


# 获取报告
# /api/v1/scans/{scan_id}/results/{scan_session_id}/vulnerabilities?l={count}&s=severity:desc
scan_id="35518a97-b04d-4b00-a833-8165cf635c00"
scan_session_id="5ea57cfd-cbf8-45bf-b71e-9114e6585197"
key="/api/v1/scans/{}/results/{}/vulnerabilities?l=100&s=severity:desc".format(scan_id,scan_session_id)
api_url = 'https://192.168.105.225:13443/'+key
headers = {
    'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c744de80f3e81439ebbd6a9bcf0715da2',
    'Content-type': 'application/json;charset=utf8'
}
r = requests.get(url=api_url, headers=headers,verify=False)
# print(r.json())
vlist=r.json()['vulnerabilities']
for i in vlist:
    print(i)
    cvelist=i['tags']
    cve=""
    for k in cvelist:
        if "CWE" in k:
            cve=k
        if "cve" in k.lower():
            cve=k
    severity=i['severity']
    introduce=str(json.dumps(i, sort_keys=True, indent=2))
    vuln_info=""
    vuln_name=str(i['vt_name'])+str(time.time())
    vuln_asset = "asset"
    vuln_id=str(i['vt_id'])
    print(cve,severity,introduce,vuln_info,vuln_name,vuln_asset,vuln_id)
# todo
'''确定安全等级数字awvs和xsoc对应，xsoc读漏洞详情并写入'''

# 获取单个漏洞详细报告
# /api/v1/scans/{scan_id}/results/{scan_session_id}/vulnerabilities/{vuln_id}
# key="/api/v1/scans/cdbf2bd2-76ca-4489-8b36-d961c254c95b/results/74413f37-62ad-4a10-81ae-e90cced3c37d/vulnerabilities/2435556751962015696"
# api_url = 'https://192.168.105.225:13443/'+key
# headers = {
#     'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c744de80f3e81439ebbd6a9bcf0715da2',
#     'Content-type': 'application/json;charset=utf8'
# }
# r = requests.get(url=api_url, headers=headers,verify=False)
# print(r.json())
