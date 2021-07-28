# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: addOrder_excel.py
# @time: 2021/5/27 19:15
# @describe : 好单多多后台

from interface.data.order_data import addOrder_data
from interface.project.admin_old.user import user_pro
from interface.project.admin_old.userInformation import userInfo_pro
from interface.tools.dataBase import DataBase


class userInfo:

    def __init__(self):
        self.userInfo = userInfo_pro()
        self.login_cookie = None
        database = DataBase()
        # 重置信贷多多后台用户登录验证码
        sql = "UPDATE admin_old.think_sms SET code =1234,`status`=0 WHERE phone=17637898368;"
        database.sql_execute(sql=sql)

        user = user_pro()
        data = {"phone": "17637898368", "code": "1234"}
        self.login_cookie = user.login(payload=data)

    def addOrder(self, phone, city_name):
        payload = addOrder_data(phone=phone, city_name=city_name)
        re = self.userInfo.addOrder(data=payload, cookies=self.login_cookie)
        print(re)

    # 订单列表
    def orderList(self, phone):
        payload = {
            'phone': phone, 'grabTime': None, 'page': 1, 'pageSize': 10
        }
        re = self.userInfo.orderList(datas=payload, cookies=self.login_cookie)
        print(re)
        # model_price
        model_price = re['data']['data'][0]['model_price']
        return model_price


if __name__ == "__main__":
    run = userInfo()
    run.orderList(phone='11111111121')
