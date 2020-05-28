
# -*- coding: utf-8 -*-
import allure
import pytest


@allure.feature('测试用例1')
def test_case_01():
    """
    用例描述：Test case 01
    """
    assert 0==0


@allure.feature('测试用例2')
def test_case_02():
    """
    用例描述：Test case 02
    """
    assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])