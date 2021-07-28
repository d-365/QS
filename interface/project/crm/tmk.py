# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 16:48
# @Author  : dujun
# @File    : tmk_manage.py
# @describe: 电销开放平台
import logging

from faker import Faker
from loguru import logger

from interface.base.base_request import base_requests
from interface.base.caps import Caps
from interface.data.CRM_Account import account_tmk
from interface.data.order_data import crm_order_data


class tmk_pro:

    def __init__(self, loginName, environment=''):
        self.caps = Caps(env=environment)
        self.re = base_requests()

        # 电销开放平台登录
        url = self.caps['tmk'] + 'api/tmk/user/login'
        header_data = {'Content-Type': 'application/json'}
        payload = account_tmk(user=loginName)
        res = self.re.request(method='post', data_is_json=True, headers=header_data, url=url, data=payload)
        logger.debug(res)
        self.token = res['data']['token']
        self.headers = {
            "Content-Type": "application/json",
            'token': self.token
        }

    # 电销开放平台登录
    def login(self, datas):
        url = self.caps['crm'] + 'api/tmk/user/login'
        res = self.re.request(method='post', data_is_json=True, url=url, data=datas)
        logger.debug(res)
        return res

    # 电销开放平台-填单
    def apply(self, phone, cityName):
        url = self.caps['tmk'] + 'api/tmk/electricity/telemarketing/apply'
        payload = crm_order_data(phone=phone, cityName=cityName)
        res = self.re.request(method='post', data_is_json=True, url=url, headers=self.headers, data=payload)
        logger.debug('电销平台填单{}'.format(res))
        return res

    # 填单-查询手机号
    def apply_select(self, phone):
        url = self.caps['crm'] + 'api/crm/telemarketing/can/apply'
        res = self.re.request(method='get', headers=self.headers, url=url, data=phone)
        print(res)
        return res

    # 电销开放平台-符合条件广告列表
    def eligible_list(self, loanID):
        url = self.caps['crm'] + 'api/crm/electrical/eligible/list'
        payload = {
            'pageNum': '1',
            'pageSize': '10',
            'id': loanID
        }
        headers = {
            'token': self.token
        }
        res = self.re.request(method='get', url=url, headers=headers, data=payload)
        eligible_lists = res['data']['records']
        return eligible_lists

    # 电销详情_推送订单(定制需电核)
    def eligible_push(self, advertisingId, companyName, thinkLoanId):
        """
        :param advertisingId: 广告ID
        :param thinkLoanId: 订单ID
        :param companyName: 公司名称
        """
        url = self.caps['crm'] + 'api/crm/electrical/push'
        payload = {
            'advertisingId': advertisingId,
            'thinkLoanId': thinkLoanId,
            'companyName': companyName
        }
        res = self.re.request(method='post', data_is_json=True, url=url, headers=self.headers, data=payload)
        return res

    # 分代账号列表
    def branchList(self, branchAgencyName, accounts):
        """
        :param branchAgencyName:
        :param accounts: 账号
        :return:
        """
        url = self.caps['tmk'] + 'api/tmk/branch/branchList'
        payload = {
            'pageNum': 1,
            'pageSize': 10,
            'name': branchAgencyName,
            'account': accounts
        }
        headers = {
            'token': self.token
        }
        res = self.re.request(method='get', url=url, headers=headers, data=payload)
        branchList = res['data']['records']
        return branchList

    # 新增分代理商账户
    def addBranch(self, payload):
        url = self.caps['tmk'] + 'api/tmk/branch/addBranch'
        res = self.re.request(method='post', url=url, data_is_json=True, headers=self.headers, data=payload)
        return res

    # 删除分代理商账户
    def delBranch(self, userID):
        url = self.caps['tmk'] + 'api/tmk/branch/delBranch'
        payload = {
            'id': userID
        }
        res = self.re.request(method='post', data_is_json=True, url=url, headers=self.headers, data=payload)
        return res

    # 更新分代理商账户状态
    def updateStatus(self, userID, status):
        """
        :param userID:  账户id
        :param status:  状态  true启用  false禁用
        :return:
        """
        url = self.caps['tmk'] + 'api/tmk/branch/updateStatus'
        payload = {
            'id': userID,
            'status': status
        }
        res = self.re.request(method='post', data_is_json=True, url=url, headers=self.headers, data=payload)
        return res

    # 编辑员工账号（新增和修改）
    def saveUser_staff(self, payload):
        url = self.caps['tmk'] + 'api/tmk/user/saveUser'
        res = self.re.request(method='post', url=url, data_is_json=True, headers=self.headers, data=payload)
        logger.debug(res)
        return res

    # 更新员工账号状态
    def updateStatus_staff(self, userID, status):
        """
        :param userID:  账户id
        :param status:  状态  true启用  false禁用
        :return:
        """
        url = self.caps['tmk'] + 'api/tmk/user/updateStatus'
        payload = {
            'id': userID,
            'status': status
        }
        res = self.re.request(method='get', data_is_json=True, url=url, headers=self.headers, data=payload)
        logger.debug(res)
        return res

    # 获取员工列表
    def userList_staff(self, name='', accounts='', status=''):
        """
        :param status: 状态
        :param name: 姓名
        :param accounts: 账号
        :return:
        """
        url = self.caps['tmk'] + 'api/tmk/user/userList'
        payload = {
            'pageNum': 1,
            'pageSize': 10,
            'name': name,
            'account': accounts,
            'status': status
        }
        headers = {
            'token': self.token
        }
        res = self.re.request(method='get', url=url, headers=headers, data=payload)
        branchList = res['data']['records']
        logger.debug(branchList)
        return branchList

    # 删除员工账户
    def delUser_staff(self, userID):
        url = self.caps['tmk'] + 'api/tmk/user/delUser'
        payload = {
            'id': userID
        }
        res = self.re.request(method='post', data_is_json=True, url=url, headers=self.headers, data=payload)
        logger.debug(res)
        return res

    # 新增编辑分组
    def saveGroup(self, name, Id=''):
        """
        :param name: 分组名称
        :param Id: 分组id  编辑时传
        :return:
        """
        url = self.caps['tmk'] + 'api/tmk/group/saveGroup'
        if Id == '':
            payload = {
                'name': str(name),
            }
        else:
            payload = {
                'name': str(name),
                'id': Id
            }
        res = self.re.request(method='post', url=url, data_is_json=True, headers=self.headers, data=payload)
        logger.debug(res)
        return res

    # 获取分组列表
    def groupList(self, name):
        url = self.caps['tmk'] + 'api/tmk/group/groupList'
        payload = {
            'pageNum': 1,
            'pageSize': 10,
            'name': name
        }
        headers = {
            'token': self.token
        }
        res = self.re.request(method='get', url=url, headers=headers, data=payload)
        groupList = res['data']['records']
        return groupList

    # 获取已分组账户列表
    def getAllocatedList(self, ID):
        """
        :param ID: 分组ID
        :return:
        """
        url = self.caps['tmk'] + 'api/tmk/group/getAllocatedList?id={}'.format(ID)
        headers = {
            'token': self.token
        }
        res = self.re.request(method='get', url=url, headers=headers)
        logger.debug(res)
        getAllocatedList = res['data']
        return getAllocatedList

    # 获取未分组账户列表
    def getUnallocatedList(self):
        url = self.caps['tmk'] + 'api/tmk/group/getUnallocatedList'
        headers = {
            'token': self.token
        }
        res = self.re.request(method='get', url=url, headers=headers)
        UnallocatedList = res['data']
        return UnallocatedList

    # 添加分组成员
    def addGroupUser(self, groupId, userIds):
        """
        :param groupId:
        :param userIds: list [userID,]
        :return:
        """
        url = self.caps['tmk'] + 'api/tmk/group/addGroupUser'
        payload = {
            'groupId': groupId,
            'userIds': userIds
        }
        res = self.re.request(method='post', data_is_json=True, url=url, headers=self.headers, data=payload)
        logger.debug(res)
        return res

    # 删除分组成员
    def delGroupUser(self, userId):
        url = self.caps['tmk'] + 'api/tmk/group/delGroupUser'
        payload = {
            'userId': userId
        }
        res = self.re.request(method='post', data_is_json=True, url=url, headers=self.headers, data=payload)
        logger.debug(res)
        return res

    # 更换分组
    def changeGroup(self, groupId, userId):
        url = self.caps['tmk'] + 'api/tmk/group/changeGroup'
        payload = {
            'groupId': groupId,
            'userId': userId
        }
        res = self.re.request(method='post', data_is_json=True, url=url, headers=self.headers, data=payload)
        logging.debug(res)
        return res

    # 获取其他分组列表
    def getOtherGroupList(self, groupId):
        url = self.caps['tmk'] + 'api/tmk/group/getOtherGroupList'
        headers = {
            'token': self.token
        }
        res = self.re.request(method='get', url=url, headers=headers, data=groupId)
        logger.debug(res)
        return res

    # 删除分组
    def delGroup(self, groupId):
        url = self.caps['tmk'] + 'api/tmk/group/delGroup'
        payload = {
            'id': groupId
        }
        res = self.re.request(method='post', url=url, data_is_json=True, headers=self.headers, data=payload)
        logger.debug(res)
        return res


if __name__ == '__main__':
    run = tmk_pro(loginName='fen_interface')
    faker = Faker(locale='zh_CN')
    name = faker.word()
    account = faker.phone_number()
    password = 'test1234'
    payload = {"name": name, "phone": "11111111119", "account": account, "password": password, "status": True}
    run.saveUser_staff(payload=payload)
