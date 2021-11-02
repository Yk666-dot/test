import crm_login
import time


class ReturnCountTest(crm_login.TestClass):
    # 校验回款金额
    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[3]/li/div').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[3]/li/ul/div[9]/a').click()
        i = 0
        row = 1
        page = 1
        while page > 0:
            while row > 0:
                try:
                    self.driver.implicitly_wait(20)
                    amount = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[%i]/td[9]' % row).text
                    i = int(amount) + i
                    row += 1
                except:
                    break
            self.driver.implicitly_wait(20)
            try:
                target = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div[2]/div/div/button[2]')
                self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 滚动条拖动到可见的元素去
                target.click()
            except:
                break
        print(i)
        target = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div[1]')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        expect = target.text[4:]
        self.assertEqual(expect, i)


if __name__ == '__main__':
    crm_login.main()