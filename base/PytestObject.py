
# -*- coding: utf-8 -*-
import pytest
import sys
from base.BasePage import test
from base.CaseOperate import case
from utlis import MyObject

class PytestClass(object):

    def pytestObject(self,module,name):        
        module=module.__class__.__name__    #module为一个对象，类名与case模块名一致
        module=module.split("_")[1]
        assertion=case.run(module,name)
        assert assertion["expected"]==assertion["actual"]   #断言预期结果与实际结果是否一致


    # @allure.feature('测试用例2')
    # def test_case_02(self):
    #     case.run("resume_save","/1.0/member/resume/save")
    #     assert 0 == 0


