# !/usr/bin/env python
# !coding:utf-8

import paramunittest
import time
import ready_login


@paramunittest.parametrized(
    {"expect1": "中国塑料城接待", "expect2": "余姚", "expect3": "中塑联机洽谈"},
)
class EnterimTest(ready_login.TestClass):
    def setParameters(self, expect1, expect2, expect3):
        self.expect1 = expect1
        self.expect2 = expect2
        self.expect3 = expect3

    def test_01(self):
        # 首页点击在线客服进入im
        time.sleep(3)
        self.driver.find_element_by_class_name('qq').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/ul/li[1]/a/span').click()
        handles = self.driver.window_handles
        for window in handles:
            self.driver.switch_to.window(window)
            if self.driver.title == "中塑联机洽谈":
                break
        self.driver.implicitly_wait(20)
        self.result = self.driver.find_element_by_class_name('h1dname').text
        self.assertEqual(self.expect1, self.result)
        self.driver.close()
        time.sleep(2)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        self.driver.find_element_by_class_name('layui-layer-setwin').click()

    def test_02(self):
        # 企业库点击洽谈进入im
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
        self.result = self.driver.find_element_by_class_name('h1dname')
        self.assertIn(self.expect2, self.result.text)
        self.driver.close()

    def test_03(self):
        # 首页点击联机洽谈
        time.sleep(2)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        target =self.driver.find_element_by_xpath('//*[@id="allTopBar"]/div[2]/a[3]')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        handles = self.driver.window_handles
        for window in handles:
            self.driver.switch_to.window(window)
            if self.driver.title == "中塑联机洽谈":
                break
        self.result = self.driver.title
        self.assertEqual(self.expect3, self.result)
        self.driver.close()

