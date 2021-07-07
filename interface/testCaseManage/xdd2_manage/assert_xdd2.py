# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 14:29
# @Author  : dujun
# @File    : assert_xdd2.py
# @describe: 好单多多App断言方法封装

import time
from interface.testCaseManage.xdd2_manage.xdd2_manage import xdd2_manage


class xdd2_assert:

    def __init__(self):
        self.xdd2 = xdd2_manage('13003672511')

    # 好单客源校验
    def app_source(self, loanId):
        time.sleep(1.5)
        orderList = self.xdd2.orderList(520400)  # 安顺市
        i = 0
        status = False
        while i < len(orderList['data']['data']):
            if loanId == orderList['data']['data'][i]['id']:
                status = True
                break
            else:
                i += 1
        if status is True:
            pass
        else:
            raise Exception("订单不在好单客源中")
        return status


if __name__ == "__main__":
    run = xdd2_assert()
    print(run.app_source(345))
