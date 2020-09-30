import os
import sys
from time import sleep

sys.path.append(os.getcwd())
import pytest
import allure

from selenium import webdriver
from page.login_page import LoginPage
from base.base_webaction import BaseAction
from base.base_yml import yml_data_with_file


def data_with_key(key):
    return yml_data_with_file("login_data", key)


class TestLogin:

    def setup(self):
        self.driver = webdriver.Chrome()
        url = "http://www.xinnet.com/"
        self.driver.get(url)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.base_webaction = BaseAction(self.driver)
        self.driver.implicitly_wait(20)
        # self.login_page.click_btncloseadv()

    # # @pytest.mark.run(order=1)
    # # @pytest.mark.skipif(True, reason="done")
    # @allure.step(title="HY登录模块校验")
    # @pytest.mark.parametrize("args", data_with_key("test_login"))
    # def test_Hy_Login(self, args):
    #     title = args["title"]
    #     screen = args["screen"]
    #     hover = args["hover"]
    #     username = args["username"]
    #     password = args["password"]
    #     exist = args["exist"]
    #
    #     print(screen)
    #     allure.attach("", "标题：" + title)
    #     allure.attach("", "用例编号：" + screen)
    #     allure.attach("", "点击登录按钮")
    #     self.login_page.click_sign()
    #     allure.attach("", "输入：" + username)
    #     self.login_page.input_username(username)
    #     allure.attach("", "输入：" + password)
    #     self.login_page.input_password(password)
    #     allure.attach("", "点击登陆页立即登录按钮")
    #     self.login_page.click_login_btn()
    #
    #     if hover == "0":
    #         pass
    #
    #     elif hover == "1":
    #         self.login_page.move_to_element(self.login_page.after_login)
    #         self.login_page.click_td1()
    #
    #     elif hover == "2":
    #         sleep(1)
    #         allure.attach("", "清空登陆页密码文本框")
    #         self.login_page.clear_password()
    #         allure.attach("", "输入登陆页密码文本框")
    #         self.login_page.input_password(password)
    #         allure.attach("", "点击登陆页立即登录按钮")
    #         self.login_page.click_login_btn()
    #         sleep(1)
    #         allure.attach("", "清空登陆页密码文本框")
    #         self.login_page.clear_password()
    #         allure.attach("", "输入登陆页密码文本框")
    #         self.login_page.input_password(password)
    #         allure.attach("", "点击登陆页立即登录按钮")
    #         self.login_page.click_login_btn()
    #     try:
    #         allure.attach("", "校验页面元素是否包含：" + exist)
    #         assert self.base_webaction.is_toast_exist(exist)
    #         # self.base_webaction.screenshot(screen)
    #         # self.base_webaction.allure_attachment_type(screen, "结果截图")
    #         self.driver.quit()
    #
    #     except Exception as msg:
    #         self.base_webaction.screenshot(screen)
    #         self.base_webaction.allure_attachment_type(screen, "结果截图")
    #         print('测试Fail,异常原因:', msg)
    #         self.driver.quit()
    #         assert False

    # @pytest.mark.run(order=2)
    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="DL登录模块校验")
    @pytest.mark.parametrize("args", data_with_key("test_login_dl"))
    def test_Dl_Login(self, args):
        title = args["title"]
        screen = args["screen"]
        hover = args["hover"]
        username = args["username"]
        password = args["password"]
        label = args["label"]
        description = args["description"]
        element = args["element"]
        branch = args["branch"]
        exist = args["exist"]

        print(screen)
        allure.attach("", "标题：" + title)
        allure.attach("", "用例编号：" + screen)
        allure.attach("", "点击登录按钮")
        self.login_page.click_sign()
        allure.attach("", "点击代理商登录页签")
        self.login_page.click_dl_bookmark()
        allure.attach("", "输入：" + username)
        self.login_page.input_username(username)
        allure.attach("", "输入：" + password)
        self.login_page.input_password(password)
        allure.attach("", "点击登陆页立即登录按钮")
        self.login_page.click_login_btn()
        if hover == "0":
            pass

        elif hover == "1":
            sleep(1)
            allure.attach("", "在" + description + "悬停")
            self.base_webaction.move_to_element(self.login_page.after_login)
            allure.attach("", "点击" + description)
            self.login_page.click_css_xapth(label,element)

        try:
            if branch == "0":
                allure.attach("", "校验页面元素是否包含：" + exist)
                assert self.base_webaction.is_toast_exist(exist)
                # self.base_webaction.screenshot(screen)
                # self.base_webaction.allure_attachment_type(screen, "结果截图")
                self.driver.quit()

        except Exception as msg:
            self.base_webaction.screenshot(screen)
            self.base_webaction.allure_attachment_type(screen, "结果截图")
            print('测试Fail,异常原因:', msg)
            self.driver.quit()
            assert False

    # @pytest.mark.run(order=3)
    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="登录页面跳转逻辑")
    @pytest.mark.parametrize("args", data_with_key("test_Login_Jump"))
    def test_Login_Jump(self, args):
        title = args["title"]
        screen = args["screen"]
        hover = args["hover"]
        label = args["label"]
        description = args["description"]
        element = args["element"]
        branch = args["branch"]
        exist = args["exist"]

        print(screen)
        allure.attach("", "标题：" + title)
        allure.attach("", "用例编号：" + screen)
        allure.attach("", "点击登录按钮")
        self.login_page.click_sign()

        # HY页签中操作
        if hover == "0":
            allure.attach("", "点击" + description)
            self.login_page.click_css_xapth(label, element)

        # DL页签中操作
        if hover == "1":
            allure.attach("", "点击代理商登录页签")
            self.login_page.click_dl_bookmark()
            allure.attach("", "点击" + description)
            self.login_page.click_css_xapth(label, element)

        try:
            assert self.base_webaction.is_toast_exist(exist)
            # self.base_webaction.screenshot(screen)
            # self.base_webaction.allure_attachment_type(screen, "结果截图")
            self.driver.quit()

        except Exception as msg:
            self.base_webaction.screenshot(screen)
            self.base_webaction.allure_attachment_type(screen, "结果截图")
            print('测试Fail,异常原因:', msg)
            self.driver.quit()
            assert False
