# coding:utf-8
import os
import sys
from time import sleep

sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_webaction import BaseAction


class LoginPage(BaseAction):
    # 活动广告关闭按钮
    btncloseadv = By.CSS_SELECTOR, ".btnCloseAdv"

    """首页区域"""
    # 首页【登录】按钮
    sign = By.CSS_SELECTOR, ".sign"

    # 首页【免费注册】按钮
    regist = By.CSS_SELECTOR, ".regist"

    # 首页【安全退出】按钮
    td1 = By.CSS_SELECTOR, ".td1>a"

    # 首页登录后【账号】按钮
    after_login = By.CSS_SELECTOR, ".username"

    """登录页区域"""
    # HY登陆页【账号】文本框按钮
    username = By.CSS_SELECTOR, "#username"

    # HY登陆页【密码】文本框按钮
    password = By.CSS_SELECTOR, "#password"

    # HY登陆页【立即登录】按钮
    login_btn = By.CSS_SELECTOR, ".login_btn"

    # HY登陆页【立即注册】按钮
    dl_toreg = By.CSS_SELECTOR, "#toReg"

    # HY登陆页【忘记密码】按钮
    dl_login_float_r = By.CSS_SELECTOR, "#repassword"

    # 【代理商登录】页签
    dl_bookmark = By.CSS_SELECTOR, "#dldiv>h3"

    # DL登陆页【申请代理商】按钮
    application_agent = By.CSS_SELECTOR, "#toReg"

    '''控制台页'''
    # 控制台页【立即认证】按钮
    kzt_authenticate_now = By.XPATH, ".//*[@id='noRealUser_tip']/div/div/div/div/p[3]/a"

    # 控制台页【查看详情】按钮
    kzt_see_details = By.XPATH, ".//*[@id='realUserPass_tip']/div/div/div/div/p[3]/a"

    # 控制台页【去升级】按钮
    kzt_to_upgrade = By.CSS_SELECTOR, "#goLevel"

    # 控制台页【充值】按钮
    kzt_goLevel = By.CSS_SELECTOR, ".a-01"

    # 控制台页【交易明细】按钮
    kzt_transaction = By.XPATH, "html/body/div[2]/div/div[2]/div[2]/div[1]/p[2]/a[1]"

    # 控制台页【资金冻结明细】按钮
    kzt_freeze = By.XPATH, "html/body/div[2]/div/div[2]/div[2]/div[1]/p[2]/a[2]"

    # 控制台页【我的优惠券】按钮
    kzt_me_coupon = By.XPATH, "html/body/div[2]/div/div[2]/div[2]/div[1]/p[2]/a[3]"

    # 控制台页【提现】按钮
    kzt_withdraw = By.XPATH, "html/body/div[2]/div/div[2]/div[2]/div[2]/p[2]/a[1]"

    # 控制台页【返利】按钮
    kzt_cash_back = By.XPATH, "html/body/div[2]/div/div[2]/div[2]/div[2]/p[2]/a[2]"

    # 控制台页【箭头云】按钮
    kzt_arrow_cloud = By.CSS_SELECTOR, "#CS"

    # 控制台页【域名】按钮
    kzt_domain_name = By.CSS_SELECTOR, "#domain"

    # 控制台页【云虚拟主机】按钮
    kzt_cloud_hosting = By.CSS_SELECTOR, "#virtual"

    # 控制台页【企业邮箱】按钮
    kzt_mail = By.CSS_SELECTOR, "#mail"

    # 控制台页【服务市场】按钮
    kzt_market = By.CSS_SELECTOR, "#market"

    # 控制台页【备案】按钮
    kzt_rrcord = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[4]/a"

    # 控制台页【帮助中心】按钮
    kzt_help = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[5]/a"

    # 控制台页【购物车】按钮
    kzt_shopping = By.CSS_SELECTOR, ".iconfont.icon-xincard"

    # 控制台页【未读消息】数量
    kzt_msgnum = By.CSS_SELECTOR, "#msgNum"

    # 控制台页【未读消息-查看全部】按钮
    kzt_msgnum_view = By.CSS_SELECTOR, "#checkAll"

    # 控制台页【我的工单】数量
    kzt_myorder = By.CSS_SELECTOR, "#myOrder"

    # 控制台页【急需续费产品】数量
    kzt_renewal = By.CSS_SELECTOR, "#productJxxfNum"

    '''控制台页【产品】下拉框'''
    kzt_product = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[1]/div[3]/a/span"

    '''控制台页【账号会员邮箱】下拉框'''
    kzt_login = By.CSS_SELECTOR, ".maxText.mg_rig3"

    # 控制台页【未实名制提示制气泡】
    bubble = By.XPATH, "html/body/div[2]/div/div[1]/p/a"

    # 控制台页【账户资料】按钮
    kzt_data = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[1]/ul/li[1]/a"

    # 控制台页【实名认证】按钮
    kzt_verified = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[1]/ul/li[2]/a"

    # 控制台页【动态口令】按钮
    kzt_dynamic = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[1]/ul/li[3]/a"

    # 控制台页【安全退出】按钮
    kzt_drop_out = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[1]/ul/li[4]/a"

    '''控制台页【费用】下拉框'''
    kzt_cost = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[2]/a/span"

    # 控制台页【费用-充值】按钮
    kzt_fy_goLevel = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[2]/ul/li[1]/a"

    # 控制台页【费用-自助提现】按钮
    kzt_self_withdrawal = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[2]/ul/li[2]/a"

    # 控制台页【费用-订单】按钮
    kzt_order = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[2]/ul/li[3]/a"

    # 控制台页【费用-发票】按钮
    kzt_invoice = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[2]/ul/li[4]/a"

    # 控制台页【费用-优惠券】按钮
    kzt_coupon = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[2]/ul/li[5]/a"

    # 控制台页【费用-返利】按钮
    kzt_cash_back1 = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[2]/ul/li[6]/a"

    # 控制台页【费用-收支明细】按钮
    kzt_revenue = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[2]/ul/li[7]/a"

    '''控制台页【工单】下拉框'''
    kzt_work_order = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[3]/a/span"

    # 控制台页【工单-我的工单】按钮
    kzt_my_work_order = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[3]/ul/li[1]/a"

    # 控制台页【工单-收支明细】按钮
    kzt_submit_work_order = By.XPATH, "html/body/div[1]/div[1]/div[1]/div[3]/div[3]/ul/li[2]/a"

    '''账户中心【侧边栏】'''
    # 账户中心【侧边栏】【账户信息】
    account_sidebar = By.CSS_SELECTOR, "#accountInfoA"

    # 账户中心【侧边栏】【实名认证】
    account_smrz = By.CSS_SELECTOR, "#realNameA"

    # 账户中心【侧边栏】【安全设置】
    account_safety = By.CSS_SELECTOR, "#safeSetA"

    '''账户资料页'''
    # 账户资料页【行业信息】【修改】按钮
    account_modify = By.XPATH, ".//*[@id='industryInfoModify_tip']/div/div/div/ul/li[2]/div[2]/p/a"

    # 账户资料页【行业信息】【所属行业】下拉框
    account_categoryname = By.XPATH, ".//*[@id='categoryName']"

    # 账户资料页【行业信息】【所属行业】下拉框中【网站】
    account_web = By.XPATH, ".//*[@id='categoryList']/li[1]"

    # 账户资料页【行业信息】【所属行业】下拉框中【移动APP】
    account_app = By.XPATH, ".//*[@id='categoryList']/li[2]"

    # 账户资料页【行业信息】【应用类型】文本框
    account_application = By.XPATH, ".//*[@id='applicationType']"

    # 账户资料页【行业信息】【保存】按钮
    account_save = By.XPATH, ".//*[@id='industryInfoEdit_tip']/div/div/div/ul/li[3]/div/a[2]"

    # 账户资料页【联系人管理】【删除】按钮
    account_delete = By.XPATH, ".//*[@id='contacts']/div/div[1]/table/tbody/tr[2]/td[5]/a[2]"

    # 账户资料页【联系人管理】【删除】【确定】按钮
    account_del_determine = By.XPATH, ".//*[@id='removeContact']/div[3]/a"

    # 账户资料页【联系人管理】【新增联系人】按钮
    account_newpeople = By.CSS_SELECTOR, ".xwBtn.xwBtn-ss.btnWhite"

    # 账户资料页【联系人管理】【新增联系人】【确定】按钮
    account_newpeople_determine = By.XPATH, ".//*[@id='updContact']/div[3]/a"

    # 账户资料页【联系人管理】【修改】按钮
    account_contact_modify = By.XPATH, ".//*[@id='contacts']/div/div[1]/table/tbody/tr[2]/td[5]/a[1]"

    # 账户资料页【联系人管理】【修改】【确定】按钮
    account_modify_determine = By.XPATH, ".//*[@id='updContact']/div[3]/a"

    '''实名认证'''
    # 实名认证页【引导页】【跳过引导】按钮
    smrz_jump_over = By.CSS_SELECTOR, ".close-btn.close-btn-led"

    # 实名认证页【账户实名认证指引】连接
    smrz_guidelines = By.XPATH, ".//*[@id='home']/div/h4/a"

    # 实名认证页【立即企业认证】按钮
    smrz_enterprise = By.CSS_SELECTOR, ".xwBtn.xwBtn-bb.btnWhite.btnCompany"

    # 实名认证页【立即企业认证/立即个人认证】弹窗中【确定】按钮
    smrz_enterprise_determine = By.CSS_SELECTOR, ".xwBtn.btnRed.btnYes"

    # 实名认证页【企业/个人认证页】【重新选择认证类型】按钮
    smrz_toHome = By.CSS_SELECTOR, "#toHome"

    # 实名认证页【立即个人认证】按钮
    smrz_personal = By.CSS_SELECTOR, ".xwBtn.xwBtn-bb.btnWhite.btnPerson"

    '''安全设置页'''
    # 安全设置页【登录密码】【修改】按钮
    safety_login_password = By.XPATH, ".//*[@id='pageVender']/div/div/div/div[2]/ul/li[1]/p[4]/a"

    # 安全设置页【邮箱绑定】【修改】按钮
    safety_email_binding = By.XPATH, ".//*[@id='pageVender']/div/div/div/div[2]/ul/li[2]/p[4]/a"

    # 安全设置页【手机绑定】【修改】按钮
    safety_phone_binding = By.XPATH, ".//*[@id='mobileButton']"

    # 安全设置页【动态口令验证】【立即验证】按钮
    safety_password_binding = By.XPATH, ".//*[@id='dynamicButton']"

    # 安全设置页【二级页面】【返回安全设置】按钮
    safety_result = By.CSS_SELECTOR, ".a1-left.a-grey.fs12"

    # 安全设置页【二级页面】【选择其他方式验证】按钮
    safety_other = By.CSS_SELECTOR, ".a-blue"

    # 安全设置页【验证方式 -手机验证方式】【去验证】按钮
    safety_other_to_verify = By.XPATH, ".//*[@id='pageVender']/div/div/div/ul/li[1]/p/a"

    # 安全设置页【验证方式 -人工服务】【查看详情】按钮
    safety_other_see_details = By.XPATH, ".//*[@id='pageVender']/div/div/div/ul/li[2]/p/a"

    # 安全设置页【验证方式 】【返回】按钮
    safety_other_return = ".a1-left.a-grey.fs12"

    '''费用中心'''
    # 自助提现页【现在去认证】按钮
    cost_decertify = By.XPATH, ".//*[@id='realNameWin']/div/div[2]/div/a"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # 点击显示 (init 里面可以去写已经确定的这个模块所有的前置功能)

    """特殊方法"""
    # 特殊查找
    def find_css_xapth_element(self, label, ele):
        # CSS定位
        if label == "0":
            element = WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ele)))
            return element
        # XPATH定位
        elif label == "1":
            element = WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located((By.XPATH, ele)))
            return element

    # 特殊点击
    def click_css_xapth(self, label, ele):
        self.find_css_xapth_element(label, ele).click()

    """首页区域操作"""

    # 点击活动广告关闭按钮
    def click_btncloseadv(self):
        self.click_element(self.btncloseadv)

    # 点击首页登陆按钮
    def click_sign(self):
        self.click_element(self.sign)

    # 点击首页安全退出按钮
    def click_td1(self):
        self.click_element(self.td1)

    # 点击首页登录后账号按钮
    def click_after_login(self):
        self.click_element(self.after_login)

    """登录页区域操作"""

    # 点击代理商登录页签
    def click_dl_bookmark(self):
        self.click_element(self.dl_bookmark)

    # 输入HY登陆页账号文本框
    def input_username(self, text="hy5270270@xinnet.com"):
        self.send_key(self.username, text)

    # 输入HY登陆页密码文本框
    def input_password(self, text="tianmo231"):
        self.send_key(self.password, text)

    # 清空HY登陆页密码文本框
    def clear_password(self, text="tianmo231"):
        self.clear_element(self.password)

    # 点击HY登陆页立即登录按钮
    def click_login_btn(self):
        self.click_element(self.login_btn)

    # 点击HY登陆页立即注册按钮
    def click_dl_toreg(self):
        self.click_element(self.dl_toreg)

    # 点击HY登陆页忘记密码按钮
    def click_dl_login_float_r(self):
        self.click_element(self.dl_login_float_r)

    '''控制台区域'''

    # 点击控制台页【未读消息-查看全部】按钮
    def click_kzt_msgnum_view(self):
        self.click_element(self.kzt_msgnum_view)

    # 点击控制台页【账户资料】按钮
    def click_kzt_data(self):
        self.click_element(self.kzt_data)

    # 实名认证页面，跳过引导
    def turn_off_boot(self):
        sleep(2)
        result = self.is_displayed(self.smrz_jump_over)
        if result == True:
            self.click_element(self.smrz_jump_over)
        else:
            pass
