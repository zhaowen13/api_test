# import MyObject
# from Dict import TestDict
import json
'''
自定义方法类，传入参数为数组，第一个参数为方法名，其他为自定参数
通过getattr调用
'''


class Method(object):
    def __init__(self):
        self.name = ""
        self.age = ""
        pass

    def a(self, data, data2):
        data = json.loads(data)
        data2 = json.loads(data2)
        data.keys()

    def idiot(self, *text):
        print(text[1]+"是sa逼啊")
        return "1234"

    def get(self, *key):
        func = getattr(self, key[0], None)
        return func(*key)

    def myTest(self, name, text):
        print("name:{0} text:{1}".format(name, text))

    def methods(self):
        return(list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and callable(getattr(self, m)), dir(self))))


myMethod = Method()

if __name__ == "__main__":
    t=Method()
    c=getattr(t,"name", 4)
    print(c)