import requests
import json,urllib,time,http
import time 
import math
#使用前请修改以下路径，例如 C:/cookie.txt
cookie_file='/home/UPC-nCoV-submit/cookies.txt' #保存cookie文件
user_file="/home/UPC-nCoV-submit/用户信息.txt"   #用户信息文件
log_file="/home/UPC-nCoV-submit/result.txt"     #日志文件
cookie = http.cookiejar.LWPCookieJar(cookie_file)
handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)
with open(user_file,'r',encoding='utf8') as load_f:
    userinfo = json.load(load_f)
params = urllib.parse.urlencode(userinfo)

cookie.save(ignore_discard=True, ignore_expires=True)

headers1 = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',)
headers2=('X-Requested-With', 'XMLHttpRequest')
cookie = http.cookiejar.LWPCookieJar()
cookie.load(cookie_file, ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
opener.addheaders = [headers1,headers2]

with opener.open('https://app.upc.edu.cn/ncov/wap/default/index') as resp:
    result=json.loads(resp.read().decode("utf8"))['d']['oldInfo']
with opener.open('https://app.upc.edu.cn/ncov/wap/default/index') as resp:
    result1=json.loads(resp.read().decode("utf8"))['d']['info']
print(result)
print(result1)
result["date"]=time.strftime("%Y%m%d", time.localtime())
result['created']=result1['created']
result['id']=result1['id']
print(result)

with open(log_file,"a",encoding='utf8') as p :     
    jsObj = json.dumps(result)
    p.write("\n--------------------------\n")
    p.write(jsObj)
    p.write("\n"+time.ctime()+"\n--------------------------\n")
params = urllib.parse.urlencode(result)
with opener.open('https://app.upc.edu.cn/ncov/wap/default/save', data=bytes(params, 'utf-8')) as resp:
    print(resp.read().decode('utf-8'))
