# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 10:49
# @Author  : dujun
# @File    : test_price.py
# @describe:
import time

from interface.data.CRM_Account import username, account
from interface.data.order_data import crm_order_data, save_electricalData
from interface.project.crm.manage import crm_pro


class crm_manage(object):
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

    def __init__(self, loginName, env=''):
        if crm_manage.init_flag is False:
            crm_manage.init_flag = True
        self.crm = crm_pro(environment=env)
        payload = account(user=loginName)
        re = self.crm.crm_login(datas=payload)
        self.token = re['data']['token']
        self.headers = {
            # 'Accept': 'application/json',
            "Content-Type": "application/json",
            'token': self.token
        }

    # CRM广告列表_修改广告
    def updateAdvertising(self, datas):
        re = self.crm.updateAdvertising(headers=self.headers, datas=datas)
        print('CRM广告列表_修改广告', re)
        return re

    # 截单_待分配列表
    def undistributed(self):
        header_data = {
            'token': self.token
        }
        re = self.crm.undistributed(headers=header_data)
        print('截单_待分配列表', re)
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
        res = self.crm.chargeBack(headers=self.headers, datas=payload)
        print(res)

    # 待分配列表-查询按钮状态(截单按钮)
    def getCutStatus(self):
        headers = {
            'token': self.token
        }
        res = self.crm.getCutStatus(headers=headers)
        return res

    # crm添加广告
    def addAdvertising(self, payload):
        res = self.crm.addAdvertising(headers=self.headers, datas=payload)
        # print('添加广告', res)
        return res

    # 查询广告列表
    def advertisingList(self, companyName='', advertisingName='', electricalStatus=''):
        """
        :param advertisingName: 广告名称
        :param companyName: 公司名称
        :param electricalStatus: 是否电核 0 非电核  1：电核
        """
        payload = {
            'electricalStatus': electricalStatus,
            'companyName': companyName,
            'advertisingName': advertisingName,

        }
        res = self.crm.advertisingList(headers=self.headers, params=payload)
        advertList = res['data']['records']
        return advertList

    # 待分配列表--置位电核单
    def setOrder(self, ID):
        payload = {
            "id": ID
        }
        res = self.crm.setOrder(headers=self.headers, datas=payload)
        return res

    # CRM-充值-余额
    def recharge(self, companyName, threadMoney):
        payload = {
            "companyName": companyName,
            "threadMoney": threadMoney
        }
        res = self.crm.recharge(headers=self.headers, datas=payload)
        # print('CRM-充值-余额', res)
        return res

    # CRM-退款
    def refund(self, companyName, threadMoney):
        payload = {
            "companyName": companyName,
            "threadMoney": threadMoney
        }
        res = self.crm.refund(headers=self.headers, datas=payload)
        # print('CRM-账户退款', res)
        return res

    # CRM- 线索推送广告
    def push(self, advertisingId, thinkLoanId, companyName):
        """
        :param advertisingId: 广告ID
        :param thinkLoanId: 线索ID
        :param companyName: 公司名称
        :return:
        """
        payload = {
            'advertisingId': advertisingId,
            'thinkLoanId': thinkLoanId,
            'companyName': companyName

        }
        res = self.crm.push(headers=self.headers, datas=payload)
        print('CRM- 线索推送广告', res)
        return res

    # CRM-广告状态
    def openStatus(self, ID, isOpen):
        """
        :param ID: 广告ID
        :param isOpen: 0：关  1 ：开
        """
        payload = {
            'id': ID,
            'isOpen': isOpen
        }
        res = self.crm.openStatus(headers=self.headers, datas=payload)
        return res

    # 电销开放平台-填单
    def apply(self, phone, cityName):
        payload = crm_order_data(phone=phone, cityName=cityName)
        res = self.crm.apply(headers=self.headers, datas=payload)
        print('电销平台填单', res)
        return res

    # 更新截单按钮状态
    def cutStatus(self, types, status):
        """
        :param types:  1:自动填单  2：手动填单
        :param status: 0:关闭  1：开启
        """
        payloads = {
            'type': types,
            "status": status
        }
        res = self.crm.cutStatus(headers=self.headers, datas=payloads)
        return res

    # 充值明细列表
    def rechargeList(self, companyName=None, orderNo=None, startTime='', endTime=''):
        startTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 00:00:00'
        endTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 23:59:59'
        if startTime == '' and endTime == '':
            payloads = {
                "companyName": companyName,
                "orderNo": orderNo,
                "startTime": startTime_today,
                "endTime": endTime_today,
                "pageNum": 1,
                "pageSize": 10
            }
        else:
            payloads = {
                "companyName": companyName,
                "orderNo": orderNo,
                "startTime": startTime,
                "endTime": endTime,
                "pageNum": 1,
                "pageSize": 10
            }
        res = self.crm.rechargeList(headers=self.headers, datas=payloads)
        rechargeList = res['data']['records']
        # print('充值明细列表',rechargeList)
        return rechargeList

    # 退款明细列表
    def refundList(self, companyName=None, orderNo=None, startTime='', endTime=''):
        startTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 00:00:00'
        endTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 23:59:59'
        if startTime == '' and endTime == '':
            payloads = {
                "companyName": companyName,
                "orderNo": orderNo,
                "startTime": startTime_today,
                "endTime": endTime_today,
                "pageNum": 1,
                "pageSize": 10
            }
        else:
            payloads = {
                "companyName": companyName,
                "orderNo": orderNo,
                "startTime": startTime,
                "endTime": endTime,
                "pageNum": 1,
                "pageSize": 10
            }
        res = self.crm.refundList(headers=self.headers, datas=payloads)
        refundList = res['data']['records']
        return refundList

    #  消耗明细列表
    def consumeList(self, companyName=None, adName=None, Id=None, startTime='', endTime=''):
        startTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 00:00:00'
        endTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 23:59:59'
        if startTime == '' and endTime == '':
            payload = {
                "companyName": companyName,
                'adName': adName,
                "id	": Id,
                "startTime": startTime_today,
                "endTime": endTime_today,
                "pageNum": 1,
                "pageSize": 10
            }
        else:
            payload = {
                "companyName": companyName,
                'adName': adName,
                "id	": Id,
                "startTime": startTime,
                "endTime": endTime,
                "pageNum": 1,
                "pageSize": 10
            }
        res = self.crm.consumeList(headers=self.headers, datas=payload)
        consumeList = res['data']['records']
        return consumeList

    # CRM管理-交易列表
    def adTradeList(self, companyName=None, startTime='', endTime=''):
        startTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 00:00:00'
        endTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 23:59:59'
        if startTime == '' and endTime == '':
            payload = {
                "companyName": companyName,
                "startTime": startTime_today,
                "endTime": endTime_today,
                "pageNum": 1,
                "pageSize": 10
            }
        else:
            payload = {
                "companyName": companyName,
                "startTime": startTime,
                "endTime": endTime,
                "pageNum": 1,
                "pageSize": 10
            }
        res = self.crm.adTradeList(headers=self.headers, datas=payload)
        rechargeList = res['data']['records']
        return rechargeList

    # 添加产品
    def add(self, payload):
        """
        :param payload: { productName: 产品名称, companyName:公司名称, loanLinesMin:贷款额度(万), loanDeadline:贷款期限,
         rateUnit：利率单位, rate:利率, oneTimeCost:一次性费用 ，loanTime：放款时间，description：描述 }
        """
        res = self.crm.add(headers=self.headers, datas=payload)
        print('添加产品', res)
        return res

    # 修改产品
    def update(self, payload):
        res = self.crm.update(headers=self.headers, datas=payload)
        print('修改产品', res)
        return res

    # 产品列表
    def product_list(self, companyName=None, productName=None):
        payload = {
            'companyName': companyName,
            'productName': productName,
            'pageNum': 1,
            'pageSize': 10
        }
        res = self.crm.product_list(headers=self.headers, params=payload)
        product_list = res['data']['records']
        print('产品列表', product_list)
        return product_list

    # 删除产品
    def delete_product(self, productId):
        res = self.crm.delete_product(headers=self.headers, productId=productId)
        print('删除产品', res)
        return res

    # 删除广告
    def delete_advertising(self, adID):
        res = self.crm.delete_advertising(headers=self.headers, adId=adID)
        print('删除广告', res)
        return res

    # 电销中心列表
    def electrical(self, phone, realname=''):
        payload = {
            'pageNum': '1',
            'pageSize': '10',
            'phone': phone,
            'realname': realname,
        }
        headers = {
            'token': self.token
        }
        res = self.crm.electrical(headers=headers, params=payload)
        electrical_list = res['data']['records']
        return electrical_list

    # 电销中心_保存订单
    def electrical_save(self, loanID):
        payload = save_electricalData(loanId=loanID)
        res = self.crm.electrical_save(headers=self.headers, datas=payload)
        print(res)
        return res

    # 电销详情-符合条件广告列表
    def eligible_list(self, loanID):
        payload = {
            'pageNum': '1',
            'pageSize': '10',
            'id': loanID
        }
        headers = {
            'token': self.token
        }
        res = self.crm.eligible_list(headers=headers, params=payload)
        eligible_lists = res['data']['records']
        return eligible_lists

    # 电销详情_推送订单(定制需电核)
    def eligible_push(self, advertisingId, thinkLoanId, companyName):
        """
        :param advertisingId: 广告ID
        :param thinkLoanId: 订单ID
        :param companyName: 公司名称
        """
        payload = {
            'advertisingId': advertisingId,
            'thinkLoanId': thinkLoanId,
            'companyName': companyName
        }
        res = self.crm.eligible_push(headers=self.headers, datas=payload)
        return res

    # 截单列表-已分配列表
    def distributed_list(self, loanId=None):
        payload = {
            'pageNum': '1',
            'pageSize': '10',
            'loanId': str(loanId)
        }
        headers = {
            'token': self.token
        }
        res = self.crm.distributed_list(headers=headers, params=payload)
        distributed_lists = res['data']['records']
        return distributed_lists

    # 已分配列表-线索详情
    def already_detail(self, loanID):
        headers = {
            'token': self.token
        }
        res = self.crm.already_detail(headers=headers, loanID=loanID)
        detail_list = res['data']
        return detail_list

    # 电销详情-提交订单
    def submitOrder(self, loanID):
        payload = {
            'loanId': loanID
        }
        res = self.crm.submitOrder(headers=self.headers, datas=payload)
        return res


if __name__ == "__main__":
    run = crm_manage(username['管理员'], env='')
    run.electrical_save(3408)
