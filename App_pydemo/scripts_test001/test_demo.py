# 引入pytest包
import pytest
from appium import webdriver
import os
from selenium.webdriver.support.wait import WebDriverWait

class Test_ST(object):

    # 函数级别 setup()／teardown() 运行一次测试函数会运行一次setup和teardown
    # def setup(self):
    #     print("start...")
    #
    # def teardown(self):
    #     print("end...")

    """
    类级别 setup_class() / teardown_class()
    在一个测试内只运行一次setup_class和teardown_class，不关心测试类内有多少个测试函数
    """
    def setup_class(self):
        # server 启动参数
        desired_caps = {}
        # 系统
        desired_caps['platformName'] = 'Android'
        # 版本
        desired_caps['platformVersion'] = '6.0'
        # 设备号
        os.system("adb devices")
        desired_caps['deviceName'] = '192.168.140.101:5555'
        # 包名
        desired_caps['appPackage'] = 'com.android.settings'    # 设置
        # 启动名
        desired_caps['appActivity'] = '.Settings'              # 设置
        # unicode设置(允许中文输入)
        desired_caps['unicodeKeyboard'] = True
        # 键盘设置(允许中文输入)
        desired_caps['resetKeyboard'] = True

        # 声明手机驱动对象
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown_class(self):
        # 关闭驱动对象，同时关闭所有关联的app
        self.driver.quit()

    def wait_ele(self,xpa):
        # ctrl+alt+空格
        return WebDriverWait(self.driver,5,0.5).until(lambda x: x.find_element_by_xpath(xpa))

    # 函数定义：test开头的测试函数
    @pytest.mark.run(order=1)    # 因为先进入更多
    def test_vpn(self):
        # 点击更多      不加self, 可能会执行类外的同名函数
        self.wait_ele("//*[contains(@text,'更多')]").click()
        # 获取所有描述信息
        text_list = self.driver.find_elements_by_id("android:id/title")

        # 创建一个空列表：text_value，将获取到的值添加append()进入列表中，
        text_value = []              # ['漫游时连接到移动数据网络服务', '3G', '选择网络运营商']
        for i in text_list:
            text_value.append(i.text)

        assert "VPN" in text_value, "他不在～"

    @pytest.mark.run(order=2)       # 在更多页面点击移动网络
    def test_2G(self):
        # 点击移动网络
        self.wait_ele("//*[contains(@text,'移动')]").click()
        # 首选网络类型
        self.wait_ele("//*[contains(@text,'首选网络')]").click()
        # 弹窗点击3G
        self.wait_ele("//*[contains(@text,'3G')]").click()
        # 获取所有描述信息
        sum_list = self.driver.find_elements_by_id("android:id/summary")
        sum_list_value = []              # ['漫游时连接到移动数据网络服务', '3G', '选择网络运营商']
        for i in sum_list:
            sum_list_value.append(i.text)

        assert "3G" in sum_list_value, "成功了～"

if __name__ == '__main__':
    pytest.main(["-s","test_demo.py"])      # 传参需要是一个元组()或者列表[]