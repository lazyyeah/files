#coding:utf-8
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .. import models,forms
from SeMFSetting.views import paging
from django.http import JsonResponse
import time,json
from django.utils.html import escape
# Create your views here.
import sqlite3
import requests
VULN_LEAVE={
    '0':'信息',
    '1':'低危',
    '2':'中危',
    '3':'高危',
    '4':'紧急'
    }
VULN_STATUS={
    '0':'已忽略',
    '1':'已修复',
    '2':'待修复',
    '3':'漏洞重现',
    '4':'复查中',
    }




@login_required
@csrf_protect
def vuln_change_status(request,vuln_id):
    user = request.user
    error=''
    if user.is_superuser:
        vuln = get_object_or_404(models.Vulnerability_scan,vuln_id=vuln_id)
    else:
        vuln = get_object_or_404(models.Vulnerability_scan,vuln_asset__asset_user=user,vuln_id=vuln_id)
    if vuln:
        if request.method == 'POST':
            form = forms.Vuln_action_form(request.POST,instance=vuln)
            if form.is_valid():
                form.save()
                error = '更改成功'
            else:
                error = '请检查参数'
        else:
            form = forms.Vuln_action_form(instance=vuln)
    else:
        error ='请检查参数'
    return render(request,'formupdate.html',{'form':form,'post_url':'vulnfix','argu':vuln_id,'error':error})




@login_required
@csrf_protect
def vuln_update(request,vuln_id):
    user = request.user
    error=''
    if user.is_superuser:
        vuln = get_object_or_404(models.Vulnerability_scan,vuln_id=vuln_id)
        if vuln:
            if request.method == 'POST':
                form = forms.Vuln_edit_form(request.POST,instance=vuln)
                if form.is_valid():
                    form.save()
                    error = '更改成功'
                else:
                    error = '请检查参数'
            else:
                form = forms.Vuln_edit_form(instance=vuln)
        else:
            error ='请检查参数'
    else:
        error = '权限错误'
    return render(request,'formupdate.html',{'form':form,'post_url':'vulnupdate','argu':vuln_id,'error':error})


@login_required
@csrf_protect
def vulncreate(request,asset_id):
    user = request.user
    error =''
    if user.is_superuser:
        asset = get_object_or_404(models.Asset,asset_id=asset_id)
    else:
        asset = get_object_or_404(models.Asset,asset_user = user,asset_id=asset_id)
    if request.method == 'POST':
        form = forms.Vuln_edit_form(request.POST)
        if form.is_valid():
            try:
                num = models.Vulnerability_scan.objects.latest('id').id
            except Exception:
                num = 0
            num =num+1
            vuln_name = form.cleaned_data['vuln_name']
            cve_name = form.cleaned_data['cve_name']
            leave = form.cleaned_data['leave']
            introduce = form.cleaned_data['introduce']
            vuln_info = form.cleaned_data['vuln_info']
            scopen = form.cleaned_data['scopen']
            fix = form.cleaned_data['fix']
            vuln_id = str(asset.asset_type.id) + time.strftime('%Y%m%d',time.localtime(time.time())) + str(num)
            vuln_type = asset.asset_type.name
            res=models.Vulnerability_scan.objects.get_or_create(
                                                                vuln_name=vuln_name,
                                                                 cve_name=cve_name,
                                                                 vuln_type=vuln_type,
                                                                 leave=leave,
                                                                 introduce=introduce,
                                                                 vuln_info=vuln_info,
                                                                 scopen=scopen,
                                                                 fix=fix,
                                                                 vuln_asset = asset,
                                                                 )
            vuln = res[0]
            if vuln.vuln_id == vuln_id:
                if vuln.fix_status == '1':
                    vuln.fix_status= '3'
            else:
                vuln.vuln_id = vuln_id
                if leave == '0':
                    vuln.fix_status= '0'
                vuln.fix_status= '2'
            vuln.save()
            error='添加成功'
        else:
            error = '请检查输入'
    else:
        form = forms.Vuln_edit_form()
    return render(request,'formupdate.html',{'form':form,'post_url':'vulncreate','argu':asset_id,'error':error})


@login_required
def vulndetails(request,vuln_id):
    user = request.user
    if user.is_superuser:
        vuln = get_object_or_404(models.Vulnerability_scan,vuln_id=vuln_id)
    else:
        vuln = get_object_or_404(models.Vulnerability_scan,vuln_asset__asset_user=user,vuln_id=vuln_id)
    return render(request,'VulnManage/vulndetails.html',{'vuln':vuln})



@login_required
def vulnview(request):
    print(request)
    #models.Vulnerability_scan.objects.get_or_create(create_data="2020-11-12 14:37:18", cve_name="cve-2020-9999", fix="1", fix_action="1", fix_status="1", id="1", introduce="1", leave="1", scopen="1", update_data="2020-11-12 14:37:18", vuln_asset=get_object_or_404(models.Asset,asset_id="1"), vuln_asset_id="1", vuln_id="1", vuln_info="1", vuln_name="1", vuln_type="1")

    return render(request,'VulnManage/vulnlist.html')




@login_required
@csrf_protect
def vulntablelist(request):
    #models.Vulnerability_scan.objects.get_or_create(create_data="2020-11-12 14:37:18", cve_name="cve-2020-9999", fix="1", fix_action="1", fix_status="1", id="1", introduce="1", leave="1", scopen="1", update_data="2020-11-12 14:37:18", vuln_asset=get_object_or_404(models.Asset,asset_id="012020102831"), vuln_asset_id="012020102831", vuln_id="1", vuln_info="1", vuln_name="1", vuln_type="1")
    #asset=get_object_or_404(models.Asset,asset_id="012020102825")
    #models.Vulnerability_scan.objects.get_or_create(fix_status="3",vuln_name=time.strftime('%Y%m%d%s',time.localtime(time.time())),cve_name="2",vuln_type="WEB应用",leave="3",introduce="introduce",vuln_info="vuln_info",scopen="None",fix="2",vuln_asset = asset,vuln_id=time.strftime('%Y%m%d%s',time.localtime(time.time())),)
    
    conn = sqlite3.connect('/usr/local/SecurityManageFramwork/db.sqlite3')
    cursor = conn.cursor()   
    sql="select asset_id,target,target_id,scan_id,scan_session_id,status,create_time from Vuln_status where status='created';"
    cursor.execute(sql)
    print(cursor)
   
    for i in cursor:

        asset_id=i[0]
        target=i[1]
        target_id=i[2]
        scan_id=i[3]
        scan_session_id=i[4]
        status=i[5]
        create_time=i[6]
        key="/api/v1/scans?l=20&q=target_id:{}".format(target_id)
        api_url = 'https://192.168.105.225:13443/'+key
        headers = {
            'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c744de80f3e81439ebbd6a9bcf0715da2',
            'Content-type': 'application/json;charset=utf8'
        }
        r = requests.get(url=api_url, headers=headers,verify=False)
        scan_session_id=str(r.json()['scans'][0]['current_session']['scan_session_id'])   
        status=str(r.json()['scans'][0]['current_session']['status'])
        scan_id=str(r.json()['scans'][0]['scan_id'])
        #print(scan_session_id,status)
        if status=='completed' :
            #conn = sqlite3.connect('/usr/local/SecurityManageFramwork/db.sqlite3')
            #cursor = conn.cursor()
            sql="UPDATE Vuln_status set scan_session_id = '{}',status='{}',scan_id='{}' where asset_id='{}';".format(scan_session_id,status,scan_id,asset_id)
            #print(sql)
            cursor.execute(sql)
            conn.commit()
            #conn.close()
            # 获取报告
            # /api/v1/scans/{scan_id}/results/{scan_session_id}/vulnerabilities?l={count}&s=severity:desc
            key="/api/v1/scans/{}/results/{}/vulnerabilities?l=100&s=severity:desc".format(scan_id,scan_session_id)
            api_url = 'https://192.168.105.225:13443/'+key
            headers = {
                'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c744de80f3e81439ebbd6a9bcf0715da2',
                'Content-type': 'application/json;charset=utf8'
            }
            r = requests.get(url=api_url, headers=headers,verify=False)
            #print(r.json())             

            vlist=r.json()['vulnerabilities']
            for i in vlist:
                #print(i)
                asset=get_object_or_404(models.Asset,asset_id=asset_id)
                #print(asset)
                cvelist=i['tags']
                cve=""
                for k in cvelist:
                    if "CWE" in k:
                        cve=k
                    if "cve" in k.lower():
                        cve=k
                severity=i['severity']
                if str(severity)=="0":
                    severity="1"
                introduce=str(json.dumps(i, sort_keys=True, indent=2,ensure_ascii=False))
                vuln_info=""
                vuln_name=str(i['vt_name'])+str(time.time())
                vuln_asset = "asset"
                vuln_id=str(i['vt_id'])
                #print(cve,severity,introduce,vuln_info,vuln_name,vuln_asset,vuln_id)
                models.Vulnerability_scan.objects.get_or_create(fix_status="2",vuln_name=vuln_name,cve_name=cve,vuln_type="WEB应用",leave=severity,introduce=introduce,vuln_info="vuln_info",scopen="None",fix="",vuln_asset = asset,vuln_id=vuln_id+str(time.time()),)
            
#        print(asset_id,target,target_id,scan_id,scan_session_id,status,create_time)
    user = request.user
    resultdict={}
    page = request.POST.get('page')
    rows = request.POST.get('limit')
    
    key = request.POST.get('key')
    if  not key:
        key=''
    
    leave = request.POST.get('leave')
    if  not leave:
        leave=''
    fix_status = request.POST.get('fix_status')
    if  not fix_status:
        fix_status=''
    
    
    if user.is_superuser:
        vuln_list = models.Vulnerability_scan.objects.filter(
            vuln_asset__asset_key__icontains = key,
            leave__icontains = leave,
            fix_status__icontains = fix_status,
            leave__gte = 1,
            ).order_by('-fix_status','-leave')
    else:
        vuln_list = models.Vulnerability_scan.objects.filter(
            vuln_asset__asset_user=user,
            vuln_asset__asset_key__icontains = key,
            leave__icontains = leave,
            fix_status__icontains = fix_status,
            leave__gte = 1,
            ).order_by('-fix_status','-leave')
    #for i in vuln_list:
    #    print(i)
    total = vuln_list.count()
    vuln_list = paging(vuln_list,rows,page)
    data = []
    #print(vuln_list)
    for vuln_item in vuln_list:
        dic={}
        dic['vuln_id'] =escape( vuln_item.vuln_id)
        dic['cve_name'] =escape( vuln_item.cve_name)
        dic['vuln_name'] =escape( vuln_item.vuln_name)
        dic['vuln_type'] =escape( vuln_item.vuln_type)
        dic['leave'] =escape( VULN_LEAVE[vuln_item.leave])
        dic['fix_status'] =escape( VULN_STATUS[vuln_item.fix_status])
        dic['update_data'] =escape( vuln_item.update_data)
        dic['asset'] =escape( vuln_item.vuln_asset.asset_key)
        dic['asset_id'] =escape( vuln_item.vuln_asset.asset_id)
        data.append(dic)
    resultdict['code']=0
    resultdict['msg']="漏洞列表"
    resultdict['count']=total
    resultdict['data']=data
    return JsonResponse(resultdict)
        

@login_required
@csrf_protect
def vulnfixlist(request):
    user = request.user
    error =''
    vuln_id_list = request.POST.get('vuln_id_list')
    vuln_id_list = json.loads(vuln_id_list)
    action = request.POST.get('action')
    if action == 'status':
        for vuln_id in vuln_id_list:
            if user.is_superuser:
                vuln = get_object_or_404(models.Vulnerability_scan,vuln_id=vuln_id)
                vuln.fix_status='4'
            else:
                vuln = get_object_or_404(models.Vulnerability_scan,asset_user=user,vuln_id=vuln_id)
                vuln.fix_status='4'
            vuln.save()
        error = '操作成功'
    else:
        error ='参数错误'
    return JsonResponse({'error':error})   
