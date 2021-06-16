# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: App_addOrder.py
# @time: 2021/5/31 14:40
# @describe : 信业帮App新增订单

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
        sql = "UPDATE jgq.think_sms SET STATUS=0 WHERE phone = %s;" % phone
        self.database.sql_execute(sql=sql)
        sql2 = "DELETE  from jgq.think_loan WHERE phone = %s;" % phone
        sql3 = "UPDATE jgq.think_loan SET creat_time = '2021-05-12 14:25:28',update_time = '2021-05-12 14:25:28',create_time_auto = '2021-05-12 14:25:28',update_time_auto = '2021-05-12 14:25:28',idcard = 411324199907100550 WHERE phone = %s ; " % phone
        self.database.sql_execute(sql3)

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
        return self.token

    # 信业帮新增订单
    def app_addOrder(self, datas):
        header = {
            'phone': self.phone,
            'auth': '98ef33',
            'token': self.token,
            'Content-Type': 'application/json'
        }
        re = self.jdf.firstLoan(headers=header, datas=datas)
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


class price_module:

    def __init__(self, phone):
        self.order = addOrder()
        self.order.test_sql(phone)
        self.phone = phone

    # 信业帮查询当前线索信息
    def get_loanId(self):
        token = self.order.app_login(phone=self.phone)
        data = {
            'phone': self.phone,
            'auth': '98ef33',
            'token': token,
            'system': 'android'

        }
        res = self.order.api.current_loanList(headers=data)
        loanID = res['data']['loan']['id']
        print(loanID)


if __name__ == "__main__":
    run = addOrder()
    run.test_sql('11111111120')
    run.app_login('11111111120')
    payload = addOrder_data(city_name='杭州市')
    run.app_addOrder(payload)
    run.loanReject()
