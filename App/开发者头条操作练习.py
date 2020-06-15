from App.init_driver.init_Driver import init_driver
from selenium.webdriver.support.wait import WebDriverWait
import time

"""
    启动开发者头条app，通过显示等待方式点击“我的”按钮，
    之后将应用置于后台10秒，通过显示等待方式点击阅读，
    截取手机屏幕图片保存到当前目录
"""

driver = init_driver()

# 点击“我的”按钮
my = WebDriverWait(driver,timeout=15,poll_frequency=1)\
    .until(lambda x: x.find_element_by_xpath("//*[contains(@text,'我的')]"))
my.click()
time.sleep(2)

# 将应用置于后台10秒
driver.background_app(10)

# 通过显示等待方式点击阅读
rd = WebDriverWait(driver,timeout=15,poll_frequency=1)\
    .until(lambda x: x.find_element_by_xpath("//*[contains(@text,'阅读')]"))
rd.click()

# 截取手机屏幕图片保存到当前目录
driver.get_screenshot_as_file("./screenshot_page/read.png")
time.sleep(2)

"""
    启动开发者头条，打开通知栏，在通知栏内点击飞行模式，
    之后关闭通知栏，关闭开发者头条app，打开设置页面，降低手机音量到最低，
    更改手机网络模式为移动流量，截取手机屏幕保存到当前目录
"""
# 打开通知栏
driver.open_notifications()
time.sleep(2)

# 点击操作横幅
driver.find_element_by_id("com.android.systemui:id/header").click()
# 点击飞行模式
driver.find_element_by_xpath("//*[contains(@text,'飞行模式')]").click()
# 点击home键
driver.keyevent(3)

# 关闭开发者头条app
driver.close_app()
print("成功关闭app")

# 打开设置页面
driver.start_activity('com.android.settings','.Settings')

# 降低手机音量到最低
for i in range(9):
    driver.keyevent(25)
    time.sleep(0.5)

# 更改手机网络模式为移动流量：1-飞行模式 2-wifi 4-移动 6-移动+wifi
driver.set_network_connection(4)
print(driver.network_connection)               # 4
time.sleep(2)

# 截取手机屏幕保存到当前目录
driver.get_screenshot_as_file("./screenshot_page/net.png")
print("截图成功")


driver.quit()


