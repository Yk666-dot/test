import paramunittest
import time
import ready_login


class SendCommodityTest(ready_login.TestClass):

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
        # 发送原料
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/ul/li[4]').click()
        self.driver.implicitly_wait(20)
        expect = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[3]/div[1]/table/tr[1]/td[2]').text
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div/div[3]/div[1]/table/tr[1]/td[1]/label').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[3]/div[3]/button[2]').click()
        time.sleep(2)
        result = self.driver.find_element_by_xpath('//*[@id="chatlist"]/li/div/div/div/a/div').text
        self.assertIn(expect, result)

    def test_02(self):
        # 发送废塑料
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/ul/li[4]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/ul/li[5]').click()
        self.driver.implicitly_wait(20)
        expect = self.driver.find_element_by_class_name('titwh').text
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[3]/div[1]/table/tr/td[1]/label').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[3]/div[3]/button[2]').click()
        result = self.driver.find_element_by_xpath('//*[@id="chatlist"]/li/div/div/div/a/div').text
        self.assertIn(expect, result)

    # 点击进入商品详情
    def test_03(self):
        time.sleep(3)
        expect = self.driver.find_element_by_xpath('//*[@id="chatlist"]/li[2]/div/div/div/a/div/div[1]/p').text
        self.driver.find_element_by_xpath('//*[@id="chatlist"]/li[2]/div/div/div/a/div').click()
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        result = self.driver.title
        self.assertIn(expect, result)
        for window in handles:
            self.driver.switch_to.window(window)
            if self.driver.title == "中塑联机洽谈":
                break

    # 发送可供
    def test_04(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/ul/li[5]').click()
        self.driver.implicitly_wait(20)
        expect = self.driver.find_element_by_xpath(
                                            '//*[@id="app"]/div[1]/div[1]/div/div[3]/div[1]/table/tr[1]/td[2]').text
        self.driver.find_element_by_xpath(
                            '//*[@id="app"]/div[1]/div[1]/div/div[3]/div[1]/table/tr[1]/td[1]/label').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[3]/div[3]/button[2]').click()
        result = self.driver.find_element_by_xpath('//*[@id="chatlist"]/li[3]/div/div/div/a/div').text
        self.assertIn(expect, result)

    # 点击可供进入企业产品
    def test_05(self):
        self.driver.find_element_by_xpath('//*[@id="chatlist"]/li[3]/div/div/div/a/div').click()
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        result = self.driver.title
        self.assertIn("企业产品", result)
