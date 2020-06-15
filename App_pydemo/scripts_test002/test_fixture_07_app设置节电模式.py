import pytest
from appium import webdriver
import os

from selenium.webdriver.support.wait import WebDriverWait


class Test_index:

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

    def wait_element(self, type, data):

        if type == "id":
            return WebDriverWait(self.driver, 5, 0.5)\
                .until(lambda x: x.find_element_by_id(data))
        if type == "xpath":
            return WebDriverWait(self.driver, 5, 0.5) \
                .until(lambda x: x.find_element_by_xpath(data))

    @pytest.fixture()
    def in_index(self):
        # 进入位置信息
        # 定位WLAN
        # wl = self.driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
        wl = self.driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")

        # 定位存储设备
        ccsb = self.driver.find_element_by_xpath("//*[contains(@text,'存储设备')]")

        # 向上滑动
        self.driver.drag_and_drop(ccsb, wl)

        # 定位位置信息并点击
        self.wait_element("xpath", "//*[contains(@text,'位置信息')]").click()

        # 函数引用
        @pytest.mark.usefixtures("in_index")  # ⚠⚠
        def test_change_mod(self):
            # 改变模式
            mod_id = self.wait_element("id", "android:id/summary")
            # 点击模式
            mod_id.click()
            # 点击节电
            self.wait_element("xpath", "//*[contains(@text,'节电')]").click()

            # 点击返回按钮
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            # 断言
            assert "节电" in mod_id.text, "失败了~~~"


if __name__ == '__main__':
    pytest.main(["-s", "test_fixture_07.py"])
