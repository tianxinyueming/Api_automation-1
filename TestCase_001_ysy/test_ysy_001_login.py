# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : WangJuan
# @File    : Test_Basic.py

import allure, pytest, os, sys
from Common import new_tool_a
from Common import ExcelHandler


@allure.feature('一生约--登录')
@allure.severity('blocker')
@allure.story('登录')
class TestYsy001Login(object):
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    # @allure.feature('ysy_Login')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
    # @allure.severity('blocker')  # allure.severity 用于定义被测功能的用例等级，blocker--测试主流程 blocker级别；
    # # 详细测试 critical级别；修改个人信息-修改不是本人的用户信息，无权限操作 这个是针对接口的功能点详细测试 critical级别
    # @allure.story('Get_Verifycode')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('login_001_get_verifycode'))
    def test_login_001_get_verifycode(self,case):
        """
            用例描述：获取验证码
        """
        self.new.write_data_to_json()       # 初始化相关数据
        self.new.test_case_method(case, 'post')

    @pytest.mark.parametrize('case', excel.get_excel_data('login_02_log_in'))
    def test_login_002_log_in(self, case):
        """
            用例描述：验证码登录
        """
        self.new.test_case_method(case, 'post')

    @pytest.mark.parametrize('case', excel.get_excel_data('login_003_get_User_Privacy_Policy'))
    def test_login_003_get_User_Privacy_Policy(self, case):
        """
            用例描述：用户隐私协议
        """
        self.new.test_case_method(case, 'get')


    @pytest.mark.parametrize('case', excel.get_excel_data('login_004_get_Member_Order'))
    def test_login_004_get_Member_Order(self, case):
        """
            用例描述：获取成员拖动顺序
        """
        self.new.test_case_method(case, 'get')


    @pytest.mark.parametrize('case', excel.get_excel_data('login_005_family_Info'))
    def test_login_005_family_Info(self, case):
        """
            用例描述：家庭信息
        """
        self.new.test_case_method(case, 'get')


    @pytest.mark.parametrize('case', excel.get_excel_data('login_006_health_Plan'))
    def test_login_006_health_Plan(self, case):
        """
            用例描述：首页-健康计划
        """
        self.new.test_case_method(case, 'get')


    @pytest.mark.parametrize('case', excel.get_excel_data('login_007_get_Not_Label_Family_User'))
    def test_login_007_get_Not_Label_Family_User(self, case):
        """
            用例描述：获取成员标签及用户信息
        """
        self.new.test_case_method(case, 'get')


    @pytest.mark.parametrize('case', excel.get_excel_data('login_007_get_Not_Label_Family_User'))
    def test_login_007_get_Not_Label_Family_User(self, case):
        """
            用例描述：获取成员标签及用户信息
        """
        self.new.test_case_method(case, 'get')


    @pytest.mark.parametrize('case', excel.get_excel_data('login_008_family_house_list'))
    def test_login_008_family_house_list(self, case):
        """
            用例描述：获取用户房屋列表
        """
        self.new.test_case_method(case, 'get')


    @pytest.mark.parametrize('case', excel.get_excel_data('login_009_update_Bind'))
    def test_login_009_update_Bind(self, case):
        """
            用例描述：设置默认房屋
            设置之后test_ysy_002_invitation即将使用绑定了道闸设备的小区
        """
        self.new.test_case_method(case, 'post')

    @pytest.mark.parametrize('case', excel.get_excel_data('login_010_versionInfo_android'))
    def test_login_010_versionInfo_android(self, case):
        """
            用例描述：设置默认房屋
            设置之后test_ysy_002_invitation即将使用绑定了道闸设备的小区
        """
        self.new.test_case_method(case, 'get')

    @pytest.mark.parametrize('case', excel.get_excel_data('login_011_versionInfo_ios'))
    def test_login_011_versionInfo_ios(self, case):
        """
            用例描述：设置默认房屋
            设置之后test_ysy_002_invitation即将使用绑定了道闸设备的小区
        """
        self.new.test_case_method(case, 'get')