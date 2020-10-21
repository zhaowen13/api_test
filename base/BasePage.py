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
import yaml
import sys

from base.custom_logger import logger_cls
     


    

class api_test(object):

    def __init__(self):
        self.cookies={}
        self.data={}
        self.my_requests=""
        self.token=""
        yamlPath="../base/config.yaml"
        yaml.load(yamlPath, Loader=yaml.BaseLoader)
        yaml.warnings({'YAMLLoadWarning': False})
        f = open(yamlPath, 'r')
        temp = yaml.load(f.read())
        self.uri=temp['st3']['uri']

    def login(self,url,body,headers=None):
        response=requests.post(self.uri+url,body,headers,verify=False)
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format("login",url,headers,body,response.json()))
        self.cookies=response.cookies
        self.data["login"]=response.json()
        self.token=response.json()['data']['token']
        logger_cls.info(self.data)
        self.my_requests= requests.Session()

    def post(self,name,url,body,headers):
        headers['Authorization']=self.token
        response=self.my_requests.post(self.uri+url,body,headers=headers,cookies=self.cookies).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format(name,url,headers,body,response))
        self.data={name:response}

    def get(self,name,url,headers):
        headers['Authorization']=self.token
        response=self.my_requests.get(self.uri+url,cookies=self.cookies,headers=headers).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nresponse:{3}".format(name,url,headers,response))
        self.data={name:response}

    def put(self,name,url,body,headers):
        headers['Authorization']=self.token
        response=self.my_requests.put(self.uri+url,body,headers,cookies=self.cookies).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format(name,url,headers,body,response))
        self.data={name:response}

    def delete(self,name,url,body,headers):
        headers['Authorization']=self.token
        response=self.my_requests.put(self.uri+url,body,headers,cookies=self.cookies).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format(name,url,headers,body,response))
        self.data={name:response}
    
test=api_test()


if __name__ == "__main__":
    name="login"
    name2="getRegionHomeNumbers"
    url = '/1.0/common/login_captcha'
    url2="/getRegionHomeNumbers?area="
    headers={"Accept":"application/x-www-form-urlencoded; charset=utf-8"}
    body ={"captcha": "1234", "mobile":"15080600001"}
    api_test().login(url,body)
    # api_test().get(name2,url2,headers)