import paramunittest
import time
import ready_login
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pag


message = "余姚!!@@43512adsgh"
while len(message) <= 200:
    message = message + "字数"


@paramunittest.parametrized(
    {"msg": message,
     },

)
class ManagementIdiomsTest(ready_login.TestClass):

    def setParameters(self, msg):
        self.msg = msg

    def test_01(self):
        # 添加常用语
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul[1]/li[4]/a').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('placeholder').click()
        self.driver.implicitly_wait(20)
        self.driver.switch_to.active_element.send_keys('余姚')
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('searchSubmit').click()
        self.driver.implicitly_wait(20)
        target = self.driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/div[5]/a')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 滚动条拖动到可见的元素去
        target.click()
        handles = self.driver.window_handles
        for window in handles:
            self.driver.switch_to.window(window)
            if self.driver.title == "中塑联机洽谈":
                break
        time.sleep(3)
        pag.click(799, 904)
        time.sleep(2)
        pag.click(1000, 658)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('addCommonWords').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/textarea').send_keys(self.msg)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div/span/b[2]').click()
        time.sleep(3)
        lens = self.driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/ul/li')
        lis = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/ul/li[%s]/p' % len(lens))
        self.assertIn(lis.text, self.msg)
        # 删除
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/ul/li[%s]/span/b[2]' % len(lens)).click()

