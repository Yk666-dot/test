import paramunittest
import time
import ready_login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@paramunittest.parametrized(
    {"group": "余姚"},

)
class SearchTest(ready_login.TestClass):
    def setParameters(self, group):
        self.group = group

    # 搜索群名
    def test_01(self):
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
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/input').send_keys(self.group)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/input').send_keys(Keys.ENTER)
        self.driver.implicitly_wait(20)
        # 验证单聊
        single_lis = self.driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[1]/div/ul/li')
        for s in single_lis:
            self.assertIn(self.group, s.text)
        # 验证群聊
        group_lis = self.driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div/ul/li')
        for g in group_lis:
            self.assertIn(self.group, g.text)

    # 测试更多单聊和更多群聊
    def test_02(self):
        # 更多单聊
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/span').click()
        self.driver.implicitly_wait(20)
        single_lis = self.driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/ul/li')
        # 必大于3个
        self.assertTrue(len(single_lis) > 3)
        for s in single_lis:
            self.assertIn(self.group, s.text)
        # 更多群聊
        target = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div/div/span')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.driver.implicitly_wait(20)
        target.click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[2]/div/div/span').click()
        self.driver.implicitly_wait(20)
        group_lis = self.driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/ul/li')
        # 必大于3个
        self.assertTrue(len(group_lis) > 3)
        for g in group_lis:
            self.assertIn(self.group, g.text)

    # 测试点击与对应公司洽谈
    def test_03(self):
        expect = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/div[1]/div/ul/li[1]/p').text
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/ul/li[1]').click()
        result = self.driver.find_element_by_class_name('h1dname').text
        self.assertEqual(expect, result)
