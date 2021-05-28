# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: order_data.py
# @time: 2021/5/28 16:59
# @describe :

# 好单多多新增订单需传入订单数据
def addOrder_data(phone, city_name):
    """

    :param phone: 传入手机号
    :param city_name: 借款城市
    :return:
    """
    # 性别
    sex = {
        '1': 1,  # 女
        '2': 2  # 男
    }
    # 资金用途
    loan_goal = {
        0: "消费贷款",
        1: "结婚贷款",
        2: "购房贷款",
        3: "装修贷款",
        4: "购车贷款",
        5: "旅游贷款",
        6: "医疗贷款",
        7: "其他贷款"
    }
    # 职业身份
    loan_id_name = {
        '上班族': '上班族',
        '自由职业': '自由职业',
        '个体户': '个体户'
    }

    # 本地社保
    social_security = {
        '无本地社保': '无本地社保',
        '3个月以下': '3个月以下',
        '连续3个月': '连续3个月',
        '连续6个月': '连续6个月'
    }
    # 本地公积金
    provident_fund = {
        '无本地公积金': '无本地公积金',
        '3个月以下': '3个月以下',
        '连续3个月': '连续3个月',
        '连续6个月': '连续6个月'
    }
    # 名下房产
    is_house = {
        '无房产': '无房产',
        '有房产，不接受抵押': '有房产，不接受抵押',
        '有房产，接受抵押': '有房产，接受抵押'
    }

    # 名下车产
    is_car = {
        '无车产': '无车产',
        '无车，准备购买': '无车，准备购买',
        '有车，不接受抵押': '有车，不接受抵押',
        '有车，可接受抵押': '有车，可接受抵押',
    }
    # 信用卡额度
    credit_money = {
        '无信用卡': '无信用卡',
        '3000元以下': '3000元以下',
        '3000元': '3000元',
        '5000元': '5000元',
        '10000元': '10000元',
        '20000元': '20000元',
        '30000元': '30000元',
        '30000元以上': '30000元以上'
    }

    # 微粒贷
    is_wld = {
        0: '无',
        1: '有',
    }

    # 芝麻分
    is_zmf = {
        0: "0",  # 无
        1: "1",  # 有
    }
    # 信用记录
    credit_record = {
        '无信用卡或贷款': '无信用卡或贷款'
    }

    # 最高学历
    education = {
        '初中': '初中',
        '高中': '高中',
        '中专': '中专',
        '大专': '大专',
        '本科及以上': '本科及以上'

    }

    # 月收入
    money = {
        '2000元以下': '2000元以下',
        '2000元': '2000元',
        '4000元': '4000元',
        '6000元': '6000元',
        '8000元': '8000元',
        '10000元': '10000元',
        '10000元以上': '10000元以上'
    }

    # 收入形势
    income_type = {
        0: '现金发放',
        1: '转账工资',
        2: '银行代发'
    }

    payload = {
        "realname": "接口生成", "age": 99, "sex": sex['1'],
        "loan_money": "3", "loan_time": 36, "loan_goal": loan_goal[0],
        "loan_id_name": loan_id_name['上班族'], "city_name": city_name,
        "provident_fund": provident_fund["无本地公积金"], "social_security": social_security["无本地社保"],
        "credit_money": credit_money['3000元'], "credit_record": credit_record['无信用卡或贷款'],
        "is_wld": is_wld[0], "wld_data": {}, "is_zmf": is_zmf[0], "zmf": "0",
        "lnsurance": "无", "lnsurance_name": "", "lnsurance_value": "",
        "workunit": "轻山", "workage": "3个月以下",
        "money": money["6000元"], "income_type": income_type[0],
        "loan": {"money": money["6000元"], "income_type": income_type[0]},
        "phone": phone, "education": education["大专"],
        "is_car": is_car['无车产'], "car_money": "10万以下", "car_data": {"car_money": "10万以下"},
        "is_house": is_house['有房产，接受抵押'], "house_data": {},
        "loan_id": "0"
    }

    return payload
