import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import unittest
import pyautogui as pag
import ready_login


class PowerTest(ready_login.TestClass):
    # 前置条件
    def test_01(self):
        self.driver.implicitly_wait(20)
        move = self.driver.find_element_by_id("kcAccountName")
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="kcLogin"]/ul/li[6]/a').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="kcNotLogin"]/a[1]').click()
        self.driver.implicitly_wait(20)
        user = self.driver.find_element_by_name("username")
        user.send_keys(13099827731)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name("password").send_keys("zs810019")
        self.driver.implicitly_wait(30)
        # driver.find_element_by_name("captcha").send_keys("3345")
        self.driver.find_element_by_xpath('//*[@id="login"]/input[4]').click()

    # 验证子账号不可更换
    def test_02(self):
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
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/div[1]/div[1]/a/img').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('layui-border-blue').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_class_name('layui-layer-content').text
        self.assertEqual("请联系主账号进行兑换", result)
        move = self.driver.find_element_by_id("kcAccountName")
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="kcLogin"]/ul/li[6]/a').click()

    # 验证未认证企业账号不可更换
    def test_03(self):
        self.driver.implicitly_wait(20)
        user = self.driver.find_element_by_name("username")
        user.send_keys(15969583909)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name("password").send_keys(123456)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="login"]/input[4]').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-border-blue').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_class_name('layui-layer-content').text
        self.driver.implicitly_wait(20)
        self.assertEqual("完成企业基本信息和工商信息认证才可兑换", result)
        move = self.driver.find_element_by_id("kcAccountName")
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="kcLogin"]/ul/li[6]/a').click()

    # 验证未认证个人账号不可更换
    def test_04(self):
        self.driver.implicitly_wait(20)
        user = self.driver.find_element_by_name("username")
        user.send_keys(16675444054)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name("password").send_keys(123456)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="login"]/input[4]').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-border-blue').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_class_name('layui-layer-content').text
        self.assertEqual("完成身份认证才可兑换", result)


if __name__ == '__main__':
   ready_login.main()