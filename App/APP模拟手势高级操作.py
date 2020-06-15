from appium import webdriver
import os,time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

# server 启动参数
desired_caps = {}
# 系统
desired_caps['platformName'] = 'Android'
# 版本
desired_caps['platformVersion'] = '6.0'
# 设备号
os.system("adb devices")
desired_caps['deviceName'] = '192.168.140.101:5555' # os.system("adb devices")

os.system("adb shell dumpsys window windows | findstr mFocusedApp")
# 包名
desired_caps['appPackage'] = 'com.android.settings'
# 启动名
desired_caps['appActivity'] = '.Settings'

# unicode设置(允许中文输入)
desired_caps['unicodeKeyboard'] = True
# 键盘设置(允许中文输入)
desired_caps['resetKeyboard'] = True

# 声明手机驱动对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)   # 127.0.0.1:4723


# # 通过tap方法点击WLAN
el_wlan = driver.find_element_by_xpath("//*[contains(@text,'WLA')]")
# # 1、通过元素
# TouchAction(driver).tap(el_wlan).perform()
# print(el_wlan.location)
# # 2、通过坐标  字典的get方法
# TouchAction(driver).tap(x=el_wlan.location.get('x'),y=el_wlan.location.get('y')).perform()


# 1、press通过元素方式点击WLAN
# TouchAction(driver).press(el_wlan).release().perform()

# 2、press通过坐标方式点击WLAN
# TouchAction(driver).press(x=el_wlan.location.get('x'),y=el_wlan.location.get('y'))\
#     .release().perform()

# # wait等待操作
# # 进入WLAN
# el_wlan.click()
# # 定位WiredSSID
# el_WiredSSID = driver.find_element_by_id("android:id/title")
# # 1、通过元素定位方式长按元素
# # TouchAction(driver).press(el_WiredSSID).wait(5000).perform()
# # 2、通过坐标方式模拟长按元素
# TouchAction(driver).press(x=el_WiredSSID.location.get('x'),y=el_WiredSSID.location.get('y'))\
#     .wait(3000).perform()

# # long_press长按操作,进入WLAN，长按WiredSSID
# # 进入WLAN
# el_wlan.click()
# # 定位WiredSSID
# el_WiredSSID = driver.find_element_by_id("android:id/title")
# # 1、通过元素长按WiredSSID
# # TouchAction(driver).long_press(el=el_WiredSSID,duration=3000).release().perform()
# # 2、通过坐标长按WiredSSID
# TouchAction(driver).long_press(x=604,y=339,duration=3000).perform()


el_yy = driver.find_element_by_xpath("//*[contains(@text,'应用')]")
# 手指滑动操作------> 使用press或者long_press,必须要用release放手，否则会报错或者无效果
# 1、通过元素方式滑动
# TouchAction(driver).press(el_cc).wait(1000).move_to(el_wlan).release().perform()      # 不加wait，滑动到页面底部，加wait正常
# TouchAction(driver).long_press(el_cc,duration=1000).move_to(el_wlan).release().perform()    # 正常

# 2、通过坐标方式滑动
# 注意： press连接一个move_to，实际调用的是swipe方法，可在log中查询，不要给相对坐标
# TouchAction(driver).press(x=227,y=1010).wait(1000).move_to(x=227,y=700).release().perform()     # 不加wait，滑动到页面底部，加wait正常
# 注意： long_press连接一个move_to，实际调用的是drag方法，可在log中查询，不要给相对坐标
# TouchAction(driver).long_press(x=227,y=1010,duration=1000).move_to(x=227,y=700).release().perform()    # 正常


def wait_element(xpa):

    el_xx = WebDriverWait(driver,5,0.5).until(lambda x: x.find_element_by_xpath(xpa))
    return el_xx

"""
    业务场景2：
    1.进入设置，向上滑动屏幕到可见"安全"选项  2.进入到安全  
    3.点击屏幕锁定方式  4.点击图案  5.绘制图案
"""
# 1、进入设置页面，向上滑动屏幕到可见"安全"选项
el_cc = wait_element("//*[contains(@text,'存储')]")
driver.drag_and_drop(el_cc,el_wlan)     # 从存储到wlan
# 2、点击安全按钮
el_aq = wait_element("//*[contains(@text,'安全')]").click()
# 3、点击屏幕锁定方式按钮
wait_element("//*[contains(@text,'屏幕锁定')]").click()
# 4、点击图案按钮
wait_element("//*[contains(@text,'图案')]").click()
time.sleep(2)
# 5、绘制图案四个坐标 1:(384,662) 2:(384,405) 3:(127,405) 4:(127,662) 5:(384,918)
# for i in range(2):     # 0 1
TouchAction(driver).press(x=384,y=662).wait(100).move_to(x=0,y=-257).wait(100)\
    .move_to(x=-257,y=0).wait(100).move_to(x=0,y=257).wait(100).move_to(x=257,y=256)\
    .release().perform()
# driver.find_element_by_id("com.android.settings:id/footerRightButton").click()
time.sleep(2)

# 截图
driver.get_screenshot_as_file('./screenshot_page/tuan.png')

time.sleep(5)
# 退出手机驱动对象
driver.quit()
