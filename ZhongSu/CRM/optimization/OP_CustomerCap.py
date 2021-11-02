import crm_login
import phoneName
import re


class CustomerNameTest(crm_login.TestClass):
    # 客户上限设置
    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[4]/li/div').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[4]/li/ul/div[1]/a/li').click()
        self.driver.implicitly_wait(20)






if __name__ == '__main__':
    crm_login.main()