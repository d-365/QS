# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: addOrder_excel.py
# @time: 2021/5/27 19:15
# @describe : excel读取对应用户贷款数据

import xlrd
from xlutils.copy import copy
from interface.data.orderData_excel import excel_addOrder
from interface.project.admin_old.user import user_pro
from interface.project.admin_old.userInformation import userInfo_pro
from interface.tools.dataBase import DataBase


class userInfo:

    def __init__(self, phone):
        """
        :param phone: 1:清空对应phone数据库订单信息  2：使用phone新增订单
        """
        self.database = DataBase()
        self.login_cookie = None
        self.phone = None
        self.phone = phone
        # 重置信贷多多后台用户登录验证码
        sql = "UPDATE admin_old.think_sms SET code =1234,`status`=0 WHERE phone=17637898368;"
        self.database.sql_execute(sql=sql)
        sql2 = "DELETE  from jgq.think_loan WHERE phone = %s;" % self.phone
        self.database.sql_execute(sql2)

    def manage_login(self):
        user = user_pro(environment='')
        data = {"phone": "17637898368", "code": "1234"}
        self.login_cookie = user.login(payload=data)

    def addOrder(self,excel_path):
        user_Info = userInfo_pro()
        payload = excel_addOrder.order_data(excel_source_path=excel_path,phone=self.phone)
        excel = xlrd.open_workbook(excel_path)
        older_sheet = excel.sheet_by_index(0)
        cols = older_sheet.ncols
        print(cols)
        new_excel = copy(excel)
        new_sheet = new_excel.get_sheet(0)
        new_sheet.write(0, cols, '脚本价格')
        for i in range(0, len(payload)):
            re = user_Info.addOrder(data=payload[i], cookies=self.login_cookie)
            payloads = {
                'phone': self.phone, 'grabTime': None, 'page': 1, 'pageSize': 10
            }
            res = user_Info.orderList(datas=payloads, cookies=self.login_cookie)
            model_price = res['data']['data'][0]['model_price']
            new_sheet.write(i + 1, cols, model_price)
            sql3 = "UPDATE jgq.think_loan SET creat_time = '2021-05-12 14:25:28',update_time = '2021-05-12 14:25:28',create_time_auto = '2021-05-12 14:25:28',update_time_auto = '2021-05-12 14:25:28',idcard = 411324199907100550 WHERE phone = %s ; " % self.phone
            self.database.sql_execute(sql3)
            print(re)
        new_excel.save(excel_path)


if __name__ == "__main__":
    run = userInfo('11111111103')
    excelPath = r'C:\Users\dujun\Downloads\excel_data.xls'
    run.manage_login()
    run.addOrder(excel_path=excelPath)
