import pytest
import allure
import sys
sys.path.append('..')
from base.PytestObject import PytestClass
from base.CaseOperate import case

class Test_choice(PytestClass):    #继承PytestClass
    module_name=sys._getframe().f_code.co_name.split("_")[1]

    @allure.feature('测试用例1')
    @pytest.mark.parametrize('name', (case.caae_name[module_name]["login"]))   #取对应json文件里面的所有case
    def test_login(self,name):
        self.pytestObject(self,name)  #执行case，断言


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])