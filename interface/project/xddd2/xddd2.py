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
    def xddd2_login(self, headers,params):
        url = self.caps['xddd2'] + 'interface/v3.0.0/beforeUser/res'
        res = self.re.get(url=url,headers=headers, params=params)
        return res

    # 密码登录
    def login_password(self, datas):
        url = self.caps['xddd2'] + 'interface/v4.1.0/beforeUser/pRes'
        res = self.re.post_app(url=url, datas=datas)
        return res

    # 好单客源列表
    def orderList(self, headers, params):
        url = self.caps['xddd2'] + 'interface/v3.0.0/order/list'
        res = self.re.get(url=url, headers=headers, params=params)
        return res

    # 更新展位状态
    def changeStatus(self,headers,datas):
        url = self.caps['xddd2'] + 'interface/v3.0.0/ddzw/ddzwinfo/changeStatus'
        res = self.re.post_app(url=url,headers=headers,datas=datas)
        return res

    # 查询展位订单
    def catchOrderList(self,headers,datas):
        url = self.caps['xddd2'] + 'interface/v3.0.0/ddzw/ddzwinfo/catchOrderList'
        res = self.re.post(url=url,headers=headers,data=datas)
        return res


