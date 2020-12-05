class TestDict(object):

    def __init__(self,fields,obj):
        self.fields = fields
        self.obj=obj


    def keys(self):                         # 获取字典的键
        return self.fields

    def __getitem__(self, item):            # 获取键对应的值
        return getattr(self.obj, item)          # getattr获取对象下某个属性的值


