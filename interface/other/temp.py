# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: temp.py
# @time: 2021/5/27 11:52
# @describe :

from interface.project.admin.user import user_pro
from interface.tools.dataBase import DataBase
from interface.project.admin.userInformation import userInfo_pro


class Test_run:

    @staticmethod
    def setup_class():
        database = DataBase()
        # 重置信贷多多后台用户登录验证码
        sql = "UPDATE admin.think_sms SET code =1234,`status`=0 WHERE phone=17637898368;"
        database.sql_execute(sql=sql)

    def test_run(self):
        user = user_pro()
        data = {"phone": "17637898368", "code": "1234"}
        login_cookie = user.login(payload=data)
        print(login_cookie)

        userInfo = userInfo_pro()
        payload = {"realname": "未实名用户", "age": 28, "sex": "2", "loan_money": "3", "loan_time": 36, "loan_goal": "消费贷款",
                   "loan_id_name": "上班族", "city_name": "杭州市", "social_security": "无本地社保", "provident_fund": "无本地公积金",
                   "is_house": "无房产", "is_car": "有车，不接受抵押", "credit_money": "20000元", "is_wld": "无", "is_zmf": "0",
                   "credit_record": "无信用卡或贷款", "lnsurance": "无", "education": "大专", "workunit": "轻山", "money": "6000元",
                   "income_type": "转账工资", "workage": "3个月以下", "car_money": "10万以下", "zmf": 0, "lnsurance_value": "",
                   "lnsurance_name": "", "loan_id": "0", "car_data": {"car_money": "10万以下"}, "house_data": {},
                   "loan": {"money": "6000元", "income_type": "转账工资"}, "wld_data": {}, "phone": "11111111115"}
        re = userInfo.addOrder(data=payload, cookies=login_cookie)
        print(re.json())
