# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 15:00
# @Author  : dujun
# @File    : crm_general.py
# @describe: CRM接口自动化常用方法和断言封装

from interface.data.CRM_Account import username
from interface.testCase.conftest import cmdOption
from interface.testCaseManage.crm.crm_admin import crm_admin
from interface.testCaseManage.crm.crm_manage import crm_manage


class crm_general:

    def __init__(self):
        self.crmManege = crm_manage(username['管理员'], env='')
        self.crm_admin = crm_admin(env='', loginName='interface_gs_manage')

    # CRM添加广告,条件不限制,返回订单ID
    def addAdvertising(self, Advertising_data):
        self.crmManege.addAdvertising(payload=Advertising_data)
        advert_list = self.crmManege.advertisingList(companyName="dujun_gs_001", advertisingName="interface_yes",
                                                     electricalStatus=1)
        # 广告ID
        advert_id = advert_list[0]['id']
        # 设置CPC出价和每日预算
        self.crm_admin.editAd(ID=advert_id, budgetConfig=99999, cpcPrice=25)
        return advert_id

    # 断言多融客公海下是否存在指定订单
    def assert_customList(self,loanId):
        clientList = self.crm_admin.customerList()
        i = 0
        status = False
        while i < len(clientList):
            if loanId == clientList[i]['id']:
                status = True
                break
            else:
                i += 1
        if status is True:
            pass
        else:
            raise Exception("线索", loanId, "不在对应广告中")


if __name__ == "__main__":
    run = crm_general()

