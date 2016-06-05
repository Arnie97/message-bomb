import requests


def send_message(phone_number):
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:40.0) Gecko/20100101 Firefox/40.1'
    }
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
