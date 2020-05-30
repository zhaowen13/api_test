# -*- coding: utf-8 -*-
'''
@Author: your name
@Date: 2020-05-09 14:24:30
@LastEditTime: 2020-05-11 17:26:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \api_test\case\test_sample.py
'''

import pytest
import sys
import allure
sys.path.append('..')
from case.monitoring import test01



# @pytest.mark.parametrize(("a", "b", "expected"), [
#     [1, 2, 3],
#     [10, 11, 21],
#     [1, 1, 2],
# ])
# def test_answer(a, b, expected):
@allure.feature('login')
def test_1():
    roleinfos=test01.login()
    assert roleinfos == u"区域用户"

@allure.feature('getRegionHomeNumbers')
def test_2():
    success=test01.getregion()
    assert success == True
