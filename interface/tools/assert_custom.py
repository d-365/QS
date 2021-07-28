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
        if status:
            pass
        else:
            raise Exception("对应{}的值不在对应数据内".format(expect_key))


if __name__ == '__main__':
    pass
