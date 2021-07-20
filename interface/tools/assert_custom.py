# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 15:38
# @Author  : dujun
# @File    : assert_custom.py
# @describe: 常用断言方法封装

class custom_assert:

    @staticmethod
    def dict_json_include(expect_key, expect_value, dict_data):
        """
        断言列表内的json内是否存在某字符
        """
        i = 0
        status = False
        if isinstance(expect_key, str):
            while i < len(dict_data):
                if expect_key in dict_data[i]:
                    if expect_value == dict_data[i][expect_key]:
                        status = True
                        break
                    else:
                        i += 1
                else:
                    raise Exception("对应的数据内没有对应得的值{}".format(expect_key))

        # elif isinstance(expect_key, dict):
        #
        #     while i < len(dict_data):
        #         for j in range(len(expect_key)):
        #             if expect_key[j] in dict_data[i]:
        #                 if expect_value[j] == dict_data[i][expect_key]:
        #                     status = True
        #                     break
        #                 else:
        #                     i += 1
        #             else:
        #                 raise Exception("对应的数据内没有对应得的值{}".format(expect_key))
        if status:
            pass
        else:
            raise Exception("对应{}的值不在对应数据内".format(expect_key))


if __name__ == '__main__':
    datas = [
        {'tags': '14', 'callOrderServiceMoney': None, 'demandMethod': 0, 'uid': None, 'money': None, 'actMoney': None,
         'speedMoney': None, 'grabTime': None, 'id': 3382, 'realname': '杜军', 'phone': '18397858213', 'cityName': '安顺市',
         'channel': 'a', 'modelCode': 'DDDACDBCCCCADAZ', 'modelPrice': 39, 'calculationPrice': 0, 'status': '4',
         'creatTime': '2021-07-19 14:03:44', 'type': None, 'isSpecial': None, 'xuserPhone': '', 'xuserId': 0,
         'xusername': None}]
    if 'id' in datas[0]:
        print('hh')
