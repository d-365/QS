# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 20:14
# @Author  : dujun
# @File    : xddd2.py
# @describe: 好单多多APP

from interface.base.caps import Caps
from interface.base.requests import Base_requests


class xddd_pro:

    def __init__(self, environment=''):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # 验证码登录
    def xddd2_login(self, params):
        url = self.caps['xddd2'] + 'interface/v3.0.0/beforeUser/res'
        res = self.re.get(url=url, params=params)
        return res

    # 密码登录
    def login_password(self, datas):
        url = self.caps['xddd2'] + 'interface/v4.1.0/beforeUser/pRes'
        res = self.re.post_app(url=url, datas=datas)
        return res
