# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 15:00
# @Author  : dujun
# @File    : crm_general.py
# @describe: CRM接口自动化常用方法和断言封装
import time
from interface.data.CRM_Account import username
from interface.data.order_data import order_data
from interface.testCaseManage.api_manage.App_addOrder import addOrder
from interface.testCaseManage.crm.crm_admin import crm_admin
from interface.testCaseManage.crm.crm_manage import crm_manage


class crm_general:

    def __init__(self):
        self.crmManege = crm_manage(username['管理员'], env='')
        self.crm_admin = crm_admin(env='', loginName='interface_gs_manage')

    # CRM添加广告,条件不限制,返回广告ID
    def add_Advertising(self, ad_data, cpcPrice):
        """
        :param ad_data: 广告数据
        :param cpcPrice: CPC出价
        :return: 广告ID
        """

        self.crmManege.addAdvertising(payload=ad_data)
        # 查询广告ID
        advert_list = self.crmManege.advertisingList(companyName=ad_data['companyName'],
                                                     advertisingName=ad_data['advertisingName'],
                                                     electricalStatus=ad_data['electricalStatus'])
        advert_id = advert_list[0]['id']
        # 修改订单CPC出价
        self.crm_admin.editAd(ID=advert_id, budgetConfig=99999, cpcPrice=cpcPrice)
        return advert_id

    # 断言多融客全部线索下是否存在指定订单
    def assert_customList(self, loanId):
        time.sleep(2)
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

    def setup_recharge(self, companyName):
        # 充值
        self.crmManege.recharge(companyName=companyName, threadMoney='999999')
        # 设置账户日预算
        self.crm_admin.update(dayBudget=99999)

    # 生成任意订单,推送给对应广告(定制需电核)
    def push_order(self, companyName, adName, electricalStatus, cpcPrice):
        self.crmManege.cutStatus(types=2, status=1)
        crm_general().setup_recharge(companyName=companyName)
        companyName = "dujun_gs_001"
        customPlan = 1
        ad_data = {"companyName": companyName, "advertisingName": adName, "electricalStatus": electricalStatus,
                   "putCity": "全国", "status": 1, "suggestedPrice": 6, "customPlan": customPlan, "requirement": {},
                   "noRequirement": {}, "remark": "interface"}
        self.crmManege.addAdvertising(payload=ad_data)
        # 查询广告ID
        advert_list = self.crmManege.advertisingList(companyName=companyName, advertisingName=adName,
                                                     electricalStatus=electricalStatus)
        advert_id = advert_list[0]['id']
        # 修改订单CPC出价
        self.crm_admin.editAd(ID=advert_id, budgetConfig=99999, cpcPrice=cpcPrice)

        # 信业帮发起订单
        payload = order_data(city_name='安顺市')
        appAddOrder = addOrder(env='', phone='11111111119')
        loanId = appAddOrder.get_loanId().app_addOrder(payload)
        # 推送对应广告
        print('线索ID：', loanId, '广告ID：', advert_id)
        time.sleep(2)
        self.crmManege.push(advertisingId=advert_id, thinkLoanId=loanId, companyName=companyName)
        return loanId, advert_id

    # CRM添加定制需电核广告
    def add_custom_yes(self, cpcPrice):
        """
        :param cpcPrice: CPC出价
        :return: 订单ID
        """
        companyName = "dujun_gs_001"
        advertisingName = 'custom_yes'
        electricalStatus = 1
        customPlan = 1
        ad_data = {"companyName": companyName, "advertisingName": advertisingName, "electricalStatus": electricalStatus,
                   "putCity": "全国", "status": 1, "suggestedPrice": 6, "customPlan": customPlan, "requirement": {},
                   "noRequirement": {}, "remark": "interface"}
        self.crmManege.addAdvertising(payload=ad_data)
        # 查询广告ID
        advert_list = self.crmManege.advertisingList(companyName=ad_data['companyName'],
                                                     advertisingName=ad_data['advertisingName'],
                                                     electricalStatus=ad_data['electricalStatus'])
        advert_id = advert_list[0]['id']
        # 修改订单CPC出价
        self.crm_admin.editAd(ID=advert_id, budgetConfig=99999, cpcPrice=cpcPrice)
        return advert_id

    # CRM添加定制不需电核广告
    def add_custom_no(self, cpcPrice):
        """
        :param cpcPrice: CPC出价
        :return: 订单ID
        """
        companyName = "dujun_gs_001"
        advertisingName = 'custom_no'
        electricalStatus = 1
        customPlan = 0
        ad_data = {"companyName": companyName, "advertisingName": advertisingName, "electricalStatus": electricalStatus,
                   "putCity": "全国", "status": 1, "suggestedPrice": 6, "customPlan": customPlan, "requirement": {},
                   "noRequirement": {}, "remark": "interface"}
        self.crmManege.addAdvertising(payload=ad_data)
        # 查询广告ID
        advert_list = self.crmManege.advertisingList(companyName=ad_data['companyName'],
                                                     advertisingName=ad_data['advertisingName'],
                                                     electricalStatus=ad_data['electricalStatus'])
        advert_id = advert_list[0]['id']
        # 修改订单CPC出价
        self.crm_admin.editAd(ID=advert_id, budgetConfig=99999, cpcPrice=cpcPrice)
        return advert_id

    # CRM添加定制不需电核广告
    def add_common_no(self, cpcPrice):
        """
        :param cpcPrice: CPC出价
        :return: 订单ID
        """
        companyName = "dujun_gs_001"
        advertisingName = 'common_no'
        electricalStatus = 0
        customPlan = 0
        ad_data = {"companyName": companyName, "advertisingName": advertisingName,
                   "electricalStatus": electricalStatus,
                   "putCity": "全国", "status": 1, "suggestedPrice": 6, "customPlan": customPlan, "requirement": {},
                   "noRequirement": {}, "remark": "interface"}
        self.crmManege.addAdvertising(payload=ad_data)
        # 查询广告ID
        advert_list = self.crmManege.advertisingList(companyName=ad_data['companyName'],
                                                     advertisingName=ad_data['advertisingName'],
                                                     electricalStatus=ad_data['electricalStatus'])
        advert_id = advert_list[0]['id']
        # 修改订单CPC出价
        self.crm_admin.editAd(ID=advert_id, budgetConfig=99999, cpcPrice=cpcPrice)
        return advert_id


if __name__ == "__main__":
    run = crm_general()
