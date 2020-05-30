# -*- coding: utf-8 -*-
'''
@Author: your name
@Date: 2020-05-09 10:19:14
@LastEditTime: 2020-05-09 14:23:06
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \api_test\base\demo.py
'''

import requests
import hashlib
from custom_logger import logger_cls
import yaml
import os



    

class api_test(object):

    def __init__(self):
        self.cookies={}
        self.data={}
        self.my_requests=""
        yamlPath="context.yaml"
        yaml.load(yamlPath, Loader=yaml.BaseLoader)
        yaml.warnings({'YAMLLoadWarning': False})
        f = open(yamlPath, 'r')
        temp = yaml.load(f.read())
        self.uri=temp['oshadan']['uri']
        self.username=temp['oshadan']['username']
        self.password=temp['oshadan']['password']

    def login(self,url,body,headers):
        response=requests.post(self.uri+url,body,headers)
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format("login",url,headers,body,response.json()))
        self.cookies=response.cookies
        self.data["login"]=response.json()
        logger_cls.info(self.data)
        self.my_requests= requests.Session()

    def post(self,name,url,body,headers):
        response=self.my_requests.post(self.uri+url,body,headers,cookies=self.cookies).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format(name,url,headers,body,response))
        self.data={name:response}

    def get(self,name,url,headers):
        response=self.my_requests.get(self.uri+url,cookies=self.cookies).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nresponse:{3}".format(name,url,headers,response))
        self.data={name:response}

    def put(self,name,url,body,headers):
        response=self.my_requests.put(self.uri+url,body,headers,cookies=self.cookies).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format(name,url,headers,body,response))
        self.data={name:response}

    def delete(self,name,url,body,headers):
        response=self.my_requests.put(self.uri+url,body,headers,cookies=cookies).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format(name,url,headers,body,response))
        self.data={name:response}
    
test=api_test()


if __name__ == "__main__":
    name="login"
    name2="getRegionHomeNumbers"
    url = '/user-check'
    url2="/getRegionHomeNumbers?area="
    # m = hashlib.md5()
    # m.update(password)
    headers={"Accept":"application/json, text/plain, */*","Origin": uri,"Referer": uri}
    body ={"username": username, "password":password, "captcha": ""}
    api_test().login(url,body,headers)
    api_test().get(name2,url2,headers)
    # r=requests.post(uri+url,body,headers)
    # s = requests.Session()
    # logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format(name,url,headers,body,r.json()))
    # cookies=r.cookies
    # url2="/getRegionHomeNumbers?area="
    # r2=s.get(uri+url2,cookies=cookies)
    # logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nresponse:{3}".format(name2,url2,headers,r2.json()))
    # print data['login']['roleinfos']