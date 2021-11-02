import crm_login
import time
import phoneName


class CustomerNameTest(crm_login.TestClass):
    # 新建合同,客户名称可选择主标题或副标题
    def test_01(self):
        # 添加副标题
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/div').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/ul/div[3]/a').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div[3]/div[3]/table/tbody/tr/td[5]/div/div/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div[6]/div/div[2]/form/div[1]/div/button').click()
        self.driver.implicitly_wait(20)
        i = 1
        while i > 0:
            try:
                self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div[6]/div/div[2]/form/div[%i]/div/div/input'% i )
            except:
                break
            i += 1
        number = i-1
        cn = phoneName.company()
        self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div[6]/div/div[2]/form/div[%i]/div/div/input' % number).send_keys(cn)
        self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div[6]/div/div[3]/div/button[2]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[3]/li/div').click()
        target = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[3]/li/ul/div[1]/a')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        self.driver.refresh()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="pane-3"]/div/div[3]/div[3]/table/tbody/tr[1]/td[3]/div/a').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[1]/div[3]/div/div/div/div/input').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[%i]' % number)
        result.text
        print(result.text)
        print(number)
        self.assertEqual(cn, result.text)
        self.driver.back()
        self.driver.refresh()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/div').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/ul/div[3]/a').click()
        self.driver.implicitly_wait(20)
        button = self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div[3]/div[3]/table/tbody/tr/td[5]/div/div/button')
        self.driver.execute_script("arguments[0].click();", button)
        self.driver.implicitly_wait(20)
        button = self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div[6]/div/div[2]/form/div[%i]/div/button' % number)
        self.driver.execute_script("arguments[0].click();", button)
        self.driver.implicitly_wait(20)
        button =self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div[6]/div/div[3]/div/button[2]')
        self.driver.execute_script("arguments[0].click();", button)



