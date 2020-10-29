class test(object):
    def __init__(self):
        pass

    def a(self,**text):
        print(text['username']+"是二逼啊")

    def c(self,**text):
        print(text['username']+"是sa逼啊")     


    def b(self,name,**text):
        func = getattr(self, name, None)
        func(**text)
    

    def methods(self):
        return(list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and callable(getattr(self, m)), dir(self))))

if __name__ == "__main__":
    t=test()
    print(t.methods())
    t.b('c',username="二空空")