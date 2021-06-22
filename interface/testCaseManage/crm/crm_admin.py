# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 10:49
# @Author  : dujun
# @File    : crm_admin.py
# @describe:

from interface.data.CRM_Account import username, account
from interface.project.crm.backend import backend_pro


class crm_admin:

    def __init__(self, loginName, env):
        self.backend = backend_pro(environment=env)
        payload = account(user=loginName)
        re = self.backend.login(datas=payload)
        self.token = re['data']['token']
        self.headers = {
            'Content-Type': 'application/json',
            'token': self.token
        }

    # # CRM后台-登录
    # def login(self, account, password):
    #     """
    #     :param account: 员工账号
    #     :param password: 密码，前端需要MD5加密
    #     :return: 登录headers信息
    #     """
    #     payload = {
    #         'account': account,
    #         'password': password,
    #         'validate': ''
    #     }
    #     res = self.backend.login(datas=payload)
    #     return res

    # CRM后台-登录-获取登录信息
    def getLoginInfo(self):
        res = self.backend.getLoginInfo(headers=self.headers)
        return res

    # CRM管理-交易列表-充值
    def recharge(self, companyName, adId, threadNum, threadMoney):
        """
        :param companyName: 公司名称
        :param adId: 广告id
        :param threadNum: 线索数量
        :param threadMoney:套餐金额
        """
        payload = {
            'companyName': companyName,
            'adId': adId,
            'threadNum': threadNum,
            'threadMoney': threadMoney
        }
        res = self.backend.recharge(datas=payload, headers=self.headers)
        return res

    # CRM管理-交易列表-退款
    def refund(self, ID, threadNum, threadMoney, companyName, adId):
        """
        :param ID: 交易id
        :param threadNum: 退款线索
        :param threadMoney:退款金额
        :param companyName: 公司名称
        :param adId: 广告id
        """
        payload = {
            'id': ID,
            'threadNum': threadNum,
            'threadMoney': threadMoney,
            'companyName': companyName,
            'adId': adId
        }
        res = self.backend.refund(datas=payload, headers=self.headers)
        return res

    # CRM管理-消耗记录
    def consumeList(self, companyName='', adName='', adCreatorId='', startTime='', endTime=''):
        """
        CRM管理-消耗记录
        :param companyName: 公司名称
        :param adName: 广告名称
        :param adCreatorId: 客户经理id
        :param startTime: 交易时间开始时间
        :param endTime: 交易时间结束时间
        """
        payload = {
            'companyName': companyName,
            'adName	': adName,
            'adCreatorId': adCreatorId,
            'startTime': startTime,
            'endTime': endTime
        }
        res = self.backend.consumeList(datas=payload, headers=self.headers)
        return res

    # 系统设置-员工账号-编辑（新增、更新）员工信息
    def editStaff(self, accounts, name, password, role, status, ID=''):
        """
        系统设置-员工账号-编辑（新增、更新）员工信息
        :param accounts: 账号
        :param name: 姓名
        :param password: 密码
        :param role: 角色id
        :param status: 状态  true 启用 false禁用
        :param ID: 账户id,当更新操作必须传id
        """
        payload = {
            'account': accounts,
            'name': name,
            'password': password,
            'role': role,
            'status': status,
            'id': ID
        }
        res = self.backend.editStaff(datas=payload, headers=self.headers)
        return res

    # CRM后台-角色管理-新增角色
    def addRole(self, roleNam):
        """
        CRM后台-角色管理-新增角色
        :param roleNam: 角色名
        """
        payload = {
            'roleName': roleNam
        }
        res = self.backend.addRole(datas=payload, headers=self.headers)
        print(res)
        return res

    # CRM后台-角色管理-删除角色
    def deleteRole(self, ID):
        """
        CRM后台-角色管理-删除角色
        :param ID: 角色id
        """
        payload = {
            'id	': ID
        }
        res = self.backend.deleteRole(datas=payload, headers=self.headers)
        print(res)
        return res

    # CRM后台-角色管理-设置角色权限
    def editRolePermission(self, ID, permissionUrl):
        """
        CRM后台-角色管理-设置角色权限
        :param ID: 角色id
        :param permissionUrl: 角色可以访问菜单的路径 [ string ]
        """
        payload = {
            'id	': ID,
            'permissionUrl': permissionUrl
        }
        res = self.backend.editRolePermission(datas=payload, headers=self.headers)
        print(res)
        return res

    # CRM后台-角色管理-角色列表
    def roleList(self, roleName=''):
        """
        CRM后台-角色管理-角色列表
        :param roleName: 角色名称
        """
        payload = {
            'roleName': roleName
        }
        res = self.backend.roleList(datas=payload, headers=self.headers)
        print(res)
        return res

    # 系统设置-CRM账号-CRM用户列表
    def userList(self, ID, permissionUrl):
        """
        系统设置-CRM账号-CRM用户列表
        :param ID: 角色id
        :param permissionUrl: 角色可以访问菜单的路径 [ string ]
        """
        payload = {
            'id	': ID,
            'permissionUrl': permissionUrl
        }
        res = self.backend.editRolePermission(datas=payload, headers=self.headers)
        print(res)
        return res

    # 多融客CRM-广告管理-更新广告状态
    def editAdIsOpen(self, Id, isOpen):
        """
        :param Id: 广告id
        :param isOpen: 是否打开  true打开 false关闭
        """
        payload = {
            'id': Id,
            'isOpen': isOpen
        }
        res = self.backend.editAdIsOpen(datas=payload, headers=self.headers)
        return res

    # 多融客CRM-广告管理-查看广告详情
    def adDateil(self, Id):
        """
        :param Id: 广告id
        """
        payload = {
            'id': Id
        }
        res = self.backend.adDateil(params=payload, headers=self.headers)
        print(res)
        return res

    # 多融客CRM - 交易记录 - 交易记录列表
    def tradeList(self, adName, Type):
        """
        :param adName: 广告名称
        :param Type: 交易类型 number
        :return:
        """
        payload = {
            "adName": adName,
            "type": Type,
            "pageIndex": None,
            "pageSize": None
        }
        res = self.backend.tradeList(headers=self.headers, datas=payload)
        print(res)
        return res

    # 多融客-客户管理-客户列表
    def customerList(self, adName='',phone=''):
        """
        adName: 广告名称--非必填
        """
        payload = {
            'adName': adName,
            'pageSize':10,
            'pageNum':1,
            'phone':phone,
        }
        res = self.backend.customerList(datas=payload, headers=self.headers)
        clientList = res['data']['records']
        print('多融客-客户管理-客户列表',clientList)
        return clientList

    # 多融客-客户管理-导出客户列表
    def exportCustomer(self):
        """
        adId：广告id
        name：客户姓名
        phone：联系方式
        startTime：对接时间开始时间
        endTime：对接时间结束时间
        """
        params = {
            'adId': '',
            'name': '',
            'phone': '',
            'startTime': '',
            'endTime': ''
        }
        headers = {

        }
        res = self.backend.exportCustomer(params=params, headers=headers)
        return res

    # 多融客-客户管理-客户跟进列表
    def followList(self, ID):
        """
        :param ID: 订单id
        """
        payload = {
            'id': ID
        }
        headers = {}
        res = self.backend.followList(params=payload, headers=headers)
        return res

    # 多融客 - 客户管理- 删除客户
    def deleteCustomer(self, Id):
        """
        :param Id:订单id
        """
        payload = {
            'id': Id
        }
        res = self.backend.deleteCustomer(datas=payload, headers=self.headers)
        print(res)
        return res

    # 多融客 - 客户管理- 新建跟进
    def addFollow(self, orderId, customerIntention, followWay, followContext=''):
        """
        :param orderId: 所跟进订单id
        :param customerIntention: 客户意向 // 0-高，1-中，2-低
        :param followWay: 跟进方式 // 0-线上沟通，1-电话沟通，2-上门拜访，3-其他方式
        :param followContext: 跟进内容
        """
        payload = {
            'orderId': orderId,
            'customerIntention': customerIntention,
            'followWay': followWay,
            'followContext': followContext
        }
        res = self.backend.addFollow(datas=payload, headers=self.headers)
        print(res)
        return res

    # 多融客CRM-广告管理-广告列表
    def getAdListByName(self, adName):
        """
        :param adName: 广告名称
        """
        payload = {
            'adName': adName
        }
        res = self.backend.getAdListByName(datas=payload, headers=self.headers)
        print(res)
        return res

    def editAd(self,ID,budgetConfig,cpcPrice):
        """
        :param ID: 广告ID
        :param budgetConfig: 每日预算
        :param cpcPrice: CPC出价
        :return:
        """
        payload = {
            'id':ID,
            'budgetConfig':budgetConfig,
            'cpcPrice':cpcPrice

        }
        res = self.backend.editAd(headers=self.headers, datas=payload)
        print(res)
        return res

    # 根据公司查询账户余额
    def getCompanyMoney(self,companyName):
        payload = {
            'companyName':companyName,
            'token': self.token
        }
        headers = {
            'token': self.token
        }
        res = self.backend.getCompanyMoney(headers=headers, datas=payload)
        print(res)
        return res


if __name__ == "__main__":
    run = crm_admin(env='', loginName=username['interface_gs_manage'])
    run.getCompanyMoney(companyName='dujun_gs_001')
