# coding:utf-8
__author__ = 'chenhuachao'
# --------------------------------------------
# Created by chenhuachao  on 2018/1/26  17:18
# detail:
# --------------------------------------------
import requests
import sys
import uuid
import urllib
from config import AppID,AppKey
import time
import hashlib
from collections import OrderedDict

def getReqSign(params,appkey):
    '''
    计算sign签名
    :param params:
    :param appkey:
    :return:
    '''
    param=OrderedDict(sorted(params.items(),key=lambda x:x[0],reverse=False))
    Str=""
    for i,j in param.items():
        if j:
            n = i+"="+j+"&"
            Str+=n
    Str=Str+"app_key="+appkey
    m2=hashlib.md5()
    m2.update(Str)
    sign=m2.hexdigest().upper()
    return sign

def main(url,content):
    '''
    分词请求主函数
    :param url: 
    :param content: 
    :return: 
    '''
    time_stamp=int(time.time())

    text=urllib.quote(content.decode(sys.stdin.encoding).encode('gbk')).upper()
    nonce_str=str(uuid.uuid1()).replace('-',"")[:10]
    param={
        "app_id":AppID,
        "time_stamp":str(time_stamp),
        "nonce_str":nonce_str,
        "text":text
    }
    sign=getReqSign(param,AppKey)
    param['sign']=sign
    params='app_id='+AppID+'&time_stamp='+str(time_stamp)+'&nonce_str='+nonce_str+'&sign='+sign+'&text='+text
    res=requests.get(url+"?"+params)
    aa= res.content
    print aa.decode('GB2312').encode('utf-8')

if __name__ == '__main__':
    url="https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordseg"
    text1="打工夫妇照顾房东老人39年，获赠北京房产，你怎么看？"
    main(url,text1)


