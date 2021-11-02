from selenium import webdriver
import unittest


# 塑博会登录
class TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        url = "https://cpe.21cp.work/login.html"
        cls.driver.get(url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        user = cls.driver.find_element_by_id("accountName")
        user.send_keys("")
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_name("password").send_keys("")
        cls.driver.implicitly_wait(30)
        #driver.find_element_by_name("captcha").send_keys("3345")
        cls.driver.find_element_by_xpath('//*[@id="login"]/input[4]').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()