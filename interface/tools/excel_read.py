# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 17:31
# @Author  : dujun
# @File    : excel_read.py
# @describe:
import xlrd


def excel_assert(excel_path):
    excel = xlrd.open_workbook(excel_path)
    sheet = excel.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    i = 1
    while i < rows:
        excel_value1 = sheet.cell_value(i, 0)
        excel_value2 = sheet.cell_value(i, 1)
        i += 1
        try:
            assert excel_value1 == excel_value2
        except AssertionError:
            print('第%d行数据不一致' % i)


if __name__ == '__main__':
    excel_path = r"C:\Users\dujun\Downloads\temp.xls"
    excel_assert(excel_path)
