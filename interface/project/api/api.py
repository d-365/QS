# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: api.py
# @time: 2021/5/31 14:30
# @describe : 信业帮App

from interface.base.requests import Base_requests
from interface.base.caps import Caps


class api_pro:

    def __init__(self, environment=''):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # 信业帮登录接口
    def user_login(self, data=''):
        url = self.caps['api'] + 'interface/v1.0.0/user/res'
        res = self.re.get(url=url, params=data)
        return res

    # 信业帮查询当前线索信息
    def current_loanList(self, datas):
        url = self.caps['api'] + 'interface/v2.0.0/loan/list'
        res = self.re.get(url=url, params=datas)
        return res
