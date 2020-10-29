
# -*- coding: utf-8 -*-
import allure
import pytest
import sys
sys.path.append('..')
from base.BasePage import test
from base.CaseOperate import case
from base import test

@allure.feature('测试用例1')
def test_case_01():
    name = "login"
    url = '/1.0/common/login_captcha'
    # test.data["phone"]=[]         #测试用的
    # test.data["phone"].append({"mobile": "15080600001"})
    # test.data["phone"].append({"mobile": "15080600002"})
    case.run(name, url)
    assert 0==0


# @allure.feature('测试用例2')
# def test_case_02():
#     case.run("resume_save","/1.0/member/resume/save")
#     assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])