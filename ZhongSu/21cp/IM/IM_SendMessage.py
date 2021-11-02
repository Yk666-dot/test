import paramunittest
import time
import ready_login

message = "字数"
while len(message) <= 202:
    message = message + "字数"


@paramunittest.parametrized(
    {"msg": "飒飒何时能刚！@sad111", "msg1": message, "tip": "上传文件不能超过5MB！",
     "route": "C:/Users/msi/Pictures/9.jpg", "route1": "C:/Users/msi/Pictures/14.jpg",
     "route2": "C:/Users/msi/Documents/中心主题1_20210414_133137.xls",
     "route3": "C:/Users/msi/Documents/WXWork/1688850884710679/Cache/Video/2021-08/video(9).MP4"},

)
class SendmessageTest(ready_login.TestClass):

    def setParameters(self, msg, msg1, tip, route, route1, route2, route3):
        self.msg = msg
        self.msg1 = msg1
        self.tip = tip
        self.route = route
        self.route1 = route1
        self.route2 = route2
        self.route3 = route3

    # 发送消息
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
        self.driver.find_element_by_xpath('//*[@id="textarea"]').send_keys(self.msg)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/button').click()
        self.driver.find_element_by_xpath('//*[@id="textarea"]').send_keys(self.msg1)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/button').click()
        result = self.driver.find_element_by_class_name('chatContent').text
        self.assertIn(self.msg, result)
        self.assertIn(self.msg1, result)

    # 使用常用语句
    def test_02(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/ul/li[1]').click()
        self.driver.implicitly_wait(20)
        xpath = '//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/ul/li[1]/div/div/ul/li[1]'
        expect = self.driver.find_element_by_xpath(xpath).text
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/button').click()
        result = self.driver.find_element_by_class_name('chatContent').text
        self.assertIn(expect, result)

    # 发送文件
    def test_03(self):
        self.driver.find_element_by_class_name('sfile').send_keys(self.route)
        time.sleep(3)
        img = self.driver.find_element_by_xpath('//*[@id="chatlist"]/li[4]/div/div/div/a/img')
        self.assertEqual('img', img.tag_name)
        # 上传不支持的大于20m
        self.driver.find_element_by_class_name('sfile').send_keys(self.route1)
        self.driver.implicitly_wait(20)
        tip = self.driver.find_element_by_class_name('toast').text
        self.assertEqual("上传文件不能超过20MB！", tip)
        # 上传xls
        time.sleep(2)
        self.driver.find_element_by_class_name('sfile').send_keys(self.route2)
        self.driver.implicitly_wait(20)
        file = self.driver.find_element_by_xpath('//*[@id="chatlist"]/li[5]/div/div/div/div/a/div[1]/p[1]').text
        self.assertEqual("中心主题1_20210414_133137.xls", file)
        # 上传不支持的视频文件
        time.sleep(2)
        self.driver.find_element_by_class_name('sfile').send_keys(self.route3)
        self.driver.implicitly_wait(20)
        tip = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/p').text
        self.assertEqual("文件格式不正确！", tip)

    # 发送开票信息
    def test_04(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/ul/li[7]').click()
        self.driver.implicitly_wait(20)
        info = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/ul').text
        self.driver.find_element_by_class_name('sendBtn').click()
        self.driver.implicitly_wait(20)
        expect = self.driver.find_element_by_xpath('//*[@id="chatlist"]/li[6]/div/div/div/div/div[1]').text
        self.assertEqual(expect, info)


