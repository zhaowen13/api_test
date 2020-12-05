# import test
import sys
sys.path.append('..')
from utlis import MyObject
from BasePage import test

class a(object):
    pass

class Abc(object):
    def __init__(self):
        self.name=a()

def setName(name):
    name="kongkong"


if __name__ == "__main__":
    name="zhaowen"
    setName(name)
    print(name)
   