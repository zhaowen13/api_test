# -*- coding: utf-8 -*-
'''
基础类封装login和各种请求并返回data对象
'''

import requests
import hashlib
import yaml
import sys
from utlis.custom_logger import logger_cls
from utlis import MyObject
     

class DataSet(object):
    pass
    

class api_test(object):

    def __init__(self):       #初始化，并读取配置文件
        self.cookies={}
        self.data=DataSet()       #初始值为对象
        self.my_requests=""
        self.token=""
        yamlPath="../base/config.yaml"
        yaml.load(yamlPath, Loader=yaml.BaseLoader)
        yaml.warnings({'YAMLLoadWarning': False})
        f = open(yamlPath, 'r')
        temp = yaml.load(f.read())
        self.uri=temp['st3']['uri']

    def login(self,url,body,headers=None):     #login方法保存cookies，token，Session等登录信息
        response=requests.post(self.uri+url,body,headers,verify=False)
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format("login",url,headers,body,response.json()))
        self.cookies=response.cookies
        setattr(self.data,"login",MyObject.dict_to_object(response.json()))      #给data对象添加login的属性
        self.token=response.json()['data']['token']
        self.my_requests= requests.Session()

    def post(self,name,url,body,headers):   #post请求，默认添加login返回的Authorization信息
        headers['Authorization']=self.token
        response=self.my_requests.post(self.uri+url,body,headers=headers,cookies=self.cookies,verify=False).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format(name,url,headers,body,response))
        setattr(self.data,name,MyObject.dict_to_object(response))

    def get(self,name,url,headers):   #get请示,没有body
        headers['Authorization']=self.token
        response=self.my_requests.get(self.uri+url,cookies=self.cookies,headers=headers,verify=False).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nresponse:{3}".format(name,url,headers,response))
        setattr(self.data,name,MyObject.dict_to_object(response))


    def put(self,name,url,body,headers):   #put请求
        headers['Authorization']=self.token
        response=self.my_requests.put(self.uri+url,body,headers,cookies=self.cookies,verify=False).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format(name,url,headers,body,response))
        setattr(self.data,name,MyObject.dict_to_object(response))



    def delete(self,name,url,body,headers):    #delete请求
        headers['Authorization']=self.token
        response=self.my_requests.put(self.uri+url,body,headers,cookies=self.cookies,verify=False).json()
        logger_cls.info("\nname:{0}\nurl:{1}\nheaders:{2}\nbody:{3}\nresponse:{4}".format(name,url,headers,body,response))
        setattr(self.data,name,MyObject.dict_to_object(response))


    
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