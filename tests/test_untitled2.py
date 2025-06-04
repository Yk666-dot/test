# -*- encoding=utf8 -*-
__author__ = "msi"

import pytest
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import random
import sys
sys.stdout.isatty = lambda: True

# 全局设置图片可信度大于等于0.8 才能识别成功,未设置时默认0.7
ST.THRESHOLD = 0.8
# 每步操作等待1秒
ST.OPDELAY = 1
# 设置全局等待超时时长
ST.FIND_TIMEOUT = 60

@pytest.fixture(scope="module")
def init_app():
    auto_setup(__file__)
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    yield poco
    # 可以在这里添加清理代码，比如停止应用等
    

# 判断当前页面是否发布页面，账号是否对上，账号不对则重新登录再发布
def check_and_login(poco):
    if not exists(Template(r"tpl1722823868406.png", threshold=0.9, record_pos=(-0.147, -0.767), resolution=(1080, 2400))):
        stop_app("com.zhongsu.online")
        start_app("com.zhongsu.online")
        touch(Template(r"tpl1722824496321.png", record_pos=(0.4, 1.02), resolution=(1080, 2400)))
        if  not exists(Template(r"tpl1722825326209.png", threshold=0.9, record_pos=(-0.16, -0.771), resolution=(1080, 2400))):
            touch(Template(r"tpl1722824574405.png", record_pos=(0.429, -0.955), resolution=(1080, 2400)))
            if exists(Template(r"tpl1727059146951.png", record_pos=(-0.253, 0.557), resolution=(1080, 2400))):

                swipe(Template(r"tpl1722824614948.png", record_pos=(-0.255, 0.567), resolution=(1080, 2400)), vector=[0.0278, -0.317])
                touch(Template(r"tpl1722824631265.png", record_pos=(-0.368, 1.046), resolution=(1080, 2400)))
                touch(Template(r"tpl1722824637736.png", record_pos=(0.199, 0.193), resolution=(1080, 2400)))

                touch(Template(r"tpl1722824648382.png", record_pos=(0.375, 0.856), resolution=(1080, 2400)))
            if exists(Template(r"tpl1722825117625.png", threshold=0.9, record_pos=(-0.003, 0.89), resolution=(1080, 2400))):
                touch(Template(r"tpl1722825183449.png", record_pos=(0.014, 0.91), resolution=(1080, 2400)))

            touch(Template(r"tpl1722824836754.png", record_pos=(-0.368, -0.318), resolution=(1080, 2400)))
            if exists(Template(r"tpl1722824904375.png", threshold=0.9, record_pos=(0.349, -0.343), resolution=(1080, 2400))):
                touch(Template(r"tpl1722824844371.png", record_pos=(0.352, -0.339), resolution=(1080, 2400)))
            text("kaiyu12")
            touch(Template(r"tpl1722824859616.png", record_pos=(-0.355, -0.157), resolution=(1080, 2400)))
            text("123456")
            touch(Template(r"tpl1722825275449.png", record_pos=(-0.002, 0.105), resolution=(1080, 2400)))
            touch(Template(r"tpl1722825282831.png", record_pos=(0.176, 0.193), resolution=(1080, 2400)))
            touch(Template(r"tpl1722825293730.png", record_pos=(0.397, 1.012), resolution=(1080, 2400)))
def publish_flow(poco):
    check_and_login(poco)
    print(11111)
    try:
        touch(Template(r"tpl1721722414239.png", record_pos=(0.365, 0.03), resolution=(1080, 2400)))
        touch(Template(r"tpl1721722508438.png", record_pos=(-0.001, -0.681), resolution=(1080, 2400)))
        items = poco("com.zhongsu.online:id/select_msg_tv")[1]
        print(items.get_text())
        touch(Template(r"tpl1721724437609.png", record_pos=(-0.229, -0.8), resolution=(1080, 2400)))
        text(items.get_text())
        poco("com.zhongsu.online:id/grid_category_label").child().click()
        touch(Template(r"tpl1721787501818.png", record_pos=(0.002, 0.9), resolution=(1080, 2400)))
        touch(Template(r"tpl1721787882694.png", record_pos=(-0.027, -0.542), resolution=(1080, 2400)))
        text("测试助剂")
        touch(Template(r"tpl1721787925402.png", record_pos=(0.004, -0.404), resolution=(1080, 2400)))
        text("测试")
        touch(Template(r"tpl1721787992822.png", record_pos=(-0.031, -0.014), resolution=(1080, 2400)))
        items = poco("com.zhongsu.online:id/recy_view").child()
        items[random.randint(0, len(items)-1)].child("com.zhongsu.online:id/chk_select").click()
        touch(Template(r"tpl1721788251043.png", record_pos=(0.006, 0.944), resolution=(1080, 2400)))
        touch(Template(r"tpl1721788829033.png", record_pos=(-0.032, -0.676), resolution=(1080, 2400)))
        text("测试助剂")
        touch(Template(r"tpl1721788851077.png", record_pos=(-0.059, -0.408), resolution=(1080, 2400)))
        text("100")
        touch(Template(r"tpl1721788863446.png", record_pos=(-0.056, -0.144), resolution=(1080, 2400)))
        text("10000")
        touch(Template(r"tpl1721788875929.png", record_pos=(-0.313, 0.331), resolution=(1080, 2400)))
        if exists(Template(r"tpl1721788905546.png", record_pos=(0.199, 0.981), resolution=(1080, 2400))):

            touch(Template(r"tpl1721788929273.png", record_pos=(0.214, 0.99), resolution=(1080, 2400)))
        touch(Template(r"tpl1721788942534.png", record_pos=(-0.049, -0.826), resolution=(1080, 2400)))

        touch(Template(r"tpl1721788952276.png", record_pos=(0.387, -0.956), resolution=(1080, 2400)))
        touch(Template(r"tpl1721788960377.png", record_pos=(0.431, -0.931), resolution=(1080, 2400)))
        sleep(3.0)
        touch(Template(r"tpl1721788985318.png", record_pos=(-0.017, 0.864), resolution=(1080, 2400)))
        if exists(Template(r"tpl1724746775154.png", record_pos=(0.005, -0.223), resolution=(1080, 2400))):
            touch(Template(r"tpl1724746764945.png", record_pos=(-0.192, 0.289), resolution=(1080, 2400)))
        # 判断有没有开启日历的提示框干扰
        if poco("com.zhongsu.online:id/last_approve_tv").exists():
            poco("com.zhongsu.online:id/last_approve_tv").click()
            poco("com.zhongsu.online:id/last_approve_tv").click()


        assert_exists(Template(r"tpl1721789050257.png", threshold=0.9, record_pos=(-0.363, -0.536), resolution=(1080, 2400)), "断言新建商品与截图一致")

        # 验证下架商品

        sleep(3.0)
        poco("com.zhongsu.online:id/tv_standupdown").click()
        sleep(3.0)
        if poco("com.zhongsu.online:id/check_box").exists():
            i = 0
            while i <= len(poco("com.zhongsu.online:id/check_box"))-1:
                poco("com.zhongsu.online:id/check_box")[i].click()
                i+=1
        poco("com.zhongsu.online:id/tv_standdown").click()
        status = poco("com.zhongsu.online:id/btn_tag")[0].get_text()
        assert status == "已下架" , "状态显示不是已下架，是%s" % status

        # 验证上架商品
        poco("com.zhongsu.online:id/tv_standupdown").click()
        sleep(3.0)
        if poco("com.zhongsu.online:id/check_box").exists():
            i = 0
            while i <= len(poco("com.zhongsu.online:id/check_box"))-1:
                poco("com.zhongsu.online:id/check_box")[i].click()
                i+=1
        poco("com.zhongsu.online:id/tv_standup").click()
        status = poco("com.zhongsu.online:id/btn_tag")[0].get_text()
        assert status == "上架中" , "状态显示不是上架中，是%s" % status

        # 最后删除商品
        touch(Template(r"tpl1721789202732.png", record_pos=(0.373, -0.164), resolution=(1080, 2400)))
        touch(Template(r"tpl1721789208645.png", record_pos=(0.197, 0.182), resolution=(1080, 2400)))

        # 验证上下架商品
        touch(Template(r"tpl1722234202777.png", record_pos=(-0.427, -0.959), resolution=(1080, 2400)))  
    finally:
        i = 1
        while i <= 30:
            if exists(Template(r"tpl1722308116816.png", threshold=0.9, record_pos=(-0.003, -0.95), resolution=(1080, 2400))):
                break
            else:
                touch(Template(r"tpl1722321160633.png", record_pos=(-0.427, -0.954), resolution=(1080, 2400)))
                if i == 30:
                    print("返回企业中心失败")
            i += 1
@pytest.mark.usefixtures("init_app")
def test_publish_flow(init_app):
    publish_flow(init_app)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
