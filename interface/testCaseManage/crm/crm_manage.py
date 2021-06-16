# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 10:49
# @Author  : dujun
# @File    : test_crmBackground.py
# @describe:

from interface.data.CRM_Account import username, account
from interface.project.crm.crm import crm_pro


class crm_manage:

    def __init__(self, loginName, env):
        self.crm = crm_pro(environment=env)
        payload = account(user=loginName)
        re = self.crm.crm_login(datas=payload)
        self.token = re['data']['token']
        self.headers = {
            'Content-Type': 'application/json',
            'token': self.token
        }

    # # 多融客登录
    # def login(self):
    #     """
    #     validate: 易盾校验
    #     """

    # 多融客-客户管理-客户列表
    def customerList(self, adName):
        """
        adName: 广告名称--非必填
        """
        payload = {
            'adName': adName
        }
        res = self.crm.customerList(datas=payload, headers=self.headers)
        return res

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
        res = self.crm.exportCustomer(params=params, headers=headers)
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
        res = self.crm.followList(params=payload, headers=headers)
        return res

    # 多融客 - 客户管理- 删除客户
    def deleteCustomer(self, Id):
        """
        :param Id:订单id
        """
        payload = {
            'id': Id
        }
        res = self.crm.deleteCustomer(datas=payload, headers=self.headers)
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
        res = self.crm.addFollow(datas=payload, headers=self.headers)
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
        res = self.crm.getAdListByName(datas=payload, headers=self.headers)
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
        res = self.crm.editAdIsOpen(datas=payload, headers=self.headers)
        print(res)
        return res

    # 多融客CRM-广告管理-查看广告详情
    def adDateil(self, Id):
        """
        :param Id: 广告id
        """
        payload = {
            'id': Id
        }
        res = self.crm.adDateil(params=payload, headers=self.headers)
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
        res = self.crm.tradeList(headers=self.headers, datas=payload)
        print(res)
        return res

    # CRM广告列表_修改广告
    def updateAdvertising(self):
        payload = {"companyName": "dujun_gs_001", "advertisingName": "gg003", "electricalStatus": 1, "putCity": "杭州市",
                   "status": 0, "requirement": {"loanMoney": 3, "sex": "1,2"}, "noRequirement": {}, "id": 13}
        re = self.crm.updateAdvertising(headers=self.headers, datas=payload)
        print(re)

    # 截单_待分配列表
    def undistributed(self):
        header_data = {
            'token': self.token
        }
        re = self.crm.undistributed(headers=header_data)
        print(re)
        # ID = re['data']['records'][0]['id']
        # return ID

    # 截单_待分配列表-退还订单
    def chargeBack(self, thinkLoanId):
        """
        :param thinkLoanId: 订单ID
        """
        payload = {
            "thinkLoanId": thinkLoanId
        }
        re = self.crm.chargeBack(headers=self.headers, datas=payload)
        print(re)

    # 待分配列表-查询按钮状态(截单按钮)
    def getStatus(self):
        headers = {
            'token': self.token
        }
        res = self.crm.getStatus(headers=headers)
        return res

    # crm添加广告
    def addAdvertising(self):
        payload = {
            "companyName": "dujun_gs_001",  # 公司名称
            "advertisingName": "interface",  # 广告名词
            "electricalStatus": 1,  # 是否电核 1:电核 0:非电核
            "putCity": "北京市",  # 城市
            "status": 1,  # 是否启用 1:启用  0:禁用
            "requirement": {  # 必要条件
                "loanMoney": 3,
                "sex": "1,2"
            },
            "noRequirement": {  # 非必要条件
                "socialSecurity": "3个月以下",
                "providentFund": "3个月以下"
            }
        }
        res = self.crm.addAdvertising(headers=self.headers, datas=payload)
        print(res)


if __name__ == "__main__":
    run = crm_manage(username['客户经理主管'], env='')
    run.addAdvertising()
    run.updateAdvertising()
    run.undistributed()
