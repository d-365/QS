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

    def __init__(self, env='',phone=''):
        self.database = DataBase()
        self.api = api_pro(environment=env)
        self.jdf = jdf_pro(environment=env)
        self.token = ''
        # 重置信业帮App用户登录验证码
        sql = "UPDATE jgq.think_sms SET STATUS=0 WHERE phone = %s;" % phone
        self.database.sql_execute(sql=sql)
        sql2 = "DELETE  from jgq.think_loan WHERE phone = %s;" % phone
        sql3 = "UPDATE jgq.think_loan SET creat_time = '2021-05-12 14:25:28',update_time = '2021-05-12 14:25:28',create_time_auto = '2021-05-12 14:25:28',update_time_auto = '2021-05-12 14:25:28',idcard = 411324199907100550 WHERE phone = %s ; " % phone
        self.database.sql_execute(sql3)
        self.phone = phone

        payload = {
            'phone': phone,
            'code': 1234,
            'device_token': 'AhGJMV5mG - XzV1hO8F_9PW - RlCTsvj6_kcr__rACf5ih',
            'isCover': 0
        }

        re = self.api.user_login(data=payload)
        self.token = re['data']['token']

    # 信业帮新增订单
    def app_addOrder(self, datas):
        header = {
            'phone': self.phone,
            'auth': '98ef33',
            'token': self.token,
            'Content-Type': 'application/json'
        }
        re = self.jdf.firstLoan(headers=header, datas=datas)
        # 信业帮新增订单_校验
        payload2 = {
            "source": 0
        }
        res = self.jdf.loanReject(headers=header, datas=payload2)
        print(self.phone + '  发布线索', res)

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

    # 信业帮查询当前线索信息
    def get_loanId(self):
        data = {
            'phone': self.phone,
            'auth': '98ef33',
            'token': self.token,
            'system': 'android'

        }
        res = self.api.current_loanList(headers=data)
        loanID = res['data']['loan']['id']
        return loanID


if __name__ == "__main__":
    run = addOrder(phone='11111111119')
    payload = addOrder_data(city_name='杭州市')
    run.app_addOrder(payload)
    run.get_loanId()

