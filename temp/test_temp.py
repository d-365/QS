# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 17:29
# @Author  : dujun
# @File    : test_temp.py
# @describe:
from interface.data.order_data import order_data

order_datas = order_data(city_name='安顺市')
json2 = {
    'id': 6,
    'localLoanId': 6,
    'uid': '8311',
    'cname': 'd女士',
    'sex': '1',
    'phone': '13003672558',
    'loanTime': 1,
    'loanMoney': 8.0,
    'loanId': '0',
    'loanIdName': '上班族',
    'loan': '{"money":"2000元以下","income_type":"现金发放"}',
    'lnsurance': '投保人寿险且投保两年以下',
    'lnsuranceName': '阳光保险',
    'lnsuranceValue': '5万元以下',
    'education': '初中',
    'cityName': '北京市',
    'creditMoney': '3000元以下',
    'isCar': '有车，不接受抵押',
    'carData': '{"car_money":"10万以下"}',
    'isHouse': '有房产，不接受抵押',
    'houseData': '{"house_money":"50万及以下","house_type":"按揭房"}',
    'creatTime': '2021-07-02 18:04:13',
    'realname': 'du',
    'idcard': '',
    'providentFund': '连续6个月',
    'socialSecurity': '连续6个月',
    'channel': 'autoTest',
    'isWld': '有',
    'wldData': '{"wld_money":"500"}',
    'isZmf': '1',
    'workage': '6个月以上',
    'zmf': 500,
    'distributionStatus': 5,
    'creditRecord': '1年内逾期超过3次或者90天',
    'loanGoal': '结婚贷款',
    'workunit': '测试',
    'distributionTime': '2021-07-08 11:43:33',
    'source': '无电核订单系统分配',
    'advertisingName': '无电核',
    'systemName': None,
    'followTime': 0,
    'oneself': False,
    'electricalEnergyStatus': False,
    'ages': 22
}

if __name__ == "__main__":
    print(type(json2))
    print(type(order_datas))