from App.init_driver.init_Driver import init_driver
import time

# 函数调用  将运行结果(手机驱动对象)返回给函数的调用者driver
driver = init_driver()

# swip滑动事件：显示 -> WLAN
driver.swipe(174,571,174,324,5000)

# scroll滑动事件(直到页面自动停止)：存储 -> WLAN
el1 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
el2 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
driver.scroll(el1,el2)
time.sleep(3)

# drag拖拽事件(替换位置)： 存储 -> WLAN
el3 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
el4 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
driver.drag_and_drop(el3,el4)
time.sleep(3)

# 应用置于后台事件(s)
driver.background_app(10)
time.sleep(2)

"""
    进入模拟器设置页面向上由“存储”滑动到“更多”，
    之后通过屏幕的宽度比例，模拟向下滑动动作，
    输出当前屏幕内“存储”的坐标
"""
# 定位存储和更多
cunchu = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
more = driver.find_element_by_xpath("//*[contains(@text,'更多')]")
driver.drag_and_drop(cunchu,more)

# 向下滑动
psize = driver.get_window_size()
x = psize['width']/2
y1 = psize['height'] * 0.8
y2 = psize.get('height') * 0.2      # 字典的get方法
driver.swipe(x,y2,x,y1,3000)

print(more.location)                             # {'x': 144, 'y': 450}

# 滑动屏幕
driver.close_app()
time.sleep(2)

phone_size = driver.get_window_size()
print(phone_size)                                # {'height': 1184, 'width': 768}
y = phone_size['height']/2
x1 = phone_size['width'] * 0.8
x2 = phone_size.get('width') * 0.2
driver.swipe(x1,y,x2,y,3000)

# 退出手机驱动对象
driver.quit()