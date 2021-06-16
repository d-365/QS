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
    def editStaff(self, account, name, password, role, status, ID=''):
        """
        系统设置-员工账号-编辑（新增、更新）员工信息
        :param account: 账号
        :param name: 姓名
        :param password: 密码
        :param role: 角色id
        :param status: 状态  true 启用 false禁用
        :param ID: 账户id,当更新操作必须传id
        """
        payload = {
            'account': account,
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


if __name__ == "__main__":
    run = backend_manage(env='', loginName=username['管理员'])
