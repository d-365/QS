# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 17:54
# @Author  : dujun
# @File    : push.py
# @describe: 推单并发

import threading
import time
from interface.testCaseManage.crm.crm_manage import crm_manage


class push:

    def __init__(self):
        self.crm_manage = crm_manage(env='', loginName='manage_interface')

    def case1(self,advertisingId,thinkLoanId):
        self.crm_manage.push(advertisingId=advertisingId, thinkLoanId=thinkLoanId, companyName='dujun_gs_001')

    def case3(self):
        t1 = threading.Thread(target=self.case1,kwargs={'advertisingId':'79','thinkLoanId':'10784'})
        t2 = threading.Thread(target=self.case1,kwargs={'advertisingId':'79','thinkLoanId':'10933'})
        t1.start()
        t2.start()


if __name__ == "__main__":
    run = push()
    run.case3()
