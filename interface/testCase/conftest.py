# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 16:10
# @Author  : dujun
# @File    : conftest.py
# @describe: conftest配置文件

import pytest


# 设置添加命令行参数
def pytest_addoption(parser):
    parser.addoption(
        # default: 默认值
        # help : 描述
        "--env", action="store", default="", help="my option: '' or online"
    )


# 返回命令行参数
@pytest.fixture(scope='session')
def cmdOption(request):
    return request.config.getoption("--env")
