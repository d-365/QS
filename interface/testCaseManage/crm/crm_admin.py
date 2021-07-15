# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 10:49
# @Author  : dujun
# @File    : crm_admin.py
# @describe:
import time

from interface.data.CRM_Account import account
from interface.project.crm.backend import backend_pro


class crm_admin:
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self, loginName, env):
        if crm_admin.init_flag is False:
            crm_admin.init_flag = True
        self.backend = backend_pro(environment=env)
        payload = account(user=loginName)
        re = self.backend.login(datas=payload)
        self.userId = re['data']['userEntity']['id']
        self.token = re['data']['token']
        self.headers = {
            'Content-Type': 'application/json',
            'token': self.token
        }

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

    # 多融客-客户管理-全部线索
    def customerList(self, startTime='', endTime=''):
        startTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 00:00:00'
        endTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 23:59:59'
        if startTime == '' and endTime == '':
            payload = {
                'startTime': startTime_today,
                'endTime': endTime_today,
            }
        else:
            payload = {
                'startTime': startTime,
                'endTime': endTime,
            }
        res = self.backend.customerList(datas=payload, headers=self.headers)
        clientList = res['data']['records']
        print('多融客-客户管理-客户列表', clientList)
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
            'ids': [Id]
        }
        res = self.backend.deleteCustomer(datas=payload, headers=self.headers)
        print("删除客户", res)
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

    # 多融客，修改广告信息
    def editAd(self, ID, budgetConfig, cpcPrice):
        """
        :param ID: 广告ID
        :param budgetConfig: 每日预算
        :param cpcPrice: CPC出价
        :return:
        """
        payload = {
            'id': ID,
            'budgetConfig': budgetConfig,
            'cpcPrice': cpcPrice

        }
        res = self.backend.editAd(headers=self.headers, datas=payload)
        # print('多融客，修改广告信息', res)
        return res

    # 账户总览
    def detail(self):
        headers = {
            'token': self.token
        }
        res = self.backend.detail(headers=headers)
        # print('账户总览',res)
        return res

    # 修改账户日预算
    def update(self, dayBudget):
        """
        :param dayBudget: 日预算
        :return:
        """
        payload = {
            'dayBudget': dayBudget
        }
        res = self.backend.update(headers=self.headers, datas=payload)
        return res

    # 公海列表
    def commonCustomerList(self, adId=None, startTime='', endTime=''):
        startTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 00:00:00'
        endTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 23:59:59'
        if startTime == '' and endTime == '':
            payload = {
                'adId': adId,
                'startTime': startTime_today,
                'endTime': endTime_today,
                'pageSize': 10,
                'pageNum': 1
            }
        else:
            payload = {
                'adId': adId,
                'startTime': startTime,
                'endTime': endTime,
                'pageSize': 10,
                'pageNum': 1
            }

        res = self.backend.commonCustomerList(headers=self.headers, datas=payload)
        commonCustomerList = res['data']['records']
        print('公海列表', commonCustomerList)
        return commonCustomerList

    # 财务管理 - -查询账户记录
    def record(self, startTime='', endTime='', types=None):
        """
        :param endTime:
        :param startTime:
        :param types: 0：充值 ，1：退款 ，2：CPC结算
        :return:
        """
        startTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 00:00:00'
        endTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 23:59:59'
        if startTime == '' and endTime == '':
            payload = {
                'startTime': startTime_today,
                'endTime': endTime_today,
                'type': types,
                'pageSize': 10,
                'pageNum': 1
            }
        else:
            payload = {
                'startTime': startTime,
                'endTime': endTime,
                'type': types,
                'pageSize': 10,
                'pageNum': 1
            }
        res = self.backend.record(headers=self.headers, params=payload)
        record_list = res['data']['records']
        # print('多融客--财务管理--查询账户记录',record_list)
        return record_list

    # 客户管理--全部线索
    def customerDetail(self, Id):
        payload = {
            'id': Id
        }
        res = self.backend.customerDetail(headers=self.headers, params=payload)
        customerDetail = res['data']
        return customerDetail

    # 全部线索,订单分配
    def allotCustomer(self, ids, userId=''):
        """
        :param userId: 用户ID
        :param ids: 订单ID 列表格式 [**]
        """
        if userId == '':
            payload = {
                'userId': self.userId,
                'ids': ids
            }
        else:
            payload = {
                'userId': userId,
                'ids': ids
            }
        res = self.backend.allotCustomer(headers=self.headers, datas=payload)
        return res

    # 多融客-客户管理_我的线索
    def myCustomerList(self, adId=''):
        payload = {
            'pageNum': 1,
            'pageSize': 10,
            'adId': adId
        }
        res = self.backend.myCustomerList(headers=self.headers, datas=payload)
        myCustomerList = res['data']['records']
        return myCustomerList

    # 多融客-我的线索-放入公海
    def throwCustomer(self, loanId):
        payload = {
            'id': loanId
        }
        res = self.backend.throwCustomer(headers=self.headers, datas=payload)
        print(res)
        return res

    # 多融客-公海-我来跟进
    def followCustomer(self, loanId):
        payload = {
            'id': loanId
        }
        res = self.backend.followCustomer(headers=self.headers, datas=payload)
        return res


if __name__ == "__main__":
    run = crm_admin(env='', loginName='interface_gs_manage')
    print(run.record(types=1))
