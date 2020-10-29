# -*- coding: utf-8 -*-
from base.BasePage import test
import json
import os
import re



class Case(object):

    def __init__(self):
        pass

    def read(self):
        request = {}
        path = "../case/"
        folders = os.listdir(path)
        for folder in folders:
            files = os.listdir("{0}/{1}/".format(path, folder))
            for file in files:
                with open('{0}/{1}/{2}'.format(path, folder, file), 'r', encoding='utf8')as fp:
                    json_list = json.load(fp)
                for json_data in json_list['case_list']:
                    request[json_data['name']] = json_data
        return request

    def my_replace(self, request_list):
        body = json.dumps(request_list['body'])
        if '$' in body:
            joins = re.search(r'\$\{(.+?)\}', body, re.M | re.I).groups()
            for join in joins:
                response = test.data
                for j in join.split("."):
                    if "[" in j:
                        response = response[j.split("[")[0]]
                        response = response[int(
                            j.split("[")[1].replace("]", ""))]
                    else:
                        response = response[j]
                body=body.replace("${"+join+"}", response)
        body = json.loads(body)
        return body

    def run(self, name, url):
        request_list = self.read()[name]
        body = self.my_replace(request_list)
        method = request_list['method']
        if method == "get":
            test.get(name, url, request_list['headers'])
        elif method == "post":
            if name == "login":
                test.login(url, body)
            else:
                test.post(name, url, body, request_list['headers'])
        elif method == "put":
            test.put(name, url, body, request_list['headers'])
        elif method == "delete":
            test.delete(name, url, body, request_list['headers'])
        return test.data[name]
        


case = Case()

if __name__ == "__main__":
    name = "login"
    test.data["phone"] = []
    test.data["phone"].append({"mobile": "15080600001"})
    test.data["phone"].append({"mobile": "15080600002"})
    url = '/1.0/common/login_captcha'
    c = Case()
    c.run(name, url)
    c.run("resume_save", "/1.0/member/resume/save")


