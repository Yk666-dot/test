import time
import ready_login
import paramunittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@paramunittest.parametrized(
    {"usn": "kai.yu", "pasw": "a000000", "admin_page": 2, "page": 2},
)
class DataCheckTest(ready_login.TestClass):
    def setParameters(self, usn, pasw, admin_page, page):
        self.usn = usn
        self.pasw = pasw
        self.admin_page = admin_page
        self.page = page

    def test_01(self):
        # 打开第二个标签,后台admin，获取后台商城所有商品名称
        self.driver.execute_script("window.open('http://admin.21cp.work/index')")
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == '欢迎登陆中塑在线':
                break
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('username').send_keys(self.usn)
        self.driver.find_element_by_name('password').send_keys(self.pasw)
        self.driver.find_element_by_id('submitBtn').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[5]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[5]/div[18]').click()
        time.sleep(3)
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_xpath('//*[@id="admui-navTabs"]/div/ul/li[3]').click()
        self.driver.implicitly_wait(20)
        admin_commodities = []
        for click in range(0, self.admin_page):
            num = len(self.driver.find_elements_by_xpath('//*[@id="table-announcement"]/tbody/tr'))
            for i in range(1, num+1):
                commodity = self.driver.find_element_by_xpath('//*[@id="table-announcement"]/tbody/tr[%i]/td[4]' % i).text
                admin_commodities.append(commodity)
            if click != self.page-1:
                self.driver.find_element_by_class_name('wb-chevron-right-mini').click()
        # 切回主网首页
        for handle in handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == '中塑在线-塑料网-21世纪塑料行业门户':
                break
        self.driver.implicitly_wait(20)
        move = self.driver.find_element_by_id("kcAccountName")
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="kcLogin"]/ul/li[1]/a').click()
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == '用户概况-中塑在线':
                break
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/a[6]').click()
        commodities = []
        for click in range(0, self.admin_page):
            num = len(self.driver.find_elements_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/div'))
            for i in range(1, num+1):
                title = self.driver.find_element_by_xpath(
                    '/html/body/div/div[3]/div[2]/div[3]/div[2]/div[%i]/div[2]' % i)
                # 获取标签里的titl
                commodity = title.get_attribute("title")
                commodities.append(commodity)
            if click != self.page-1:
                self.driver.find_element_by_class_name('layui-laypage-next').click()
        self.assertEqual(commodities, admin_commodities)


