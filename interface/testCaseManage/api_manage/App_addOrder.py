# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: App_addOrder.py
# @time: 2021/5/31 14:40
# @describe :
import json

from interface.data.order_data import addOrder_data
from interface.project.api.api import api_pro
from interface.project.jdf.jdf import jdf_pro
from interface.tools.dataBase import DataBase


class addOrder:

    def __init__(self):
        self.database = DataBase()
        self.api = api_pro()
        self.jdf = jdf_pro()
        self.token = ''
        self.phone = ''

    def test_sql(self, phone):
        # 重置信贷多多后台用户登录验证码
        sql = "UPDATE jgq.think_sms SET STATUS=0 WHERE phone = %d;" % phone
        self.database.sql_execute(sql=sql)
        # sql2 = "DELETE  from jgq.think_loan WHERE phone = %d;" % phone
        # self.database.sql_execute(sql2)

    # app登录
    def app_login(self, phone):
        """
        :param phone: 登录手机号
        :return:
        """
        self.phone = phone
        payload = {
            'phone': self.phone,
            'code': 1234,
            'device_token': 'AhGJMV5mG - XzV1hO8F_9PW - RlCTsvj6_kcr__rACf5ih',
            'isCover': 0
        }
        re = self.api.user_login(data=payload)
        self.token = re['data']['token']

    # 信业帮新增订单
    def app_addOrder(self):
        headers = {
            'phone': self.phone,
            'auth': '98ef33',
            'token': self.token,
            'Content-Type': 'application/json'
        }
        payload = addOrder_data(city_name='杭州市')
        re = self.jdf.firstLoan(headers=headers, datas=payload)
        print(re)

    # 信业帮新增订单_校验
    def loanReject(self):
        headers = {
            'phone': self.phone,
            'auth': '98ef33',
            'token': self.token,
            'Content-Type': 'application/json'
        }
        payload = {
            "source": 0
        }
        re = self.jdf.loanReject(headers=headers, datas=payload)
        print(re)


if __name__ == "__main__":
    run = addOrder()
    run.test_sql(11111111101)
    run.app_login('11111111101')
    run.app_addOrder()
    run.loanReject()