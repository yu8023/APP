from App.init_driver.init_Driver import init_driver
import time
from selenium.webdriver.support.wait import WebDriverWait

# 函数调用  将运行结果(手机驱动对象)返回给函数的调用者driver
driver = init_driver()

try:
    # 定位一个元素
    # # 1、id 点击搜索按钮
    # driver.find_element_by_id("com.android.settings:id/search").click()
    # time.sleep(2)
    # # 2、点击搜索返回按钮
    # driver.find_element_by_class_name("android.widget.ImageButton").click()
    # time.sleep(2)
    # # 3、点击设置页显示
    # driver.find_element_by_xpath("//*[contains(@text,'示')]").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[contains(@class,'android.widget.ImageButton')]").click()
    # time.sleep(2)

    # 定位一组元素
    # 4.1、定位一组元素：id
    # ele_list = driver.find_elements_by_id("com.android.settings:id/title")
    # print(type(ele_list))           # <class 'list'>
    # print(ele_list)

    # 4.2、定位一组元素：class
    # ele_class_list = driver.find_elements_by_class_name("android.widget.TextView")

    # 4.3、定位一组元素：xpath
    # ele_xpath_list = driver.find_elements_by_xpath("//*[contains(@class,'widget.TextView')]")
    #
    # for i in ele_xpath_list:
    #     print(i.text)     # print(i.get_attribute("text"))
    #     if '应用' in i.get_attribute("text"):    # 模糊匹配
    #         i.click()
    #         # 退出循环
    #         break

    # 打印初始化时间
    print(time.strftime("%H:%M:%S",time.localtime()))
    # 显示等待
    search = WebDriverWait(driver,timeout=30,poll_frequency=1)\
        .until(lambda x: x.find_element_by_xpath("//*[contains(@text,'更多')]"))
    search.click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
    time.sleep(2)
    driver.find_element_by_id("android:id/switchWidget").click()
    time.sleep(2)


except Exception as e:
    print(e)                          # Message:
finally:
    print(time.strftime("%H:%M:%S", time.localtime()))
    driver.quit()
