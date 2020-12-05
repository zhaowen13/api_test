# -*- coding: utf-8 -*-
from base.BasePage import test
from utlis.MyMethod import myMethod
from utlis import MyObject
import json
import os
import re


class Case(object):

    def __init__(self):     #初始化时取出所有json文件中的case
        request = {}
        case_name={}
        path = "../case/"
        folders = os.listdir(path)        #获取case目录下的所有文件夹名称
        for folder in folders:
            files = os.listdir("{0}/{1}/".format(path, folder))
            request[folder] = {}       #case的模块名
            case_name[folder]={}       #case_name的模块名
            for file in files:      #获取文件夹下所有文件
                case_name[folder][file.split('.')[0]]=[]
                with open('{0}/{1}/{2}'.format(path, folder, file), 'r', encoding='utf8')as fp:
                    json_list = json.load(fp)
                for json_data in json_list['case_list']:    #保存文件中的所有case    
                    request[folder][json_data['name']] = json_data   #按照模块名 用例名称保存好
                    case_name[folder][file.split('.')[0]].append(json_data["name"]) 
                    #case集，按模块名，json文件名存放  
        self.case_name=case_name
        self.request = request

    def myReplace(self, body):   #替换json方法
        obj=test.data
        if '${' in body:   #如果body中包含变量
            responses = re.findall(r'\$(.+?)\}', body, re.M | re.I)     #用正则匹配出所有的变量
            for response in responses:
                if "myMethod" in response:       #如果包含myMethod，则为方法
                    response = "$"+response+"}"
                    name = response.split("myMethod.")[1].split("(")[0]
                    parameter = response.split(name+"(")[1].split(")")[0]
                    if '${' in parameter:     #如果方法里面的参数是变量
                        response = response+")}"
                        parameter = parameter.replace("${", "{data.")   
                        parameter = parameter.format(data=obj)
                    new_parameter = myMethod.get(
                        name, parameter.encode('utf-8').decode('unicode_escape'))
                    body = body.replace(response, new_parameter)    #返回替换好的body
                    print(body)
                else:
                    response = "$"+response+"}"
                    new_response = response
                    new_response = new_response.replace("${", "{data.")                
                    body = body.replace(
                        response, new_response.format(data=obj))
        body = json.loads(body)
        return body

    def run(self, class_name, name):        #执行请求方法
        request_parameter = self.request[class_name][name]    #获取请求参数
        url = request_parameter["url"].replace("${", "{data.").format(data=test.data)   #替换路径参数
        body = self.myReplace(json.dumps(request_parameter['body']))   #替换body参数
        method = request_parameter['method']   #请求方法
        if method == "get":      #判断请求方法
            test.get(name, url, request_parameter['headers'])
        elif method == "post":
            if name == "login":
                test.login(url, body)
            else:
                test.post(name, url, body, request_parameter['headers'])
        elif method == "put":
            test.put(name, url, body, request_parameter['headers'])
        elif method == "delete":
            test.delete(name, url, body, request_parameter['headers'])
        assertion = self.myReplace(json.dumps(request_parameter['assertion']))    #替换断言结果
        return assertion   #返回断言结果


case = Case()

if __name__ == "__main__":
    name = "login"
    # test.data["response"] = {"login": {"mobile": "15080605720"}}
    # url = '/1.0/common/login_captcha'
    # # c = Case()
    # c.run(name)
    # request_parameter = c.request[name]
    # body = c.myReplace(request_parameter)
    # print(body)
    # c.run("resume_save", "/1.0/member/resume/save")
    # obj = MyObject.dict_to_object(test.data)
    # print("{response.login.mobile}".format(response=obj.response))
