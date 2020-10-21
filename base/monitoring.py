from .BasePage import test


class monitoring(object):
    def login(self):
        url = '/user-check'
        # m = hashlib.md5()
        # m.update(password)
        headers = {"Accept": "application/json, text/plain, */*",  "Origin": test.uri, "Referer": test.uri}
        body = {"username": test.username,"password": test.password, "captcha": ""}
        test.login(url, body, headers)
        return test.data["login"]["roleinfos"]

    def getregion(self):
        name = "getRegionHomeNumbers"
        url = 'getRegionHomeNumbers?area='
        headers = {"Accept": "application/json, text/plain, */*",  "Origin": test.uri, "Referer": test.uri}
        body = {"username": test.username,"password": test.password, "captcha": ""}
        test.get(name, url, headers)
        return test.data[name]["success"]

test01=monitoring()