# -*- coding: utf-8 -*-
'''
@Author: your name
@Date: 2020-05-09 14:24:30
@LastEditTime: 2020-05-11 17:26:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \api_test\case\test_sample.py
'''
from HTMLTestRunner import HTMLTestRunner
import pytest
import sys
import allure
sys.path.append('..')
from base.custom_logger import logger_cls
from base.demo import api_test


# @pytest.mark.parametrize(("a", "b", "expected"), [
#     [1, 2, 3],
#     [10, 11, 21],
#     [1, 1, 2],
# ])
# def test_answer(a, b, expected):
@allure.feature('login')
def test_1():
    test=api_test()
    url = '/user-check'
    # m = hashlib.md5()
    # m.update(password)
    headers = {"Accept": "application/json, text/plain, */*",  "Origin": test.uri, "Referer": test.uri}
    body = {"username": test.username,"password": test.password, "captcha": ""}
    test.login(url, body, headers)
    
    assert test.data["login"]["roleinfos"] == u"区域用户"
    # assert 1==2

# @allure.feature('getRegionHomeNumbers')
# def test_2():
#     name = "getRegionHomeNumbers"
#     url = '/getRegionHomeNumbers?area='
#     headers = {"Accept": "application/json, text/plain, */*",  "Origin": api_test().uri, "Referer": api_test().uri}
#     body = {"username": api_test().username,"password": api_test().password, "captcha": ""}
#     api_test().get(name, url, headers)
#     assert api_test().api_test().data[name]["success"] == True
