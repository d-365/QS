# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: userInformation.py
# @time: 2021/5/27 11:21
# @describe :

from interface.base.requests import Base_requests
from interface.base.caps import Caps


class userInfo_pro:

    def __init__(self, environment=''):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # phoneSale/addOrder 电销中心_新增订单
    def addOrder(self, data, cookies=''):
        url = self.caps['admin'] + 'api/v2.0.0/UserInformation/phoneSale/addOrder'
        res = self.re.post_json(url=url, datas=data, cookies=cookies)
        return res

    # 查询订单详情
    def orderList(self, datas, cookies):
        url = self.caps['admin'] + 'api/v2.0.0/UserInformation/order/OrderList'
        res = self.re.post_json(url=url, datas=datas, cookies=cookies)
        return res
