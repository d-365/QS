# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: api.py
# @time: 2021/5/27 11:48
# @describe :

from interface.base.requests import Base_requests
from interface.base.caps import Caps


class user_pro:

    def __init__(self, environment=''):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # api/login
    def login(self, payload):
        url = self.caps['admin'] + '/api/sms/interface/dologin'
        res = self.re.post_login(url=url, datas=payload)
        return res
