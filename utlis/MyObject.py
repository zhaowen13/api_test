class TurnDict(dict):             
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

def dict_to_object(dictObj):    #将字典转换为对象
    if not isinstance(dictObj, dict):  
        return dictObj
    inst=TurnDict()
    for k,v in dictObj.items():
        inst[k] = dict_to_object(v)
    return inst