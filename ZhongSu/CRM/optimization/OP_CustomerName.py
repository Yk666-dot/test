# noinspection PyBroadException
from selenium import webdriver
import crm_login
import time
import phoneName


class CustomerNameTest(crm_login.TestClass):
    # 新建合同,客户名称可选择主标题或副标题
    def test_01(self):
        global name
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/div').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/ul/div[3]/a').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div[3]/div[3]/table/tbody/tr/td[2]/div/a').click()
        self.driver.implicitly_wait(20)
        name = []
        i = 1
        while i > 0:
            try:
                element = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[2]/div/div/div/div[%i]/input' % i)
                # 获取输入框中文本
                value = element.get_attribute('value')
                name.append(value)
                i += 1
            except:
                break
        target = self.driver.find_element_by_xpath('//*[@id="tab-1"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="pane-1"]/div/div[1]/div[1]/a').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/form/div[1]/div[3]/div/div/div/div').click()
        time.sleep(3)
        result = []
        element = self.driver.find_elements_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li')
        for i in range(1, len(element)+1):
            result.append(self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[%i]' % i).text)
        self.assertEqual(name, result)

    # 验证编辑合同时可选择客户名称
    def test_02(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[3]/li/div').click()
        self.driver.implicitly_wait(20)
        target = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[3]/li/ul/div[1]')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        self.driver.implicitly_wait(20)
        self.driver.refresh()
        self.driver.implicitly_wait(20)
        cn = self.driver.find_element_by_xpath(
            '//*[@id="pane-3"]/div/div[3]/div[3]/table/tbody/tr[1]/td[4]/div/div[1]/a/span').text
        self.driver.find_element_by_xpath('//*[@id="pane-3"]/div/div[3]/div[3]/table/tbody/tr/td[3]/div/a').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[1]/div[3]/div/div/div/div/input').click()
        time.sleep(20)
        i = 1
        while i > 0:
            try:
                element = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[%i]' % i)
                expect = element.text
                if element.text != cn:
                    element.click()
                    break
                i += 1
            except:
                print("无副标题或无法选择")
                break
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[6]/div/button[1]').click()
        time.sleep(3)
        result = self.driver.find_element_by_class_name('el-notification__title').text
        self.assertEqual("成功", result)
        self.driver.back()
        self.driver.refresh()
        cn = self.driver.find_element_by_xpath(
            '//*[@id="pane-3"]/div/div[3]/div[3]/table/tbody/tr[1]/td[4]/div/div[1]/a/span').text
        self.assertEqual(expect, cn)


if __name__ == '__main__':
    crm_login.main()
