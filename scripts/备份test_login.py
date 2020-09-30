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
        url = "http://xinnet.com/"
        self.driver.get(url)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.base_webaction = BaseAction(self.driver)
        self.driver.implicitly_wait(20)
        # self.login_page.click_btncloseadv()

    # @pytest.mark.run(order=1)
    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="HY登录模块校验")
    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_Hy_Login(self, args):
        title = args["title"]
        screen = args["screen"]
        hover = args["hover"]
        username = args["username"]
        password = args["password"]
        exist = args["exist"]

        print(screen)
        allure.attach("", "标题：" + title)
        allure.attach("", "用例编号：_" + screen)
        allure.attach("", "点击登录按钮")
        self.login_page.click_sign()
        allure.attach("", "输入：" + username)
        self.login_page.input_username(username)
        allure.attach("", "输入" + password)
        self.login_page.input_password(password)
        allure.attach("", "点击HY登陆页立即登录按钮")
        self.login_page.click_login_btn()

        if hover == "0":
            pass
            try:
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

        elif hover == "1":
            self.login_page.move_to_element(self.login_page.after_login)
            self.login_page.click_td1()
            try:
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

        elif hover == "2":
            sleep(1)
            allure.attach("", "清空HY登陆页密码文本框")
            self.login_page.clear_password()
            allure.attach("", "输入HY登陆页密码文本框")
            self.login_page.input_password(password)
            allure.attach("", "点击HY登陆页立即登录按钮")
            self.login_page.click_login_btn()
            sleep(1)
            allure.attach("", "清空HY登陆页密码文本框")
            self.login_page.clear_password()
            allure.attach("", "输入HY登陆页密码文本框")
            self.login_page.input_password(password)
            allure.attach("", "点击HY登陆页立即登录按钮")
            self.login_page.click_login_btn()
            try:
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

    # @pytest.mark.run(order=2)
    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="标题_登录页面跳转")
    @pytest.mark.parametrize("args", data_with_key("test_Hy_Login_Jump"))
    def test_Hy_Login_Jump(self, args):
        title = args["title"]
        screen = args["screen"]
        hover = args["hover"]
        label = args["label"]
        description = args["description"]
        element = args["element"]
        exist = args["exist"]

        print(screen)
        allure.attach("", "标题_" + title)
        allure.attach("", "用例编号：_" + screen)
        allure.attach("", "点击登录按钮")
        self.login_page.click_sign()
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

    # @pytest.mark.run(order=3)
    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="标题_控制台页面跳转")
    @pytest.mark.parametrize("args", data_with_key("test_HyConsole_Jump"))
    def test_HyConsole_Jump(self, args):
        title = args["title"]
        screen = args["screen"]
        hover = args["hover"]
        label = args["label"]
        username = args["username"]
        password = args["password"]
        description = args["description"]
        element = args["element"]
        description2 = args["description2"]
        element2 = args["element2"]
        exist = args["exist"]

        print(screen)
        allure.attach("", "标题_" + title)
        allure.attach("", "用例编号：_" + screen)
        allure.attach("", "点击登录按钮")
        self.login_page.click_sign()
        allure.attach("", "输入HY登陆页账号文本框")
        self.login_page.input_username(username)
        allure.attach("", "输入HY登陆页密码文本框")
        self.login_page.input_password(password)
        allure.attach("", "点击HY登陆页立即登录按钮")
        self.login_page.click_login_btn()
        allure.attach("", "点击账号连接")
        self.login_page.click_after_login()

        # 页面直接操作点击
        if hover == "0":
            allure.attach("", "点击" + description)
            sleep(1)
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

        # 新开句柄
        elif hover == "1":
            current = self.base_webaction.current_handle()
            allure.attach("", "点击" + description)
            sleep(1)
            self.login_page.click_css_xapth(label, element)
            self.base_webaction.handles_handle(current)
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

        # 悬停-账号
        elif hover == "2":
            sleep(2)
            self.login_page.move_to_element(self.login_page.kzt_login)
            allure.attach("", "点击" + description)
            sleep(1)
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

        # 悬停-费用
        elif hover == "3":
            sleep(1)
            self.login_page.move_to_element(self.login_page.kzt_cost)
            allure.attach("", "点击" + description)
            sleep(1)
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

        # 悬停-工单
        elif hover == "4":
            sleep(1)
            self.login_page.move_to_element(self.login_page.kzt_work_order)
            allure.attach("", "点击" + description)
            sleep(1)
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

        # 页面直接操作点击2次
        elif hover == "5":
            allure.attach("", "点击" + description)
            self.login_page.click_css_xapth(label, element)
            allure.attach("", "点击" + description2)
            sleep(1)
            self.login_page.click_css_xapth(label, element2)
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

        # 未实名制用户判断是否显示页面元素
        elif hover == "6":
            sleep(2)
            pass
            try:
                ret = self.base_webaction.is_displayed(self.login_page.bubble)
                print(ret)
                assert ret == True
                # self.base_webaction.screenshot(screen)
                # self.base_webaction.allure_attachment_type(screen, "结果截图")
                self.driver.quit()

            except Exception as msg:
                self.base_webaction.screenshot(screen)
                self.base_webaction.allure_attachment_type(screen, "结果截图")
                print('测试Fail,异常原因:', msg)
                self.driver.quit()
                assert False

        elif hover == "7":
            sleep(2)
            pass
            try:
                ret = self.base_webaction.is_displayed(self.login_page.bubble)
                print(ret)
                assert ret == False
                # self.base_webaction.screenshot(screen)
                # self.base_webaction.allure_attachment_type(screen, "结果截图")
                self.driver.quit()

            except Exception as msg:
                self.base_webaction.screenshot(screen)
                self.base_webaction.allure_attachment_type(screen, "结果截图")
                print('测试Fail,异常原因:', msg)
                self.driver.quit()
                assert False

        elif hover == "8":
            self.login_page.click_css_xapth(label, element)
            sleep(2)
            ret = self.base_webaction.is_displayed(self.login_page.cost_decertify)
            print(ret)
            try:
                assert ret == True
                # self.base_webaction.screenshot(screen)
                # self.base_webaction.allure_attachment_type(screen, "结果截图")
                self.driver.quit()

            except Exception as msg:
                self.base_webaction.screenshot(screen)
                self.base_webaction.allure_attachment_type(screen, "结果截图")
                print('测试Fail,异常原因:', msg)
                self.driver.quit()
                assert False

    # @pytest.mark.run(order=4)
    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="账户信息页修改行业信息")
    @pytest.mark.parametrize("args", data_with_key("test_Account_modify"))
    def test_Account_Modify(self, args):
        title = args["title"]
        screen = args["screen"]
        hover = args["hover"]
        label = args["label"]
        username = args["username"]
        password = args["password"]
        text = args["text"]
        element = args["element"]
        text2 = args["text2"]
        element2 = args["element2"]
        exist = args["exist"]
        exist2 = args["exist2"]

        print(screen)
        allure.attach("", "标题：" + title)
        allure.attach("", "用例编号：_" + screen)
        allure.attach("", "点击登录按钮")
        self.login_page.click_sign()
        allure.attach("", "输入HY登陆页账号文本框")
        self.login_page.input_username(username)
        allure.attach("", "输入HY登陆页密码文本框")
        self.login_page.input_password(password)
        allure.attach("", "点击HY登陆页立即登录按钮")
        self.login_page.click_login_btn()
        allure.attach("", "点击账号连接")
        self.login_page.click_after_login()
        allure.attach("", "点击账户资料按钮")
        sleep(1)
        self.base_webaction.move_to_element(self.login_page.kzt_login)
        sleep(1)
        self.login_page.click_kzt_data()
        allure.attach("", "点击修改按钮")
        self.base_webaction.click_element(self.login_page.account_modify)
        allure.attach("", "判断当前所属行业，如当前为‘网站’则修改为【移动APP】；当前为‘移动APP’则修改为【网站】")
        sleep(1)
        result = self.base_webaction.wait_element(self.login_page.account_categoryname).text
        if result == "网站":
            self.login_page.click_element(self.login_page.account_categoryname)
            allure.attach("", "选择‘移动APP’标签")
            sleep(1)
            self.base_webaction.click_element(self.login_page.account_app)
            sleep(1)
            self.base_webaction.clear_element(self.login_page.account_application)
            self.base_webaction.send_key(self.login_page.account_application, text)
            allure.attach("", "点击保存按钮")
            self.base_webaction.click_element(self.login_page.account_save)
            allure.attach("", "刷新页面后断言")
            self.driver.refresh()
            sleep(1)
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

        elif result == "移动APP":
            self.login_page.click_element(self.login_page.account_categoryname)
            allure.attach("", "选择‘移动APP’标签")
            sleep(1)
            self.base_webaction.click_element(self.login_page.account_web)
            sleep(1)
            self.base_webaction.clear_element(self.login_page.account_application)
            self.base_webaction.send_key(self.login_page.account_application, text2)
            allure.attach("", "点击保存按钮")
            self.base_webaction.click_element(self.login_page.account_save)
            allure.attach("", "刷新页面后断言")
            self.driver.refresh()
            sleep(1)
            try:
                assert self.base_webaction.is_toast_exist(exist2)
                # self.base_webaction.screenshot(screen)
                # self.base_webaction.allure_attachment_type(screen, "结果截图")
                self.driver.quit()

            except Exception as msg:
                self.base_webaction.screenshot(screen)
                self.base_webaction.allure_attachment_type(screen, "结果截图")
                print('测试Fail,异常原因:', msg)
                self.driver.quit()
                assert False

    # @pytest.mark.run(order=5)
    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="账户信息页跳转逻辑")
    @pytest.mark.parametrize("args", data_with_key("test_Account_Jump"))
    def test_Account_Jump(self, args):
        title = args["title"]
        screen = args["screen"]
        hover = args["hover"]
        username = args["username"]
        password = args["password"]
        description = args["description"]
        label = args["label"]
        element = args["element"]
        description2 = args["description2"]
        label2 = args["label2"]
        element2 = args["element2"]
        exist = args["exist"]

        print(screen)
        allure.attach("", "标题：" + title)
        allure.attach("", "用例编号：_" + screen)
        allure.attach("", "点击登录按钮")
        self.login_page.click_sign()
        allure.attach("", "输入HY登陆页账号文本框")
        self.login_page.input_username(username)
        allure.attach("", "输入HY登陆页密码文本框")
        self.login_page.input_password(password)
        allure.attach("", "点击HY登陆页立即登录按钮")
        self.login_page.click_login_btn()
        allure.attach("", "点击账号连接")
        self.login_page.click_after_login()
        allure.attach("", "点击账户资料按钮")
        sleep(1)
        self.base_webaction.move_to_element(self.login_page.kzt_login)
        sleep(1)
        self.login_page.click_kzt_data()
        # sleep(1)
        # ret1 = self.login_page.find_css_xapth_element(label2, element2).is_displayed()
        # print(ret1)

        if hover == "0":
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

        elif hover == "1":
            allure.attach("", "点击" + description)
            self.login_page.click_css_xapth(label, element)
            allure.attach("", "点击" + description2)
            # 判断确定按钮是否显示
            sleep(1)
            ret = self.login_page.find_css_xapth_element(label2, element2).is_displayed()
            print(ret)
            try:
                assert ret == True
                # self.base_webaction.screenshot(screen)
                # self.base_webaction.allure_attachment_type(screen, "结果截图")
                self.driver.quit()

            except Exception as msg:
                self.base_webaction.screenshot(screen)
                self.base_webaction.allure_attachment_type(screen, "结果截图")
                print('测试Fail,异常原因:', msg)
                self.driver.quit()
                assert False

    # @pytest.mark.run(order=6)
    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="实名认证页跳转逻辑")
    @pytest.mark.parametrize("args", data_with_key("test_Verified_Jump"))
    def test_Verified_Jump(self, args):
        title = args["title"]
        screen = args["screen"]
        hover = args["hover"]
        username = args["username"]
        password = args["password"]
        description = args["description"]
        label = args["label"]
        element = args["element"]
        description2 = args["description2"]
        label2 = args["label2"]
        element2 = args["element2"]
        description3 = args["description3"]
        label3 = args["label3"]
        element3 = args["element3"]
        exist = args["exist"]

        print(screen)
        allure.attach("", "标题：" + title)
        allure.attach("", "用例编号：_" + screen)
        allure.attach("", "点击登录按钮")
        self.login_page.click_sign()
        allure.attach("", "输入HY登陆页账号文本框")
        self.login_page.input_username(username)
        allure.attach("", "输入HY登陆页密码文本框")
        self.login_page.input_password(password)
        allure.attach("", "点击HY登陆页立即登录按钮")
        self.login_page.click_login_btn()
        allure.attach("", "点击账号连接")
        self.login_page.click_after_login()
        allure.attach("", "点击实名认证按钮")
        sleep(1)
        self.base_webaction.move_to_element(self.login_page.kzt_login)
        sleep(1)
        self.base_webaction.click_element(self.login_page.kzt_verified)
        allure.attach("", "判断是否弹出引导页，并关闭引导页")
        self.login_page.turn_off_boot()

        if hover == "0":
            allure.attach("", "点击" + description)
            self.login_page.click_css_xapth(label, element)
            sleep(1)
            allure.attach("", "点击" + description2)
            self.login_page.click_css_xapth(label2, element2)
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

        elif hover == "1":
            # 获取当前句柄
            current = self.base_webaction.current_handle()
            allure.attach("", "点击" + description)
            self.login_page.click_css_xapth(label, element)
            # 获取全部句柄
            self.base_webaction.handles_handle(current)
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

        elif hover == "2":
            allure.attach("", "点击" + description)
            self.login_page.click_css_xapth(label, element)
            allure.attach("", "点击" + description2)
            sleep(1)
            self.login_page.click_css_xapth(label2, element2)
            allure.attach("", "点击" + description3)
            sleep(1)
            self.login_page.click_css_xapth(label3, element3)
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

        elif hover == "3":
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

    # @pytest.mark.run(order=7)
    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="安全设置页跳转逻辑")
    @pytest.mark.parametrize("args", data_with_key("test_Safety_Jump"))
    def test_Safety_Jump(self, args):
        title = args["title"]
        screen = args["screen"]
        hover = args["hover"]
        username = args["username"]
        password = args["password"]
        description = args["description"]
        label = args["label"]
        element = args["element"]
        description2 = args["description2"]
        label2 = args["label2"]
        element2 = args["element2"]
        description3 = args["description3"]
        label3 = args["label3"]
        element3 = args["element3"]
        exist = args["exist"]

        print(screen)
        allure.attach("", "标题：" + title)
        allure.attach("", "用例编号：_" + screen)
        allure.attach("", "点击登录按钮")
        self.login_page.click_sign()
        allure.attach("", "输入HY登陆页账号文本框")
        self.login_page.input_username(username)
        allure.attach("", "输入HY登陆页密码文本框")
        self.login_page.input_password(password)
        allure.attach("", "点击HY登陆页立即登录按钮")
        self.login_page.click_login_btn()
        allure.attach("", "点击账号连接")
        self.login_page.click_after_login()
        allure.attach("", "点击账户资料按钮")
        sleep(1)
        self.base_webaction.move_to_element(self.login_page.kzt_login)
        sleep(1)
        self.base_webaction.click_element(self.login_page.kzt_data)
        allure.attach("", "点击安全设置按钮")
        self.base_webaction.click_element(self.login_page.account_safety)

        if hover == "0":
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

        # 返回安全设置页
        elif hover == "1":
            allure.attach("", "点击" + description)
            self.login_page.click_css_xapth(label, element)
            allure.attach("", "点击" + description2)
            self.login_page.click_css_xapth(label2, element2)
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

        # 选择其它验证方式
        elif hover == "2":
            allure.attach("", "点击" + description)
            self.login_page.click_css_xapth(label, element)
            allure.attach("", "点击" + description2)
            sleep(1)
            self.login_page.click_css_xapth(label2, element2)
            allure.attach("", "点击" + description3)
            sleep(1)
            self.login_page.click_css_xapth(label3, element3)
            try:
                self.driver.refresh()
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

        # 多窗口
        elif hover == "3":
            current = self.base_webaction.current_handle()
            allure.attach("", "点击" + description)
            self.login_page.click_css_xapth(label, element)
            allure.attach("", "点击" + description2)
            sleep(1)
            self.login_page.click_css_xapth(label2, element2)
            allure.attach("", "点击" + description3)
            sleep(1)
            self.login_page.click_css_xapth(label3, element3)
            self.base_webaction.handles_handle(current)
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
