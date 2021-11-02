#!/usr/bin/env python
#!coding:utf-8

import unittest
import paramunittest
from selenium import webdriver
import time
import phoneName


@paramunittest.parametrized(
    {"tip": "请输入正确的企业名称！", "tip1": "企业已存在", "tip2": "请输入正确的企业名称！",
     "tip3": "已经存在", "tip4": "请输入正确的手机号！",
     "tip5": "两次密码不一致，请重新输入！", "tip6": "请输入正确的手机号", "tip7": "请输入正确的姓名！"},

)
class RegisterTest(unittest.TestCase):
    def setParameters(self, tip, tip1, tip2, tip3, tip4, tip5, tip6, tip7):
        self.tip = tip
        self.tip1 = tip1
        self.tip2 = tip2
        self.tip3 = tip3
        self.tip4 = tip4
        self.tip5 = tip5
        self.tip6 = tip6
        self.tip7 = tip7

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        url = "http://passport.21cp.work/auth/realms/zs-web/protocol/openid-connect/auth?response_type=code&client_id" \
              "=zs-www-web&redirect_uri=http%3A%2F%2Fwww.21cp.work%2Fsso%2Flogin&state=d70c5931-f9aa-4d1d-bf8e-" \
              "53a33d23617b&login=true&scope=openid"
        cls.driver.get(url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_class_name('reg').click()
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 测试企业注册
    def test_01(self):
        # 直接点击同意并注册
        self.driver.find_element_by_class_name('layui-btn').click()
        self.driver.implicitly_wait(30)
        result = self.driver.find_element_by_id('corpName-error').text
        self.assertEqual(self.tip, result)
        self.driver.refresh()

    def test_02(self):
        # 输入已注册的公司名称
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('corpName').send_keys("测试有限公司")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('corpName-error').text
        self.assertEqual(self.tip1, result)
        self.driver.refresh()

    def test_03(self):
        # 输入错误的企业名称
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('corpName').send_keys("有限企业")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('corpName-error').text
        self.assertEqual(self.tip2, result)
        self.driver.refresh()
        self.driver.find_element_by_name('corpName').send_keys("无敌！@有限公司")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('corpName-error').text
        self.assertEqual(self.tip2, result)
        self.driver.refresh()

    def test_04(self):
        # 输入已存在的手机号
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('phone').send_keys('18888648053')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('phone-error').text
        self.assertEqual(self.tip3, result)
        self.driver.refresh()

    def test_05(self):
        # 输入错误的手机号
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('phone').send_keys('1888864805')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('phone-error').text
        self.assertEqual(self.tip4, result)
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('phone').send_keys('188886480555')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('phone-error').text
        self.assertEqual(self.tip4, result)
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('phone').send_keys('!@')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('phone-error').text
        self.assertEqual(self.tip4, result)
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('phone').send_keys('中文')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('phone-error').text
        self.assertEqual(self.tip4, result)
        self.driver.refresh()

    def test_06(self):
        # 2次输入的密码不一致
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('password').send_keys("a000000")
        self.driver.find_element_by_name('confirmPassword').send_keys('a00000')
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('confirmPassword-error').text
        self.assertEqual(self.tip5, result)
        self.driver.refresh()

    def test_07(self):
        # 手机错误，无法发送验证码
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('getCode').click()
        time.sleep(2)
        result = self.driver.find_element_by_class_name('layui-layer-content').text
        self.assertEqual(self.tip6, result)

    def test_08(self):
        # 验证码60秒后可重新发送
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('phone').send_keys(phoneName.phone())
        self.driver.find_element_by_class_name('getCode').click()
        self.driver.implicitly_wait(20)
        self.assertIn("秒后重新获取", self.driver.find_element_by_class_name('getCode').text)
        time.sleep(61)
        self.assertIn("获取验证码", self.driver.find_element_by_class_name('getCode').text)

    def test_09(self):
        # 验证码错误注册失败
        self.driver.find_element_by_name('corpName').send_keys(phoneName.company())
        self.driver.find_element_by_name('contactName').send_keys(phoneName.name())
        self.driver.find_element_by_name('password').send_keys("a000000")
        self.driver.find_element_by_name('confirmPassword').send_keys('a000000')
        self.driver.find_element_by_name('code').send_keys(66666)
        self.driver.find_element_by_xpath('//*[@id="corpValidate"]/div[8]/div/i').click()
        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(3)
        result = self.driver.find_element_by_class_name('layui-layer-content').text
        self.assertEqual('验证码错误！', result)
        self.driver.find_element_by_class_name('layui-layer-btn0').click()

    def test_10(self):
        global phone
        # 使用另一个号的验证码注册失败
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('phone').clear()
        phone = phoneName.phone()
        self.driver.find_element_by_name('phone').send_keys(phone)
        self.driver.find_element_by_name('code').send_keys(666666)
        self.driver.find_element_by_class_name('layui-btn').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_class_name('layui-layer-content').text
        self.assertEqual('验证码错误！', result)
        time.sleep(2)
        self.driver.find_element_by_class_name('layui-layer-btn0').click()

    def test_11(self):
        # 注册成功,可以登录
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('getCode').click()
        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(3)
        result = self.driver.find_element_by_class_name('layui-layer-title').text
        self.assertEqual('注册成功', result)
        self.driver.refresh()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="kcNotLogin"]/a[1]').click()
        self.driver.implicitly_wait(20)
        user = self.driver.find_element_by_name("username")
        user.send_keys(phone)
        self.driver.find_element_by_name("password").send_keys("a000000")
        self.driver.find_element_by_xpath('//*[@id="login"]/input[4]').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[1]').text
        self.assertEqual('温馨提示', result)

    # 测试个人注册
    def test_12(self):
        self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[2]').click()
        self.driver.implicitly_wait(20)
        # 直接点击注册
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/a[2]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('contactName-error').text
        self.assertEqual(self.tip7, result)

    def test_13(self):
        # 输入已存在的手机号
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('phone').send_keys('18888648053')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('phone-error').text
        self.assertEqual(self.tip3, result)
        self.driver.refresh()

    def test_14(self):
        # 输入错误的手机号
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('phone').send_keys('1888864805')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('phone-error').text
        self.assertEqual(self.tip4, result)
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('phone').send_keys('188886480555')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('phone-error').text
        self.assertEqual(self.tip4, result)
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('phone').send_keys('!@')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('phone-error').text
        self.assertEqual(self.tip4, result)
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('phone').send_keys('中文')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('phone-error').text
        self.assertEqual(self.tip4, result)
        self.driver.refresh()

    def test_15(self):
        # 2次输入的密码不一致
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('password').send_keys("a000000")
        self.driver.find_element_by_name('confirmPassword').send_keys('a00000')
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('layui-btn').click()
        result = self.driver.find_element_by_id('confirmPassword-error').text
        self.assertEqual(self.tip5, result)
        self.driver.refresh()

    def test_16(self):
        # 验证码60秒后可重新发送
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('phone').send_keys(phoneName.phone())
        self.driver.find_element_by_class_name('getCode').click()
        self.driver.implicitly_wait(20)
        self.assertIn("秒后重新获取", self.driver.find_element_by_class_name('getCode').text)
        time.sleep(61)
        self.assertIn("获取验证码", self.driver.find_element_by_class_name('getCode').text)

    def test_17(self):
        # 验证码错误注册失败
        self.driver.find_element_by_name('phone').clear()
        self.driver.find_element_by_name('phone').send_keys(phoneName.phone())
        self.driver.find_element_by_name('contactName').send_keys(phoneName.name())
        self.driver.find_element_by_name('password').send_keys("a000000")
        self.driver.find_element_by_name('confirmPassword').send_keys('a000000')
        self.driver.find_element_by_name('code').send_keys(66666)
        self.driver.find_element_by_xpath('//*[@id="personValidate"]/div[6]/div/i').click()
        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(3)
        result = self.driver.find_element_by_class_name('layui-layer-content').text
        self.assertEqual('验证码错误！', result)
        self.driver.find_element_by_class_name('layui-layer-btn0').click()

    def test_18(self):
        # 使用另一个号的验证码注册失败
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('phone').clear()
        phone = phoneName.phone()
        self.driver.find_element_by_name('phone').send_keys(phone)
        self.driver.find_element_by_name('code').send_keys(666666)
        self.driver.find_element_by_class_name('layui-btn').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_class_name('layui-layer-content').text
        self.assertEqual('验证码错误！', result)
        time.sleep(2)
        self.driver.find_element_by_class_name('layui-layer-btn0').click()

    def test_19(self):
        # 注册成功,可以登录
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('getCode').click()
        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(3)
        result = self.driver.find_element_by_class_name('layui-layer-title').text
        self.assertEqual('注册成功', result)
        self.driver.refresh()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="kcNotLogin"]/a[1]').click()
        self.driver.implicitly_wait(20)
        user = self.driver.find_element_by_name("username")
        user.send_keys(phone)
        self.driver.find_element_by_name("password").send_keys("a000000")
        self.driver.find_element_by_xpath('//*[@id="login"]/input[4]').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[1]').text
        self.assertEqual('温馨提示', result)

