# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 17:44
# @Author  : dujun
# @File    : price_module.py
# @describe:


# 微粒贷金额
def wld_money_new(x):
    if 0 <= x <= 3000:
        return 'D', '>= 0 或 <= 3000'
    elif x > 20000:
        return 'A', '> 20000'
    else:
        return 'B', 'other'


# 认证社保
def type_2(x):
    if x == True:
        return 'A', '有'
    else:
        return 'D', '无'


# 认证公积金
def type_3(x):
    if x == True:
        return 'A', '有'
    else:
        return 'D', '无'


# 借款金额
def loan_money(x):
    if x < 2:
        return 'D', '<2'
    elif x >= 5 and x <= 60:
        return 'A', '>= 5 且 x <= 60'
    else:
        return 'C', 'other'


# 性别
def sex(x):
    if x == '1':
        return 'B', '女'
    else:
        return 'C', '男'


# 信用卡额度
def credit_money(x):
    if x in ['无信用卡', '3000元', '3000元以下', '5000元']:
        return 'D', '无信用卡, 3000元, 3000元以下, 5000元'
    elif x in ['20000元', '30000元', '30000元以上']:
        return 'B', '20000元, 30000元, 30000元以上'
    else:
        return 'C', 'other'


# 发薪方式
def p_income_type(x):
    if x == '银行代发':
        return 'A', '银行代发'
    elif x == '转账工资':
        return 'B', '转账工资'
    else:
        return 'C', 'other'


# 用户自己填的公积金缴纳月数
def provident_fund(x):
    if x == '连续6个月':
        return 'B', '连续6个月'
    else:
        return 'C', 'other'


# 年龄
def age(x):
    if x >= 24 and x < 40:
        return 'A', '>=24, <40'
    elif x < 60 and x >= 40:
        return 'B', '40-60'
    else:
        return 'C', 'other'


# 用户自己填的社保缴纳月数
def social_security(x):
    if x == '连续6个月':
        return 'B', '连续6个月'
    else:
        return 'C', 'other'


# 房产价值
def house_money(x):
    if x in ['1000万以上', '100万-200万', '200万-500万', '500万-1000万']:
        return 'A', '100W以上'
    elif x == '50万及以下':
        return 'D', '<=50'
    else:
        return 'C', 'other'


# 是否有微粒贷
def is_wld(x):
    if x == '有':
        return 'A', '有'
    else:
        return 'C', '无'


# 收入金额
def p_income(x):
    if x in ['2000元', '4000元', '2000元以下', '8000元', '6000元']:
        return 'D', '<=8000'
    else:
        return 'A', 'other'
