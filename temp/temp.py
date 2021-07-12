# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 17:29
# @Author  : dujun
# @File    : test_temp.py
# @describe:

if __name__ == '__main__':
    data = {
        'id': '20120001',
        'name': 'Bob',
        'age': 20
    }
    table = 'students'
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    print(values)
