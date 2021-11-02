from selenium import webdriver
import unittest


# 塑博会登录
class TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        url = "https://admin-crm.21cp.work"
        cls.driver.get(url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        user = cls.driver.find_element_by_name("username")
        user.send_keys("kai.yu")
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_name("password").send_keys("a000000")
        cls.driver.implicitly_wait(30)
        #driver.find_element_by_name("captcha").send_keys("3345")
        cls.driver.find_element_by_id('submitBtn').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()