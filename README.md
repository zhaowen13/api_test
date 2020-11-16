# 一.基本简介
1.采用requests库，BasePage初始化时会读取config配置文件获取请求地址，对requests基础的get,post等请求做了封装，加入了日志,
        把login也封装在底层，login会把登录信息（cookies，token，Session等）存放到属性中，在其他请求被调用时默认会带上登录信息
        ，每个请求的response会以属性的形式存放在data属性中，属性的名称就是请求的名称
        2.CaseOperate是case解析和执行，在初始化时会读取所有case目录下面所有的文件，把case按目录，name，存放在字典中

# 二.使用
1.在case目录创建模块目录，在模块目录下面创建对应的json文件，名字随便取（能让别人看懂就行）
例：
{
    "case_list": [
        {
            "name": "login",
            "url": "/1.0/common/login_captcha",
            "method": "post",
            "headers": {
                "Accept": "application/x-www-form-urlencoded; charset=utf-8"
            },
            "body": {
                "captcha": "${myMethod.idiot(${test.mobile})}",
                "mobile": "${test.mobile}"
            },
            "assertion": {
                "expected": "0",
                "actual": "${login.code}"
            }
        },
        {
            "name": "resume_save",
            "url": "/1.0/member/resume/save",
            "method": "post",
            "headers": {
                "Content-type": "application/json; charset=utf-8"
            },
            "body": {
                "member": {
                    "name": "二空",
                    "gender": "1",
                    "birthday": "2000-1-1",
                    "job_want_status": "1",
                    "expect_salary_min": "2000",
                    "expect_salary_max": "5000"
                },
                "resume": {
                    "expect_city_id": 11000,
                    "expect_job": "10,11"
                }
            },
            "assertion": {
                "expected": "0",
                "actual": "${resume_save.code}"
            }
        }
    ]
}

使用变量时${请求名.data[1]}
调用本地方法${myMethod.idiot(${test.mobile})}   idiot为方法名方法内的参数也可以调用变量
MyMethod中可以自定义方法，通过${myMethod.方法名(参数)}调用
请求地址,body和断言都可以使用变量
2.执行case
在test目录下创建以test开头的py文件 例test_01.py
在test_01.py 中创建类Test_choice   choice为case中的文件夹（模块）名

@allure.feature('测试用例1')    #allure报告
@pytest.mark.parametrize('name', (case.caae_name[module_name]["login"]))
#取choice文件夹下 login.json文件里面的所有case
def test_login(self,name):
    self.pytestObject(self,name)  #执行case，断言
方法名也要以test开头(pytest规范)
