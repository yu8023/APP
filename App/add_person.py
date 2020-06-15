from App.init_driver.init_Driver import init_driver
import time

# 函数调用 手机驱动对象返回给函数的调用者
driver = init_driver()

# 8.0手机模拟电话本新建用户 张三，要求必填信息为 姓名 电话 电子邮件 网址，保存后修改张三姓名改为李四
# 点击添加按钮
add_person = driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
time.sleep(3)

# 处理弹窗
driver.find_element_by_id("com.android.contacts:id/left_button").click()
time.sleep(3)

# 点击输入姓名、电话
name1 = driver.find_element_by_xpath("//*[contains(@text,'名字')]").send_keys("张三")   # 乱码加u
time.sleep(1)
iphone = driver.find_element_by_xpath("//*[contains(@text,'电话')]").send_keys("12345678")
time.sleep(2)
email = driver.find_element_by_xpath("//*[contains(@text,'电子邮件')]").send_keys("123@qq.com")
time.sleep(2)

#向上滑动：drag_and_drop
el1 = driver.find_element_by_xpath("//*[contains(@text,'电话')]")
el2 = driver.find_element_by_id("com.android.contacts:id/account_type")
driver.drag_and_drop(el1,el2)
time.sleep(2)

# 点击更多字段
more = driver.find_element_by_xpath("//*[contains(@text,'更多字段')]").click()
time.sleep(2)

# 向上滑动：scroll
el3 = driver.find_element_by_xpath("//*[contains(@text,'电话')]")
el4 = driver.find_element_by_xpath("//*[contains(@text,'姓氏拼音')]")
driver.scroll(el3,el4)
time.sleep(2)

internet = driver.find_element_by_xpath("//*[contains(@text,'网站')]").send_keys("http://www.baidu.com")

# 点击保存
driver.find_element_by_id("com.android.contacts:id/editor_menu_save_button").click()
time.sleep(3)

# 修改姓名
driver.find_element_by_id("com.android.contacts:id/menu_edit").click()
time.sleep(2)

name2 = driver.find_elements_by_class_name("android.widget.EditText")
name2[1].clear()
name2[1].send_keys("王二")
# 点击保存
driver.find_element_by_id("com.android.contacts:id/editor_menu_save_button").click()

time.sleep(2)
driver.quit()
