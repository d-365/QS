# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: common_data.py
# @time: 2021/5/27 10:53
# @describe :

# 需传入cookie的header
def header_cookie(cookie=''):
    header_data = {
        'Content-Type': 'application/json',
        'Cookie': cookie
    }
    return header_data


