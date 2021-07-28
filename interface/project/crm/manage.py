# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 10:19
# @Author  : dujun
# @File    : manage.py
# @describe:
from interface.base.base_request import base_requests
from interface.base.caps import Caps
from interface.base.request_raw import Base_requests


class crm_pro:

    def __init__(self, environment=''):
        self.re = Base_requests()
        self.caps = Caps(env=environment)
        self.req = base_requests()

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

    # 待分配列表-查询截单按钮状态
    def getCutStatus(self, headers):
        url = self.caps['crm'] + 'api/crm/config/getCutStatus'
        res = self.re.Get(url=url, headers=headers)
        return res

    # 添加广告
    def addAdvertising(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/advertising/addAdvertising'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # CRM管理-交易列表
    def adTradeList(self, headers, datas):
        url = self.caps['crm'] + 'api/backend/adTrade/adTradeList'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 更新截单按钮状态
    def cutStatus(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/config/updateCutStatus'
        res = self.re.put_json(url=url, headers=headers, datas=datas)
        return res

    # 查询广告列表
    def advertisingList(self, headers, params):
        url = self.caps['crm'] + 'api/crm/advertising/list'
        res = self.re.get(url=url, headers=headers, params=params)
        return res

    # 待分配列表--置位电核单
    def setOrder(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/advertising/setOrder'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # CRM-充值-余额
    def recharge(self, headers, datas):
        url = self.caps['crm'] + 'api/backend/adTrade/recharge'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # CRM-退款-余额
    def refund(self, headers, datas):
        url = self.caps['crm'] + 'api/backend/adTrade/refund'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # CRM-推送订单
    def push(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/loan/order/push'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # CRM-广告状态
    def openStatus(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/advertising/update/openStatus'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 电销开放平台-填单
    def apply(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/telemarketing/apply'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 充值明细列表
    def rechargeList(self, headers, datas):
        url = self.caps['crm'] + 'api/backend/finance/rechargeList'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 退款明细列表
    def refundList(self, headers, datas):
        url = self.caps['crm'] + 'api/backend/finance/refundList'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 消耗明细列表
    def consumeList(self, headers, datas):
        url = self.caps['crm'] + 'api/backend/finance/consumeList'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 添加产品
    def add(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/product/save'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 修改产品
    def update(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/product/update'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # 产品列表
    def product_list(self, headers, params):
        url = self.caps['crm'] + 'api/crm/product/list'
        res = self.re.Get(url=url, headers=headers, params=params)
        return res

    # 删除产品
    def delete_product(self, headers, productId):
        url = self.caps['crm'] + 'api/crm/product/%d' % productId
        res = self.re.delete(url=url, headers=headers)
        return res

    # 删除产品
    def delete_advertising(self, headers, adId):
        url = self.caps['crm'] + 'api/crm/product/%d' % adId
        res = self.re.delete(url=url, headers=headers)
        return res

    # 电销中心列表
    def electrical(self, headers, params):
        url = self.caps['crm'] + 'api/crm/electrical/list'
        res = self.req.request(method='get', url=url, headers=headers, data=params)
        return res

    # 电销中心列表
    def electrical_save(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/electrical/save'
        res = self.req.request(method='post', url=url, data_is_json=True, headers=headers, data=datas)
        return res

    # 电销详情-符合条件广告列表
    def eligible_list(self, headers, params):
        url = self.caps['crm'] + 'api/crm/electrical/eligible/list'
        res = self.req.request(method='get', url=url, headers=headers, data=params)
        return res

    # 电销详情_推送订单(定制需电核)
    def eligible_push(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/electrical/push'
        res = self.req.request(method='post', data_is_json=True, url=url, headers=headers, data=datas)
        return res

    # 截单列表-已分配列表
    def distributed_list(self, headers, params):
        url = self.caps['crm'] + 'api/crm/loan/order/distributed/list'
        res = self.req.request(method='get', url=url, headers=headers, data=params)
        return res

    # 已分配列表-线索详情
    def already_detail(self, headers, loanID):
        url = self.caps['crm'] + 'api/crm/loan/order/already/detail?id={}'.format(loanID)
        res = self.req.request(method='get', url=url, headers=headers)
        return res

    # 电销详情-提交订单
    def submitOrder(self, headers, datas):
        url = self.caps['crm'] + 'api/crm/electrical/submitOrder'
        res = self.req.request(method='post', url=url, headers=headers, data_is_json=True, data=datas)
        return res

    # 新增总代理商账户
    def addUser(self, headers, datas):
        url = self.caps['crm'] + 'api/backend/tmk/user/addUser'
        res = self.req.request(method='post', url=url, headers=headers, data=datas,data_is_json=True)
        return res

    # 开放平台账号列表
    def userList(self, headers, datas):
        url = self.caps['crm'] + 'api/backend/tmk/user/userList'
        res = self.req.request(method='get', url=url, headers=headers, data=datas)
        return res

    # 删除总代理账号
    def delUser(self, headers, datas):
        url = self.caps['crm'] + 'api/backend/tmk/user/delUser'
        res = self.req.request(method='post', url=url, headers=headers, data=datas,data_is_json=True)
        return res

    # 全部线索--恢复已删除客户
    def recoverCustomer(self, headers, datas):
        url = self.caps['crm'] + 'api/backend/customer/recoverCustomer'
        res = self.req.request(method='post', url=url,data_is_json=True, headers=headers, data=datas)
        return res

    # 电销开放平台--订单列表
    def tmk_list(self,headers,datas):
        url = self.caps['crm'] + 'api/crm/tmk/list'
        res = self.req.request(method='get', url=url, headers=headers,data=datas,data_is_json=True)
        return res

    # 更新总代理商账户状态
    def updateStatus_total(self,headers,datas):
        url = self.caps['crm'] + 'api/backend/tmk/user/updateStatus'
        res = self.req.request(method='post', url=url, headers=headers,data=datas,data_is_json=True)
        return res
