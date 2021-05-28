# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: userInfo_manage.py
# @time: 2021/5/27 19:15
# @describe :

from interface.project.admin.user import user_pro
from interface.tools.dataBase import DataBase
from interface.project.admin.userInformation import userInfo_pro
from interface.data.order_data import addOrder_data


class userInfo:

    def __init__(self):
        self.login_cookie = None

    @staticmethod
    def test_sql():
        database = DataBase()
        # 重置信贷多多后台用户登录验证码
        sql = "UPDATE admin.think_sms SET code =1234,`status`=0 WHERE phone=17637898368;"
        database.sql_execute(sql=sql)

    def test_login(self):
        user = user_pro()
        data = {"phone": "17637898368", "code": "1234"}
        self.login_cookie = user.login(payload=data)
        print(self.login_cookie)

    def addOrder(self):
        userInfo = userInfo_pro()
        payload = addOrder_data(phone='11111111119', city_name='杭州市')
        re = userInfo.addOrder(data=payload, cookies=self.login_cookie)
        print(re.json())


if __name__ == "__main__":
    run = userInfo()
    run.test_sql()
    run.test_login()
    run.addOrder()
