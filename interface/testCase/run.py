# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 17:16
# @Author  : dujun
# @File    : run.py
# @describe: 用例执行文件
import os
import time

from loguru import logger

from interface.tools.sendMail import send_mail


class Test_run:

    def setup_class(self):
        self.today_data = time.strftime("%m%d%H%M", time.localtime())
        self.file_path = "./report/{}.html".format(self.today_data)
        logger.debug("-" * 20 + "用例执行开始" + "-" * 20)

    def teardown_class(self):
        send_mail(file_name=self.file_path)

    def test_run(self):
        os.system(r'pytest -s crm\test_tmk.py --html={}'.format(self.file_path))
