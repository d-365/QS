# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 16:28
# @Author  : dujun
# @File    : test_CRM_Condition.py
# @describe: CRM广告匹配


class Test_CRM:

    def test_case1(self, order):
        payload = {"loan_money": "6", "loan_time": 1, "loan_goal": "消费贷款", "loan_id_name": "上班族", "education": "大专",
                   "workunit": "轻山", "money": "10000元以上", "income_type": "转账工资", "workage": "3个月以下", "license": "",
                   "year": "", "warter_money": "", "social_security": "连续6个月", "provident_fund": "连续6个月",
                   "is_house": "有房产，接受抵押", "house_type": "其他", "house_money": "50万及以下", "is_car": "有车，不接受抵押",
                   "car_money": "10万以下", "credit_money": "3000元以下", "is_wld": "有", "wld_money": 900, "is_zmf": "有",
                   "zmf": "620", "credit_record": "1年内逾期超过3次或者90天", "lnsurance": "无", "lnsurance_name": "",
                   "lnsurance_value": "", "city_name": "杭州市", "loan_id": 0, "car_data": {"car_money": "10万以下"},
                   "house_data": {"house_money": "50万及以下", "house_type": "其他"},
                   "loan": {"money": "10000元以上", "income_type": "转账工资"}, "wld_data": {"wld_money": 500}}
        order.app_addOrder(datas=payload)
        order.loanReject()

    def test_case2(self, order):
        payload = {"loan_money": "3", "loan_time": 1, "loan_goal": "消费贷款", "loan_id_name": "上班族", "education": "大专",
                   "workunit": "轻山", "money": "10000元以上", "income_type": "转账工资", "workage": "3个月以下", "license": "",
                   "year": "", "warter_money": "", "social_security": "连续6个月", "provident_fund": "连续6个月",
                   "is_house": "有房产，接受抵押", "house_type": "其他", "house_money": "50万及以下", "is_car": "有车，不接受抵押",
                   "car_money": "10万以下", "credit_money": "3000元以下", "is_wld": "有", "wld_money": 500, "is_zmf": "有",
                   "zmf": "500", "credit_record": "1年内逾期超过3次或者90天", "lnsurance": "无", "lnsurance_name": "",
                   "lnsurance_value": "", "city_name": "杭州市", "loan_id": 0, "car_data": {"car_money": "10万以下"},
                   "house_data": {"house_money": "50万及以下", "house_type": "其他"},
                   "loan": {"money": "10000元以上", "income_type": "转账工资"}, "wld_data": {"wld_money": 500}}
        order.app_addOrder(datas=payload)
        order.loanReject()
