# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 16:28
# @Author  : dujun
# @File    : test_CRM_Condition.py
# @describe: CRM广告匹配
import time


class Test_CRM:

    def test_case2(self, order):
        payload = {
            "city_name": "杭州市",
            "loan_money": "50",
            "loan_time": 6,
            "loan_goal": "消费贷款",
            "loan_id_name": "上班族",
            "education": "本科及以上",
            "workunit": "测试",
            "money": "2000元",
            "income_type": "转账工资",
            "workage": "3个月-6个月",
            "license": "",
            "year": "",
            "warter_money": "",
            "social_security": "3个月以下",
            "provident_fund": "3个月以下",
            "is_house": "有房产，接受抵押",
            "house_type": "按揭房",
            "house_money": "50万-100万",
            "is_car": "有车，不接受抵押",
            "car_money": "10万以下",
            "credit_money": "3000元以下",
            "is_wld": "有",
            "wld_money": 500,
            "is_zmf": "有",
            "zmf": "555",
            "credit_record": "无信用卡或贷款",
            "lnsurance": "投保人寿险且投保两年以上",
            "lnsurance_name": "安邦保险",
            "lnsurance_value": "10万元以上",
            "loan_id": 0,
            "car_data": {
                "car_money": "10万以下"
            },
            "house_data": {
                "house_money": "50万-100万",
                "house_type": "按揭房"
            },
            "loan": {
                "money": "2000元",
                "income_type": "转账工资"
            },
            "wld_data": {
                "wld_money": 500
            }
        }
        for i in range(0,1):
            order.app_addOrder(datas=payload)
            loanId = order.get_loanId()
            print(loanId)
