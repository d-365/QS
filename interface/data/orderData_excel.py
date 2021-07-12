# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 17:06
# @Author  : dunjun
# @File    : orderData_excel.py
# @describe: 获取excel数据,生成订单
import xlrd


class excel_addOrder:

    @staticmethod
    def order_data(excel_source_path,phone):
        """
        :param excel_source_path: 源文件位置
        :param phone:
        :return: type(list)
        """
        # 性别
        sex_value = ''
        # 借款金额
        loan_money_value = ''
        # 借款周期
        loan_id_name_value = ''
        # 城市
        city_name_value = ''
        # 公积金缴纳月数
        provident_fund_value = ''
        # 社保缴纳月数
        social_security_value = ''
        # 信用卡额度
        credit_money_value = ''
        # 发薪方式
        loan_value = ''
        # 微粒贷金额
        wld_data_value = ''
        # 是否微粒贷
        is_wld_value = ''
        education_value = ''
        is_car_value = ''
        car_data_value = ''
        is_house_value = ''
        house_data_value = ''
        age_value = ''

        excel_path = excel_source_path
        excel = xlrd.open_workbook(excel_path)
        sheet = excel.sheet_by_index(0)
        rows = sheet.nrows
        cols = sheet.ncols
        excel_listData = []

        for j in range(0, rows - 1):
            for i in range(0, cols - 1):
                # 性别
                if sheet.cell_value(j, i) == 'sex':
                    sex_value = sheet.cell_value(j + 1, i)
                # 借款金额
                elif sheet.cell_value(j, i) == 'loan_money':
                    loan_money_value = sheet.cell_value(j + 1, i)
                # 职业身份
                elif sheet.cell_value(j, i) == 'loan_id_name':
                    loan_id_name_value = sheet.cell_value(j + 1, i)
                # loan
                elif sheet.cell_value(j, i) == 'loan':
                    loan_value = sheet.cell_value(j + 1, i)
                # 城市
                elif sheet.cell_value(j, i) == 'city_name':
                    city_name_value = sheet.cell_value(j + 1, i)
                # 信用卡额度
                elif sheet.cell_value(j, i) == 'credit_money':
                    credit_money_value = sheet.cell_value(j + 1, i)
                # is_car
                elif sheet.cell_value(j, i) == 'is_car':
                    is_car_value = sheet.cell_value(j + 1, i)
                # car_data
                elif sheet.cell_value(j, i) == 'car_data':
                    car_data_value = sheet.cell_value(j + 1, i)
                # is_house
                elif sheet.cell_value(j, i) == 'is_house':
                    is_house_value = sheet.cell_value(j + 1, i)
                # house_data
                elif sheet.cell_value(j, i) == 'house_data':
                    house_data_value = sheet.cell_value(j + 1, i)
                # age
                elif sheet.cell_value(j, i) == '年龄':
                    age_value = sheet.cell_value(j + 1, i)
                # 公积金缴纳月数
                elif sheet.cell_value(j, i) == 'provident_fund':
                    provident_fund_value = sheet.cell_value(j + 1, i)
                # 社保缴纳月数
                elif sheet.cell_value(j, i) == 'social_security':
                    social_security_value = sheet.cell_value(j + 1, i)
                # is_wld
                elif sheet.cell_value(j, i) == 'is_wld':
                    is_wld_value = sheet.cell_value(j + 1, i)
                # wld_data
                elif sheet.cell_value(j, i) == 'wld_data':
                    wld_data_value = sheet.cell_value(j + 1, i)
                # wld_data
                elif sheet.cell_value(j, i) == 'education':
                    education_value = sheet.cell_value(j + 1, i)

            payload = {
                "realname": "接口生成", "age": age_value, "sex": sex_value,
                "loan_money": loan_money_value, "loan_time": 12, "loan_goal": '消费贷款',
                "loan_id_name": loan_id_name_value, "city_name": city_name_value,
                "provident_fund": provident_fund_value, "social_security": social_security_value,
                "credit_money": credit_money_value, "credit_record": '无信用卡或贷款',
                "is_wld": is_wld_value, "wld_data": wld_data_value, "is_zmf": '无', "zmf": "0",
                "lnsurance": "无", "lnsurance_name": "", "lnsurance_value": "",
                "workunit": "轻山", "workage": "3个月以下",
                "loan": loan_value,
                "education": education_value,
                "is_car": is_car_value,
                "car_data": car_data_value,
                "is_house": is_house_value,
                "house_data": house_data_value,
                "loan_id": "0", "phone": phone
            }
            excel_listData.append(payload)

        return excel_listData


if __name__ == "__main__":
    excel_path = r'C:\Users\dujun\Downloads\excel_data.xls'
    data = excel_addOrder().order_data(excel_source_path=excel_path,phone='1111111103')
    print(data)
