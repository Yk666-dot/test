#!/usr/bin/env python
# !coding:utf-8
from selenium import webdriver
import unittest
import paramunittest


# 多个字典可以多次循环执行

class TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        url = "http://passport.21cp.work/auth/realms/zs-web/protocol/openid-connect/auth?response_type=code&client_id" \
          "=zs-www-web&redirect_uri=http%3A%2F%2Fwww.21cp.work%2Fsso%2Flogin&state=d70c5931-f9aa-4d1d-bf8e-" \
          "53a33d23617b&login=true&scope=openid"
        cls.driver.get(url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        user = cls.driver.find_element_by_name("username")
        user.send_keys("kaiyu12")
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_name("password").send_keys("123456")
        cls.driver.implicitly_wait(30)
        #driver.find_element_by_name("captcha").send_keys("3345")
        cls.driver.find_element_by_xpath('//*[@id="login"]/input[4]').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
