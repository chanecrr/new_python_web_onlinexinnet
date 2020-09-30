from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
url = "http://xinnet.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(20)
from page.login_page import LoginPage
from base.base_webaction import BaseAction

login_page = LoginPage(driver)
base_webaction = BaseAction(driver)

'''账户资料-联系人管理中判断显示删除-确定按钮'''
# login_page.click_sign()
#
# # login_page.input_username("chenran@xinnet.com")
# # login_page.input_password("tianmo231")
#
# login_page.input_username()
# login_page.input_password()
#
# login_page.click_login_btn()
# login_page.click_after_login()
#
# # 点击账户资料按钮
# base_webaction.move_to_element(login_page.kzt_login)
# login_page.click_kzt_kzt_data()
# sleep(2)
# ret1 = base_webaction.is_displayed(login_page.account_del_determine)
# print(ret1)
# sleep(2)
# # 点击删除按钮
# base_webaction.click_element(login_page.account_delete)
# sleep(2)
# ret2 = base_webaction.is_displayed(login_page.account_del_determine)
# print(ret2)
# driver.quit()

'''账户资料-联系人管理中判断显示删除-确定按钮'''
login_page.click_sign()

# login_page.input_username("chenran@xinnet.com")
# login_page.input_password("tianmo231")

login_page.input_username()
login_page.input_password()

login_page.click_login_btn()
login_page.click_after_login()

# 点击账户资料按钮
base_webaction.move_to_element(login_page.kzt_login)
login_page.click_kzt_kzt_data()
sleep(2)
ret1 = base_webaction.is_displayed(login_page.account_newpeople_determine)
print(ret1)
sleep(2)
# 点击心新增按钮
base_webaction.click_element(login_page.account_newpeople)
sleep(2)
ret2 = base_webaction.is_displayed(login_page.account_newpeople_determine)
print(ret2)
driver.quit()