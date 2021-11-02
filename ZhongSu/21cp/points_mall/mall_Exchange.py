import time
import ready_login
import paramunittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

rulers = '''1.兑换成功后将从会员账户中扣除相应的中塑币。
2.礼品一旦兑换，若无质量问题，不予办理礼品退换货。
3.对符合国家质量三包规定的礼品，客户可在签收礼品后5个工作日内，申请办理礼品退/换货，客服电话：0574-62534692。
4.积分商城兑换的礼品均不提供发票。
5.配送运费由中塑在线支付。'''


class ExchangeTest(ready_login.TestClass):
    # 验证点击商品进入详情页
    def test_01(self):
        global coin
        move = self.driver.find_element_by_id("kcAccountName")
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="kcLogin"]/ul/li[1]/a').click()
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == '用户概况-中塑在线':
                break
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/a[6]').click()
        stock = self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/span').text
        coin = "".join(list(filter(str.isdigit, stock)))
        title = self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/div[1]/div[2]')
        commodity = title.get_attribute('title')
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/div[1]/div[1]/a/img').click()
        title = self.driver.find_element_by_class_name('pro_name').text
        self.assertEqual(commodity, title)


    # 测试商品兑换成功
    def test_02(self):
        # 手机验证码错误
        stock = self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[1]/div[2]/ul/li[2]/em').text
          # 只保留字符串中的数字
        stock_num = "".join(list(filter(str.isdigit, stock)))
        price = self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[1]/div[2]/ul/li[1]/strong').text
        self.driver.find_element_by_class_name('layui-border-blue').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('getCode').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('phoneCode').send_keys('66666')
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('layui-layer-padding').text
        self.assertEqual("手机验证码错误", self.driver.find_element_by_class_name('layui-layer-padding').text)
        # 兑换成功
        time.sleep(10)
        self.driver.find_element_by_name('phoneCode').clear()
        self.driver.find_element_by_name('phoneCode').send_keys('666666')
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('layui-layer-padding').text
        self.assertEqual("提交成功!", self.driver.find_element_by_class_name('layui-layer-padding').text)
        time.sleep(5)
        stock = self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[1]/div[2]/ul/li[2]/em').text
        result = "".join(list(filter(str.isdigit, stock)))
        # 兑换成功后库存减1
        self.assertEqual(int(stock_num)-1, int(result))
        self.driver.back()
        # 中塑币减少
        stock = self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/span').text
        result = "".join(list(filter(str.isdigit, stock)))
        self.assertEqual(int(coin) - int(price), int(result))

    # 测试库存0兑换失败
    def test_03(self):
        self.driver.implicitly_wait(20)
        i = 1
        while i <= 12:
            text = self.driver.find_element_by_xpath(
                '/html/body/div/div[3]/div[2]/div[3]/div[2]/div[%i]/div[3]/span[2]' % i).text
            if text == "库存：0件":
                self.driver.find_element_by_xpath(
                    '/html/body/div/div[3]/div[2]/div[3]/div[2]/div[%i]/div[1]/a/img' % i).click()
                self.driver.implicitly_wait(20)
                result = self.driver.find_element_by_class_name('layui-btn-disabled').text
                self.assertEqual(result, "已兑完")
                break
            elif i == 12:
                print("没有库存0的商品，需创建测试数据")
            i = i + 1
        self.driver.back()

    # 测试中塑币不足兑换失败
    def test_04(self):
        self.driver.implicitly_wait(20)
        i = 1
        while i <= 12:
            text = self.driver.find_element_by_xpath(
                '/html/body/div/div[3]/div[2]/div[3]/div[2]/div[%i]/div[3]/span[1]' % i).text
            amount = text[:text.index("中塑币")]
            if int(amount) > 90000:
                target = self.driver.find_element_by_xpath(
                    '/html/body/div/div[3]/div[2]/div[3]/div[2]/div[%i]/div[1]/a/img' % i)
                target.click()
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_class_name('exchange').click()
                time.sleep(3)
                result = self.driver.find_element_by_class_name('layui-layer-padding').text
                self.assertEqual(result, "很遗憾！中塑币不足")
                break
            elif i == 12:
                print("当前中塑币数量足够，需添加巨额商品")
            i = i + 1
        self.driver.back()

    # 校对规则说明
    def test_05(self):
        self.driver.implicitly_wait(20)
        button = self.driver.find_element_by_class_name('rules')
        self.driver.execute_script("$(arguments[0]).click()", button)
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
        self.assertEqual(rulers, result)



if __name__ == '__main__':
        ready_login.main()


