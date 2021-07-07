# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: api.py
# @time: 2021/5/31 14:30
# @describe : 信业帮App

from interface.base.caps import Caps
from interface.base.requests import Base_requests


class api_pro:

    def __init__(self, environment=''):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # 信业帮App登录接口
    def user_login(self, data=''):
        url = self.caps['api'] + 'interface/v1.0.0/user/res'
        res = self.re.get(url=url, params=data)
        return res

    # 信业帮App查询当前线索信息
    def current_loanList(self, headers=''):
        url = self.caps['api'] + 'interface/v2.0.0/loan/list'
        res = self.re.get(url=url, headers=headers)
        return res

    # 查询我的线索发布记录
    def myloan(self,headers):
        url = self.caps['api'] + 'interface/v2.0.0/loan/list'
        res = self.re.post(url=url, headers=headers)
        return res

