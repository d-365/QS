# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 10:19
# @Author  : dujun
# @File    : manage.py
# @describe:

from interface.base.caps import Caps
from interface.base.requests import Base_requests


class crm_pro:

    def __init__(self, environment=''):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # 多融客CRM登录
    def crm_login(self, datas):
        url = self.caps['crm'] + 'api/backend/user/login'
        res = self.re.post_json(url=url, datas=datas)
        return res

    # 截单_待分配列表
    def undistributed(self, headers):
        url = self.caps['crm'] + 'api/crm/loan/order/undistributed/list'
        res = self.re.Get(url=url, headers=headers)
        return res

    # 截单_待分配列表-退还订单
    def chargeBack(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/loan/order/chargeBack'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # CRM广告列表_修改广告
    def updateAdvertising(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/advertising/updateAdvertising'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 待分配列表-查询按钮状态(截单按钮)
    def getStatus(self, headers):
        url = self.caps['crm'] + 'api/crm/loan/order/getStatus'
        res = self.re.Get(url=url, headers=headers)
        return res

    # 添加广告
    def addAdvertising(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/advertising/addAdvertising'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # CRM管理-交易列表
    def adTradeList(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/advertising/addAdvertising'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 更新截单按钮状态
    def cutStatus(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/loan/order/update/cutStatus'
        res = self.re.put_json(url=url, headers=headers, datas=datas)
        return res

    # 查询广告列表
    def advertisingList(self, headers, params):
        url = self.caps['crm'] + 'api/crm/advertising/list'
        res = self.re.get(url=url, headers=headers, params=params)
        return res

    # 待分配列表--置位电核单
    def setOrder(self,headers,datas):
        url = self.caps['crm'] + 'api/crm/advertising/setOrder'
        res = self.re.post_json(url=url,headers=headers,datas=datas)
        return res