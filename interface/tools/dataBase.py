# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: dataBase.py
# @time: 2021/5/27 15:38
# @describe :
from sqlite3 import OperationalError

import pymysql


class DataBase:

    def __init__(self, host='', port='', user='', password=''):
        if host == '' and port == '' and user == '' and password == '':
            # 测试环境
            host = '118.31.184.240'
            port = 3306
            user = 'root'
            password = '3wHNY2Bq'
            self.conn = pymysql.connect(host=host, port=port, user=user, password=password)
        else:
            self.conn = pymysql.connect(host=host, port=port, user=user, password=password)
        self.cursor = self.conn.cursor()

    # 执行sql
    def sql_execute(self, sql=''):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            sql_value = self.cursor.fetchmany()
            return sql_value
        except OperationalError:
            self.conn.rollback()


if __name__ == '__main__':
    run = DataBase()
    run.sql_execute(sql="SELECT * from jgq.think_sms WHERE phone = 17637898368;")
