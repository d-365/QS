# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 14:24
# @Author  : dujun
# @File    : locust_temp.py
# @describe:
from locust import TaskSet, task, HttpUser
from loguru import logger
from interface.testCaseManage.crm.crm_manage import crm_manage


class MyTaskSet(TaskSet):

    def on_start(self):
        logger.debug('locust执行开始')

    @task(2)
    def case1(self):
        run = crm_manage(loginName='dujun', env='')
        print(run.consumeList())
        logger.debug('哈哈')


class MyLocust(HttpUser):
    tasks = [MyTaskSet]
    host = 'https://school.51bm.net.cn'
    min_wait = 5000
    max_wait = 15000


if __name__ == "__main__":
    import os
    os.system("locust -f locust_temp.py")
