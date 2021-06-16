# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: api.py
# @time: 2021/5/27 11:48
# @describe : 信业帮(信贷多多)后台项目

from interface.base.caps import Caps
from interface.base.requests import Base_requests


class user_pro:

    def __init__(self, environment=''):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # 信业帮后台登录接口
    def login(self, payload):
        url = self.caps['admin'] + '/api/sms/interface/dologin'
        res = self.re.post_login(url=url, datas=payload)
        return res
