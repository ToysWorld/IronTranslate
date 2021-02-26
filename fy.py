import os
import urllib.request
import urllib.parse
import json
from time import sleep

while 1:
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}

    local = os.getcwd()

    f = open(local + "\\will.txt")

    data['i'] = f.read()
    data['from']= 'AUTO'
    data['to']= 'AUTO'
    data['smartresult']= 'dict'
    data['client']= 'fanyideskweb'
    data['salt']= '16029936230111'
    data['sign']= '08714420b7b24624cdc1b9539ac3b9de'
    data['lts']= '1602993623011'
    data['bv']= 'a1cbc92f4166e300df7d5089e67d53ed'
    data['doctype']= 'json'
    data['version']= '2.1'
    data['keyfrom']= 'fanyi.web'
    data['action']= 'FY_BY_REALTlME'
    data = urllib.parse.urlencode(data).encode('utf-8')

    reponse = urllib.request.urlopen(url,data)
    html = reponse.read().decode('utf-8')

    htmls = json.loads(html)
    result = htmls['translateResult'][0][0]['tgt']

    f = open(local +  "\\result.txt")
    f.write(result)
   
    #for i in range(0,3):
        #print(f'为了防止造成服务器拥堵，请等待{3 - i}秒后继续翻译！')
        #sleep(1)
        #os.system("cls")


