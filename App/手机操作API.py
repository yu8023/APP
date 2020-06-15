
from App.init_driver.init_Driver import init_driver
import time

# 函数调用  将运行结果(手机驱动对象)返回给函数的调用者driver
driver = init_driver()

# 1、获取当前手机的时间
print(driver.device_time)

# 2、获取手机的宽高(手机的分辨率)
print(type(driver.get_window_size()))  # <class 'dict'> ：字典类型
print(driver.get_window_size())      # {'height': 1184, 'width': 768}

# 向上滑动
phone_size = driver.get_window_size()
x = phone_size['width']/2      # x = phone_size.get('width')/2
y1 = phone_size['height'] * 0.8
y2 = phone_size.get('height') * 0.2
driver.swipe(x,y1,x,y2,3000)

# 3、发送键到设备：音量减小键
for i in range(2):            # 0 1
    driver.keyevent(25)
    time.sleep(0.5)

# 3、发送键到设备：home键
driver.keyevent(3)
time.sleep(2)

# 3、发送键到设备：菜单键
driver.keyevent(82)
time.sleep(2)

# 4、操作手机通知栏：打开通知栏
driver.open_notifications()
# 点击操作横幅
driver.find_element_by_id("com.android.systemui:id/header").click()
# 点击飞行模式
driver.find_element_by_xpath("//*[contains(@text,'飞行模式')]").click()
# 点击home键
driver.keyevent(3)

# 4、操作手机通知栏：点击腾讯新闻通知
driver.open_notifications()
time.sleep(3)
text_desc = driver.find_element_by_xpath("//*[contains(@text,'扫墓')]")
# 打印标题
print(text_desc.text)
# 通过通知栏进入app
text_desc.click()
print("进入成功")

# 5、获取手机当前网络模式：1-飞行模式 2-wifi 4-移动 6-移动+wifi
print(driver.network_connection)

# 6、设置手机网络,可能需要超级权限
driver.set_network_connection(1)
print("网络设置完成")
# print(driver.network_connection)

# 7、手机截图
# 打开设置
driver.get_screenshot_as_file("./screenshot_page/air1.png")


# 退出驱动对象
driver.quit()