# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
import time
import parameter


class ajTest(unittest.TestCase):
    qybj = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[1]/div[2]').click()
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://192.168.1.101/html/anjianTest/#/login")
        cls.driver.find_element_by_name("username").send_keys(13605014662)
        cls.driver.find_element_by_name("password").send_keys(123456)
        cls.driver.find_element_by_xpath('//*[@id="app"]/div/form/button').click()
        time.sleep(2)

#xpath = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div/span'
#driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div/span').click
#driver.find_element_by_xpath(xpath).click()
    @classmethod
    def tearDownClass(cls):
        print("测试结束")

    def test_login(self):
        username = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div/span').text
        self.assertEqual(username, "吴府去是是")
    
    # 测试注册地址长数据
    def test_AjQyxx005(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[1]/div[2]').click()
        dz = '//*[@id="app"]/div/div[3]/section/div/table[1]/tr[3]/td[2]/div/div/input'
        zcdz = self.driver.find_element_by_xpath(dz)
        zcdz.clear()
        zcdz.send_keys(parameter.Laddress)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/button[2]/span').click()
        jd = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/table[1]/tr[3]/td[2]/div').text
        time.sleep(2)
        self.assertEqual(jd , parameter.Laddress)

#测试编辑合法数据
    def test_AjQyxx006(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[1]/div[2]').click()



if __name__=='__main__':
    unittest.main()