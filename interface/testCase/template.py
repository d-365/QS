# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 15:52
# @Author  : dujun
# @File    : template.py
# @describe:
import allure
import pytest


@allure.feature("")
class Test_demo:

    @pytest.fixture(scope='session')
    def setup(self):
        pass

    @allure.story("")
    def test_case1(self):
        with allure.step(''):
            pass
        with allure.step(''):
            pass
        with allure.step(''):
            pass
        with allure.step(''):
            pass

    @allure.story("")
    def test_case2(self):
        with allure.step(''):
            pass
        with allure.step(''):
            pass
        with allure.step(''):
            pass
        with allure.step(''):
            pass
