# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 10:19
# @Author  : dujun
# @File    : crm.py
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

    # 多融客-客户管理-客户列表
    def customerList(self, headers, datas=''):
        url = self.caps['crm'] + 'api/crm/customer/customerList'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 多融客 - 客户管理 - 导出客户列表
    def exportCustomer(self, params, headers):
        url = self.caps['crm'] + 'api/crm/customer/exportCustomer'
        res = self.re.Get(url=url, headers=headers, params=params)
        return res

    # 多融客-客户管理-客户跟进列表
    def followList(self, params, headers):
        url = self.caps['crm'] + 'api/crm/follow/followList'
        res = self.re.Get(url=url, headers=headers, params=params)
        return res

    # 多融客 - 客户管理- 删除客户
    def deleteCustomer(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/customer/deleteCustomer'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 多融客-客户管理-新建跟进
    def addFollow(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/follow/addFollow'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 多融客CRM-广告管理-广告列表
    def getAdListByName(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/ad/getAdListByName'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 多融客CRM-广告管理-更新广告状态
    def editAdIsOpen(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/ad/editAdIsOpen'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 多融客CRM-广告管理-查看广告详情
    def adDateil(self, headers, params):
        url = self.caps['crm'] + 'api/crm/ad/adDateil'
        res = self.re.Get(url=url, headers=headers, params=params)
        return res

    # 多融客CRM - 交易记录 - 交易记录列表
    def tradeList(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/adTrade/tradeList'
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
