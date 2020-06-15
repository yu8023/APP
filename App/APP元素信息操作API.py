from App.init_driver.init_Driver import init_driver
import time

# 函数调用  将运行结果(手机驱动对象)返回给函数的调用者driver
driver = init_driver()

try:
    # 1、打开设置点击搜索按钮
    driver.find_element_by_id("com.android.settings:id/search").click()

    for i in ("中文","vpn","wi","ls"):
        # 定位搜索框
        input_text = driver.find_element_by_id("android:id/search_src_text")
        # 3、清空输入框--业务：搜索框多次输入内容 有下拉提示认为成功
        input_text.clear()
        # 2、输入内容
        input_text.send_keys(i)
        time.sleep(2)
        # 判断有下拉提示
        # 4、获取元素的文本内容：text
        xiala_data = driver.find_element_by_id("com.android.settings:id/title").text
        print(xiala_data)
        if xiala_data:
            print(True)
        else:
            print(False)

    # 点击返回按钮
    driver.find_element_by_class_name("android.widget.ImageButton").click()
    time.sleep(5)

    # 获取元素的属性值
    # 5、获取元素的属性值： get_attribute(value)
    desc = driver.find_element_by_id("com.android.settings:id/search").get_attribute("name")
    print(desc)             # 搜索设置
    text = driver.find_element_by_xpath("//*[contains(@text,'WLA')]").get_attribute("text")
    print(text)             # WLAN
    cname = driver.find_element_by_xpath("//*[contains(@text,'存储设备')]").get_attribute("className")
    print(cname)            # android.widget.TextView
    res = driver.find_element_by_xpath("//*[contains(@text,'提示音和通知')]").get_attribute("resourceId")
    print(res)              # com.android.settings:id/title

    # 6、获取元素的坐标
    loc = driver.find_element_by_id("com.android.settings:id/search").location
    print(loc)          # {'x': 672, 'y': 56}

    # 7、获取app包名和启动名
    print("包名",driver.current_package)
    print("启动名",driver.current_activity)

except Exception as e:
    print(e)
finally:
    driver.quit()

