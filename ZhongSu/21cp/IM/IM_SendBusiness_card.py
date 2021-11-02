import paramunittest
import time
import ready_login


class SendBusinessTest(ready_login.TestClass):

    # 发送名片
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
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/ul/li[6]').click()
        self.driver.implicitly_wait(20)
        expect = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div[1]/table/tr[1]/td[3]').text
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div[1]/table/tr[1]/td[1]/label').click()
        self.driver.find_element_by_class_name('active').click()
        result = self.driver.find_element_by_xpath('//*[@id="chatlist"]/li/div/div/div/div/div[1]/p').text
        self.assertEqual(expect, result)

    # 点击名片进行洽谈
    def test_02(self):
        expect = self.driver.find_element_by_class_name('cardname').text
        self.driver.find_element_by_xpath('//*[@id="chatlist"]/li/div/div/div').click()
        time.sleep(3)
        result = self.driver.find_element_by_class_name('h1dname').text
        self.assertEqual(expect, result)

