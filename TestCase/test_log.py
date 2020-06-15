# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : WangJuan
# @File    : Test_Basic.py

import allure, pytest
from Common import Consts
from Common import new_tool_a
from Common import ExcelHandler
from Common import req_reload
from Common import Assert


class TestLog:
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()
    reqe = req_reload.ReqReload()
    test = Assert.Assertions()

    @allure.feature('Log')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
    @allure.severity('blocker')  # allure.story  用于定义被测功能的用例等级，blocker--测试主流程 blocker级别；
    # 详细测试 critical级别；修改个人信息-修改不是本人的用户信息，无权限操作 这个是针对接口的功能点详细测试 critical级别
    @allure.story('Get_Verifycode')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('login_01_get_verifycode'))
    def test_login_01_get_verifycode(self,case):
        """
            用例描述：获取验证码，该用例数据源来自excel
        """
        api_method, expect,api_url, headers,params= self.new.param_get_deal(case)
        response = self.reqe.req(api_method,api_url, params, headers)              # 响应有问题，需要查看日志
        self.test.assert_common(response['code'],response['body'],expect,response['time_consuming'])
        Consts.RESULT_LIST.append('True')
        print('运行case为：{0}，验证：{1}，预期结果为：{2}'.format(case['module'],case['case_description'], case['case_expect']))

    @allure.feature('Log')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
    @allure.severity('blocker')  # allure.story  用于定义被测功能的用例等级，blocker--测试主流程 blocker级别；
    # 边界值情况的测试，应该是normal级别；修改个人信息-sex参数传F和M两种类型，成功(枚举类型) 这个是针对接口的功能点
    # 详细测试 critical级别；修改个人信息-修改不是本人的用户信息，无权限操作 这个是针对接口的功能点详细测试 critical级别
    @allure.story('Log in')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('login_02_log_in'))
    def test_login_02_log_in(self, case):
        """
            用例描述：获取验证码，该用例数据源来自excel
        """
        api_method, expect,api_url, headers,params= self.new.param_get_deal(case)
        response = self.reqe.req(api_method, api_url, params, headers)  # 响应有问题，需要查看日志
        self.test.assert_common(response['code'], response['body'], expect, response['time_consuming'])
        Consts.RESULT_LIST.append('True')
        print('运行case为：{0}，验证：{1}，预期结果为：{2}'.format(case['module'],case['case_description'], case['case_expect']))

