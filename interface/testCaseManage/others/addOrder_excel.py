# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: addOrder_excel.py
# @time: 2021/5/27 19:15
# @describe : excel读取对应用户贷款数据
import xlrd
from interface.project.admin.user import user_pro
from interface.tools.dataBase import DataBase
from interface.project.admin.userInformation import userInfo_pro
from interface.data.orderData_excel import excel_addOrder
from xlutils.copy import copy


class userInfo:
    """

    """

    def __init__(self,phone):
        self.database = DataBase()
        self.login_cookie = None
        self.phone = None
        self.phone = phone
        # 重置信贷多多后台用户登录验证码
        sql = "UPDATE admin.think_sms SET code =1234,`status`=0 WHERE phone=17637898368;"
        self.database.sql_execute(sql=sql)
        sql2 = "DELETE  from jgq.think_loan WHERE phone = %s;" % self.phone
        self.database.sql_execute(sql2)


    def manage_login(self):
        user = user_pro()
        data = {"phone": "17637898368", "code": "1234"}
        self.login_cookie = user.login(payload=data)

    def addOrder(self):
        userInfo = userInfo_pro()
        payload = excel_addOrder.order_data(phone=self.phone)
        excel_path = r'C:\Users\dujun\Downloads\excel_data.xls'
        excel = xlrd.open_workbook(excel_path)
        older_sheet = excel.sheet_by_index(0)
        cols = older_sheet.ncols
        print(cols)
        new_excel = copy(excel)
        new_sheet = new_excel.get_sheet(0)
        new_sheet.write(0, cols, '脚本价格')
        for i in range(0, len(payload)):
            re = userInfo.addOrder(data=payload[i], cookies=self.login_cookie)
            payloads = {
                'phone': self.phone, 'grabTime': None, 'page': 1, 'pageSize': 10
            }
            res = userInfo.orderList(datas=payloads, cookies=self.login_cookie)
            model_price = res['data']['data'][0]['model_price']
            new_sheet.write(i + 1, cols, model_price)
            sql2 = "DELETE  from jgq.think_loan WHERE phone = %s;" % self.phone
            self.database.sql_execute(sql2)
            print(re)
        new_excel.save(excel_path)


if __name__ == "__main__":
    run = userInfo('11111111103')
    run.manage_login()
    run.addOrder()
