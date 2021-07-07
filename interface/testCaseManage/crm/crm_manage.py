# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 10:49
# @Author  : dujun
# @File    : test_price.py
# @describe:
import time

from interface.data.CRM_Account import username, account
from interface.data.order_data import crm_order_data
from interface.project.crm.manage import crm_pro


class crm_manage:

    def __init__(self, loginName, env=''):
        self.crm = crm_pro(environment=env)
        payload = account(user=loginName)
        re = self.crm.crm_login(datas=payload)
        self.token = re['data']['token']
        self.headers = {
            'Content-Type': 'application/json',
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
    def getStatus(self):
        headers = {
            'token': self.token
        }
        res = self.crm.getStatus(headers=headers)
        return res

    # crm添加广告
    def addAdvertising(self, payload):
        res = self.crm.addAdvertising(headers=self.headers, datas=payload)
        print('添加广告', res)
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

    # CRM-退款-余额
    def refund(self, companyName, threadMoney):
        payload = {
            "companyName": companyName,
            "threadMoney": threadMoney
        }
        res = self.crm.refund(headers=self.headers, datas=payload)
        print('CRM-退款-余额', res)
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
    def cutStatus(self, status):
        """
        :param status: 0:关闭  1：开启
        """
        payload = {
            "status": status
        }
        res = self.crm.cutStatus(headers=self.headers, datas=payload)
        return res

    # 更新手动截单按钮状态
    def cutStatus1(self, status):
        """
        :param status: 0:关闭  1：开启
        """
        payload = {
            "status": status
        }
        res = self.crm.cutStatus1(headers=self.headers, datas=payload)
        return res

    # 更新自动截单按钮状态
    def cutStatus2(self, status):
        """
        :param status: 0:关闭  1：开启
        """
        payload = {
            "status": status
        }
        res = self.crm.cutStatus2(headers=self.headers, datas=payload)
        return res

    # 充值明细列表
    def rechargeList(self, companyName='', orderNo='', startTime='', endTime=''):
        startTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 00:00:00'
        endTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 23:59:59'
        if startTime == '' and endTime == '':
            payload = {
                "companyName": companyName,
                "orderNo": orderNo,
                "startTime": startTime_today,
                "endTime": endTime_today,
                "pageNum": 1,
                "pageSize": 10
            }
        else:
            payload = {
                "companyName": companyName,
                "orderNo": orderNo,
                "startTime": startTime,
                "endTime": endTime,
                "pageNum": 1,
                "pageSize": 10
            }
        res = self.crm.rechargeList(headers=self.headers, datas=payload)
        rechargeList = res['data']['records']
        return rechargeList

    # 退款明细列表
    def refundList(self, companyName='', orderNo='', startTime='', endTime='', pageNum='', pageSize=''):
        startTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 00:00:00'
        endTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 23:59:59'
        if startTime == '' and endTime == '':
            payload = {
                "companyName": companyName,
                "orderNo": orderNo,
                "startTime": startTime_today,
                "endTime": endTime_today,
                "pageNum": pageNum,
                "pageSize": pageSize
            }
        else:
            payload = {
                "companyName": companyName,
                "orderNo": orderNo,
                "startTime": startTime,
                "endTime": endTime,
                "pageNum": pageNum,
                "pageSize": pageSize
            }
        res = self.crm.refundList(headers=self.headers, datas=payload)
        refundList = res['data']['records']
        return refundList

    #  消耗明细列表
    def consumeList(self, companyName='',adName='', Id='', startTime='', endTime='', pageNum='', pageSize=''):
        startTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 00:00:00'
        endTime_today = time.strftime('%Y-%m-%d', time.localtime()) + ' 23:59:59'
        if startTime == '' and endTime == '':
            payload = {
                "companyName": companyName,
                'adName':adName,
                "id	": Id,
                "startTime": startTime_today,
                "endTime": endTime_today,
                "pageNum": pageNum,
                "pageSize": pageSize
            }
        else:
            payload = {
                "companyName": companyName,
                'adName': adName,
                "id	": Id,
                "startTime": startTime,
                "endTime": endTime,
                "pageNum": pageNum,
                "pageSize": pageSize
            }
        res = self.crm.consumeList(headers=self.headers, datas=payload)
        consumeList = res['data']['records']
        return consumeList

    # CRM管理-交易列表
    def adTradeList(self, companyName='', startTime='', endTime=''):
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


if __name__ == "__main__":
    run = crm_manage(username['管理员'], env='')
    run.apply(phone='13003672580',cityName='安顺市')

