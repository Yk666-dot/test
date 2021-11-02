import paramunittest
import time
import ready_login
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class ChatHistoryTest(ready_login.TestClass):

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
        time.sleep(4)
        # 校验搜索为空
        Action = ActionChains(self.driver)
        Action.move_by_offset(0, 0).perform()
        Action.move_by_offset(1460, 788).click().perform()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div/input').send_keys("！@#￥%%%%")
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div/input').send_keys(Keys.ENTER)
        time.sleep(3)
        result = self.driver.find_element_by_class_name('chatHistoryList').text
        self.assertEqual('暂无相关聊天记录', result)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div/input').clear()

    def test_02(self):
        # 正常搜索
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div/input').send_keys("字数")
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div/input').send_keys(Keys.ENTER)
        self.driver.implicitly_wait(20)
        results = self.driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/ul/li')
        for i in range(1, len(results)):
            result = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/ul/li[%i]/p' % i)
            self.driver.execute_script("arguments[0].scrollIntoView();", result)
            self.assertIn("字数", result.text)


