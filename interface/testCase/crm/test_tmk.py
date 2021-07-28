# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 17:29
# @Author  : dujun
# @File    : test_tmk.py
# @describe: 电销开放平台
import random
import allure
import pytest
from interface.tools.assert_custom import custom_assert


@allure.feature('电销开放平台账户管理')
class Test_account:

    @pytest.fixture(scope='session')
    def setup(self):
        pass

    @allure.story("创建分代理商账号")
    def test_case1(self, tmk, faker):
        with allure.step('输入合理的代理商，可正常保存'):
            branchAgencyName = faker.word()
            branchAgencyCode = faker.phone_number()
            name = faker.word()
            account = faker.phone_number()
            password = 'test1234'
            status = True
            payload = {"branchAgencyName": branchAgencyName, "branchAgencyCode": branchAgencyCode, "name": name,
                       "phone": '11111111119',
                       'account': account, "password": password, "status": status}
            tmk.addBranch(payload=payload)
            with allure.step("分代账号列表断言"):
                branchList = tmk.branchList(accounts=account, branchAgencyName=branchAgencyName)
                assert branchList[0]['branchAgencyName'] == branchAgencyName
                assert branchList[0]['branchAgencyCode'] == branchAgencyCode
                assert branchList[0]['name'] == name
                assert branchList[0]['account'] == account
                assert branchList[0]['status'] == status
            with allure.step("更新账户状态"):
                branchId = branchList[0]['id']
                tmk.updateStatus(userID=branchId, status=False)
                branchList_after = tmk.branchList(accounts=account, branchAgencyName=branchAgencyName)
                assert branchList_after[0]['status'] is False

        with allure.step('不同代理商输入重复代码，不可输入'):
            message2 = "该代码已存在"
            branchAgencyName2 = faker.word()
            account2 = faker.numerify()
            payload2 = {"branchAgencyName": branchAgencyName2, "branchAgencyCode": branchAgencyCode, "name": name,
                        "phone": '11111111119',
                        'account': account2, "password": password, "status": True}
            res = tmk.addBranch(payload=payload2)
            assert res['msg'] == message2

        with allure.step('输入重复的账号'):
            message4 = "该代理商名称已存在"
            branchAgencyCode4 = faker.phone_number()
            payload4 = {"branchAgencyName": branchAgencyName, "branchAgencyCode": branchAgencyCode4, "name": name,
                        "phone": '11111111119',
                        'account': account, "password": password, "status": True}
            res = tmk.addBranch(payload=payload4)
            assert res['msg'] == message4

        with allure.step('删除分代理商'):
            tmk.delBranch(userID=branchId)
            branchList_after = tmk.branchList(accounts=account, branchAgencyName=branchAgencyName)
            assert len(branchList_after) == 0

    @allure.story("创建员工账号")
    def test_case2(self, tmk_sub, faker):
        with allure.step('输入合理的账户,可正常保存'):
            name = faker.word()
            account = faker.phone_number()
            password = 'test1234'
            status = True
            payload = {"name": name, "phone": '11111111119', 'account': account, "password": password, "status": status}
            tmk_sub.saveUser_staff(payload=payload)
            with allure.step("员工列表断言"):
                userList_staff = tmk_sub.userList_staff(accounts=account, name=name)
                assert userList_staff[0]['name'] == name
                assert userList_staff[0]['account'] == account
                assert userList_staff[0]['status'] == status

            with allure.step("更新账户状态"):
                userID = userList_staff[0]['id']
                tmk_sub.updateStatus(userID=userID, status=False)
                userList_staff_after = tmk_sub.userList_staff(accounts=account, name=name)
                assert userList_staff_after[0]['status'] is False

        with allure.step('输入重复的账号'):
            message4 = "该账号已存在，请重新设置"
            payload4 = {"name": name, "phone": '11111111119', 'account': account, "password": password, "status": True}
            res = tmk_sub.saveUser_staff(payload=payload4)
            assert res['msg'] == message4

        with allure.step('删除员工账号'):
            tmk_sub.delUser_staff(userID=userID)
            userList_staff_afterAgain = tmk_sub.userList_staff(accounts=account, name=name)
            assert len(userList_staff_afterAgain) == 0

    @allure.story("新建分组")
    def test_case3(self, tmk_sub, faker):
        with allure.step('输入符合规则字符可正常创建分组'):
            groupName = faker.sentence()
            tmk_sub.saveGroup(name=groupName)
            groupList = tmk_sub.groupList(name=groupName)
            groupId = groupList[0]['id']
            assert groupList[0]['name'] == groupName
        with allure.step('创建名称相同的分组'):
            message = '该分组已存在'
            saveGroup = tmk_sub.saveGroup(name=groupName)
            assert saveGroup['msg'] == message
            groupList2 = tmk_sub.groupList(name=groupName)
            assert len(groupList2) == 1
        with allure.step('分配组员'):
            # 未分配员工列表
            getUnallocatedList = tmk_sub.getUnallocatedList()
            # 存在未分配员工账号
            if len(getUnallocatedList) > 0:
                # 未分配用户ID
                unAllot_userId = getUnallocatedList[0]['id']
                tmk_sub.addGroupUser(groupId=groupId, userIds=[unAllot_userId])
                getAllocatedList = tmk_sub.getAllocatedList(ID=groupId)
                custom_assert().dict_json_include(expect_key='id', expect_value=unAllot_userId,
                                                  dict_data=getAllocatedList)
            # 不存在未分配员工账号
            else:
                name = faker.word()
                account = faker.phone_number()
                password = 'test1234'
                status = True
                payload = {"name": name, "phone": '11111111119', 'account': account, "password": password,
                           "status": status}
                tmk_sub.saveUser_staff(payload=payload)
                userList_staff = tmk_sub.userList_staff(accounts=account, name=name)
                userID = userList_staff[0]['id']
                tmk_sub.addGroupUser(groupId=groupId, userIds=[userID])
                getAllocatedList = tmk_sub.getAllocatedList(ID=groupId)
                custom_assert().dict_json_include(expect_key='id', expect_value=userID, dict_data=getAllocatedList)

        with allure.step('删除组员'):
            getAllocatedList_3 = tmk_sub.getAllocatedList(ID=groupId)
            random_user = random.randint(0, len(getAllocatedList_3) - 1)
            userId3 = getAllocatedList_3[random_user]['id']
            tmk_sub.delGroupUser(userId=userId3)
            getAllocatedList_3_after = tmk_sub.getAllocatedList(ID=groupId)
            for i in range(0, len(getAllocatedList_3_after)):
                assert userId3 not in getAllocatedList_3_after[i].values()

        with allure.step('删除分组'):
            tmk_sub.delGroup(groupId=groupId)
            groupList4 = tmk_sub.groupList(name=groupName)

            for i in range(0, len(groupList4)):
                assert groupId and groupName not in groupList4[i].values()
        with allure.step('删除员工账号'):
            tmk_sub.delUser_staff(userID=userID)

    @allure.story("更换分组")
    def test_case4(self, tmk_sub, faker):
        with allure.step('新增分组A、B'):
            groupA = 'groupA'
            tmk_sub.saveGroup(name=groupA)

            groupListA = tmk_sub.groupList(name=groupA)
            groupIdA = groupListA[0]['id']
            # 分组B
            groupB = 'groupB'
            tmk_sub.saveGroup(name=groupB)
            groupListB = tmk_sub.groupList(name=groupB)
            groupIdB = groupListB[0]['id']
        with allure.step('查询待分配用户ID'):
            # 未分配员工列表
            getUnallocatedList = tmk_sub.getUnallocatedList()
            # 存在未分配员工账号
            if len(getUnallocatedList) > 0:
                # 未分配用户ID
                userId = getUnallocatedList[0]['id']
            # 不存在未分配员工账号
            else:
                name = faker.word()
                account = faker.phone_number()
                password = 'test1234'
                status = True
                payload = {"name": name, "phone": '11111111119', 'account': account, "password": password,
                           "status": status}
                tmk_sub.saveUser_staff(payload=payload)
                userList_staff = tmk_sub.userList_staff(accounts=account, name=name)
                userId = userList_staff[0]['id']
        with allure.step('组员添加到分组A'):
            tmk_sub.addGroupUser(groupId=groupIdA, userIds=[userId])
        with allure.step('组员更换到分组B'):
            tmk_sub.changeGroup(groupId=groupIdB, userId=userId)
        with allure.step('断言处理,分组A下无此用户，分组B下存在此用户'):
            # 分组A断言
            getAllocatedListA = tmk_sub.getAllocatedList(ID=groupIdA)
            assert len(getAllocatedListA) == 0

            # 分组B断言
            getAllocatedListB = tmk_sub.getAllocatedList(ID=groupIdB)
            custom_assert().dict_json_include(expect_key='id', expect_value=userId,
                                              dict_data=getAllocatedListB)
        with allure.step('删除对应分组A和B'):
            tmk_sub.delGroup(groupId=groupIdA)
            tmk_sub.delGroup(groupId=groupIdB)
        with allure.step('删除员工账号'):
            tmk_sub.delUser_staff(userID=userId)


@allure.feature("电销平台-填单")
@pytest.mark.usefixtures('setup_process')
class Test_apply:

    @allure.story('')
    def test_case1(self, crmManege):
        with allure.step('电销平台发起订单'):
            pass
