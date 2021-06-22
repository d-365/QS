# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 10:20
# @Author  : dujun
# @File    : crm_admin.py
# @describe:

from interface.base.caps import Caps
from interface.base.requests import Base_requests


class backend_pro:

    def __init__(self, environment=''):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # CRM后台-登录
    def login(self, datas):
        url = self.caps['crm_admin'] + 'api/crm/user/login'
        res = self.re.post_json(url=url, datas=datas)
        return res

    # CRM后台-登录-获取登录信息
    def getLoginInfo(self, headers):
        url = self.caps['crm_admin'] + 'api/backend/user/getLoginInfo'
        res = self.re.post(url=url, headers=headers)
        return res

    # CRM管理-交易列表-充值
    def recharge(self, datas, headers):
        url = self.caps['crm_admin'] + 'api/backend/adTrade/recharge'
        res = self.re.post_json(url=url, datas=datas, headers=headers)
        return res

    # CRM管理-交易列表-退款
    def refund(self, datas, headers):
        url = self.caps['crm_admin'] + 'api/backend/adTrade/refund'
        res = self.re.post_json(url=url, datas=datas, headers=headers)
        return res

    # CRM管理-消耗记录
    def consumeList(self, datas, headers):
        url = self.caps['crm_admin'] + 'api/backend/consume/consumeList'
        res = self.re.post_json(url=url, datas=datas, headers=headers)
        return res

    # 系统设置-员工账号-编辑（新增、更新）员工信息
    def editStaff(self, datas, headers):
        url = self.caps['crm_admin'] + 'api/backend/user/editStaff'
        res = self.re.post_json(url=url, datas=datas, headers=headers)
        return res

    # CRM后台-角色管理-新增角色
    def addRole(self, datas, headers):
        url = self.caps['crm_admin'] + 'api/backend/role/addRole'
        res = self.re.post_json(url=url, datas=datas, headers=headers)
        return res

    # CRM后台-角色管理-删除角色
    def deleteRole(self, datas, headers):
        url = self.caps['crm_admin'] + 'api/backend/role/deleteRole'
        res = self.re.post_json(url=url, datas=datas, headers=headers)
        return res

    # CRM后台-角色管理-设置角色权限
    def editRolePermission(self, datas, headers):
        url = self.caps['crm_admin'] + 'api/backend/role/editRolePermission'
        res = self.re.post_json(url=url, datas=datas, headers=headers)
        return res

    # CRM后台-角色管理-角色列表
    def roleList(self, datas, headers):
        url = self.caps['crm_admin'] + 'api/backend/role/roleList'
        res = self.re.post_json(url=url, datas=datas, headers=headers)
        return res

    # 系统设置-CRM账号-CRM用户列表
    def userList(self, datas, headers):
        url = self.caps['crm_admin'] + 'api/backend/crmUser/userList'
        res = self.re.post_json(url=url, datas=datas, headers=headers)
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

    # 多融客-更新广告
    def editAd(self,headers,datas):
        url = self.caps['crm'] + 'api/crm/ad/editAd'
        res = self.re.post_json(url=url,headers=headers,datas=datas)
        return res

    # 根据公司查询账户余额
    def getCompanyMoney(self,headers,datas):
        url = self.caps['crm'] + 'api/backend/adTrade/getCompanyMoney'
        res = self.re.Get(url=url, headers=headers, params=datas)
        return res
