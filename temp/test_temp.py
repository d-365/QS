# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 17:29
# @Author  : dujun
# @File    : test_temp.py
# @describe:
import allure
import pytest


class Test_temp:

    @allure.story('temp')
    def test_temp(self):
        print('temp')


if __name__ == "__main__":
    pytest.main(["test_temp.py", "--alluredir=./result"])
