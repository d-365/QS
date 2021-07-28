# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: userInformation.py
# @time: 2021/5/27 11:21
# @describe : 好单多多后台

from interface.base.caps import Caps
from interface.base.request_raw import Base_requests


class userInfo_pro:

    def __init__(self, environment=''):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # phoneSale/addOrder 电销中心_新增订单
    def addOrder(self, data, headers='', cookies=''):
        url = self.caps['admin'] + 'api/v2.0.0/UserInformation/phoneSale/addOrder'
        res = self.re.post_json(url=url, datas=data, headers=headers, cookies=cookies)
        return res

    # 查询订单详情
    def orderList(self, datas, headers='', cookies=''):
        url = self.caps['admin'] + 'api/v2.0.0/UserInformation/order/OrderList'
        res = self.re.post_json(url=url, datas=datas, headers=headers, cookies=cookies)
        return res
