# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 17:54
# @Author  : dujun
# @File    : push.py
# @describe: 推单并发

import threading
import time
from interface.data.order_data import order_data
from interface.testCaseManage.api_manage.App_addOrder import addOrder
from interface.testCaseManage.crm.crm_manage import crm_manage


class push:

    def __init__(self):
        self.crm_manage = crm_manage(env='', loginName='manage_interface')

    def case1(self, advertisingId, thinkLoanId):
        self.crm_manage.push(advertisingId=advertisingId, thinkLoanId=thinkLoanId, companyName='dujun_gs_001')

    def case3(self):
        t1 = threading.Thread(target=self.case1, kwargs={'advertisingId': '79', 'thinkLoanId': '10784'})
        t2 = threading.Thread(target=self.case1, kwargs={'advertisingId': '79', 'thinkLoanId': '10933'})
        t1.start()
        t2.start()


class create_order:

    @staticmethod
    def case1(phone):
        api = addOrder(phone=phone)
        payload = order_data(city_name='安顺市')
        api.app_addOrder(payload)
        # 线索ID
        loanId = api.get_loanId()

    @staticmethod
    def case2():
        for i in range(0,10):
            t1 = threading.Thread(target=create_order().case1, args=('11111111121',))
            t2 = threading.Thread(target=create_order().case1, args=('18397858213',))
            t1.start()
            t2.start()
            time.sleep(1)


if __name__ == "__main__":
    create_order().case2()
