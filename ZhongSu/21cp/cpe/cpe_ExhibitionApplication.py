import unittest
import paramunittest
from selenium import webdriver
import time
import phoneName


class ExhibitionApplicationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        url = "https://cpe.21cp.work/login.html"
        cls.driver.get(url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        # 从参展申请按钮进入
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/a[1]').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_class_name('main-title').text
        self.assertEqual(result, "参展申请")
        self.driver.find_element_by_class_name('nav-login').click()

    def test_02(self):
        # 从登录按钮下方的按钮进入
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="layuiForm"]/div[6]/div[1]/a[1]').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_class_name('main-title').text
        self.assertEqual(result, "参展申请")

    def test_03(self):
        # 公司名称长度校验
        self.driver.find_element_by_name('corpName').send_keys('沈阳')
        self.driver.find_element_by_name('phone').send_keys(phoneName.phone())
        self.driver.find_element_by_class_name('enter-btn').click()
        time.sleep(3)
        result = self.driver.find_element_by_class_name('layui-layer-content').text
        self.assertEqual('公司名称格式错误，公司名称只允许输入中文名称、字母、中英文括号，长度5-30位', result)
        self.driver.find_element_by_name('corpName').clear()

    def test_04(self):
        # 公司名称带特殊符号
        self.driver.find_element_by_name('corpName').send_keys('!@#$$%有限公司')
        self.driver.find_element_by_class_name('enter-btn').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_class_name('layui-layer-content').text
        self.assertEqual('公司名称格式错误，公司名称只允许输入中文名称、字母、中英文括号，长度5-30位', result)
        self.driver.refresh()

    def test_05(self):
        # 手机号长度校验
        self.driver.implicitly_wait(20)
        phonelist = ['1309928339', '1398829332@', '130999288321']
        self.driver.find_element_by_name('corpName').send_keys(phoneName.company())
        for phone in phonelist:
            self.driver.find_element_by_name('phone').send_keys(phone)
            self.driver.find_element_by_class_name('enter-btn').click()
            time.sleep(2)
            result = self.driver.find_element_by_class_name('layui-layer-content').text
            self.assertEqual('手机号码格式错误', result)
            self.driver.find_element_by_name('phone').clear()
        self.driver.refresh()

    def test_06(self):
        # 公司手机查重
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('corpName').send_keys('沈阳四维高聚物塑胶有限公司')
        self.driver.find_element_by_name('phone').send_keys(13905745983)
        self.driver.find_element_by_class_name('enter-btn').click()
        self.driver.implicitly_wait(20)
        self.num = len(self.driver.find_elements_by_xpath('//*[@id="modalTable"]/tbody/tr'))
        form = self.driver.find_element_by_xpath('//*[@id="modalTable"]/tbody').text
        self.assertEqual(self.num, 2)
        self.assertIn('沈阳四维高聚物塑胶有限公司', form)
        self.assertIn('5983', form)

    def test_07(self):
        # 验证查重列表只能单选
        for i in range(1, self.num+1):
            self.driver.find_element_by_xpath('//*[@id="modalTable"]/tbody/tr[%i]/td[1]/input' % i).click()
            time.sleep(10)
        num = len(self.driver.find_elements_by_class_name('active'))
        self.assertEqual(1, num)

    def test_08(self):
        # 选择存在，去登陆
        self.driver.find_element_by_class_name('cancel').click()
        time.sleep(3)
        self.assertEqual("第二十三届塑博会登录界面_中国塑料博览会官方网站", self.driver.title)

    def test_09(self):
        # 选择不存在，去申请
        self.driver.find_element_by_class_name('enter').click()
        time.sleep(3)
        self.assertEqual('第二十三届塑博会参展申请_中国塑料博览会官方网站', self.driver.title)







if __name__ == '__main__':
    unittest.main()

