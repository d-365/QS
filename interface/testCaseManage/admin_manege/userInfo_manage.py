# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: addOrder_excel.py
# @time: 2021/5/27 19:15
# @describe :

from interface.data.order_data import addOrder_data
from interface.project.admin.user import user_pro
from interface.project.admin.userInformation import userInfo_pro
from interface.tools.dataBase import DataBase


class userInfo:

    def __init__(self):
        self.login_cookie = None

    @staticmethod
    def test_sql(phone):
        database = DataBase()
        # 重置信贷多多后台用户登录验证码
        sql = "UPDATE admin.think_sms SET code =1234,`status`=0 WHERE phone=17637898368;"
        database.sql_execute(sql=sql)
        sql2 = "DELETE  from jgq.think_loan WHERE phone = %s;" % phone
        database.sql_execute(sql2)

    def manage_login(self):
        user = user_pro()
        data = {"phone": "17637898368", "code": "1234"}
        self.login_cookie = user.login(payload=data)
        return self.login_cookie

    def addOrder(self, phone, city_name):
        self.userInfo = userInfo_pro()
        payload = addOrder_data(phone=phone, city_name=city_name)
        re = self.userInfo.addOrder(data=payload, cookies=self.login_cookie)
        print(re)

    # 订单列表
    def orderList(self, phone):
        payload = {
            'phone': phone, 'grabTime': None, 'page': 1, 'pageSize': 10
        }
        re = self.userInfo.orderList(datas=payload, cookies=self.login_cookie)
        # model_price
        model_price = re['data']['data'][0]['model_price']
        print(model_price)
        return model_price


if __name__ == "__main__":
    for i in range(0, 2):
        run = userInfo()
        run.test_sql('11111111103')
        run.manage_login()
        run.addOrder('11111111103', city_name='杭州市')
