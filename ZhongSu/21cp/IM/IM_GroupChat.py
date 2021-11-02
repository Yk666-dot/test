import paramunittest
import time
import ready_login
from selenium.webdriver.common.action_chains import ActionChains

@paramunittest.parametrized(
    {"people_number": 2,
     "name": "！@123测试",
     "name01": "测试测试测试测试测试测试测试测试测试测试测试测试测试"},

)
class GroupChatTest(ready_login.TestClass):
    def setParameters(self, people_number, name, name01):
        self.people_number = people_number
        self.name = name
        self.name01 = name01

    def test_01(self):
        global member01, member02, member03
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
        time.sleep(2)
        member01 = self.driver.find_element_by_class_name('h1dname').text
        member02 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[2]/h3').text
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/ul/li[3]').click()
        self.driver.implicitly_wait(20)
        num = self.driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[1]/table/tr')
        # 子账号数量校验
        self.assertEqual(len(num), self.people_number)
        member03 = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div[1]/table/tr[1]/td[3]').text

    def test_02(self):
        # 创建群聊
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div/div[2]/div[1]/table/tr[1]/td[1]/label').click()
        self.driver.find_element_by_class_name("active").click()
        members = member01 + '、' + member02 + '、' + member03
        time.sleep(3)
        result = self.driver.find_element_by_class_name('h1dname').text
        self.assertEqual(members, result)

    def test_03(self):
        # 重复邀请
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/ul/li[3]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name("active").click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/p').text
        self.assertEqual("请邀请新用户加入", result)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[3]/button[1]').click()

    def test_04(self):
        # 修改群聊名称超过12字
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div[2]/div/div').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/input').send_keys(self.name01)
        self.driver.find_element_by_class_name('active').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/p').text
        self.assertEqual('最多只能输入16个字符', result)

    def test_05(self):
        # 群聊名称修改成功
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/input').send_keys(self.name)
        self.driver.find_element_by_class_name('active').click()
        time.sleep(2)
        result = self.driver.find_element_by_class_name('userList').text
        self.assertIn(self.name, result)

    def test_06(self):
        # 设置置顶
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div[4]/div/p/label').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/div[1]/h3').text
        self.assertEqual(self.name, result)

    def test_07(self):
        # 取消置顶
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div[4]/div/p/label').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/div[1]/h3').text
        self.assertNotEqual(self.name, result)

    def test_08(self):
        # 解散本群
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div[4]/div/div/button[2]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('active').click()
        time.sleep(2)
        result = self.driver.find_element_by_class_name('userList').text
        self.assertNotIn(self.name, result)




