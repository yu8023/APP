from App.init_driver.init_Driver import init_driver
import time


driver = init_driver()

# 给用户为13488834010发送三条短信，内容分别为123456、sd456、你好

#进入短信应用，点击+ 号，发起新的对话
driver.find_element_by_id("com.android.messaging:id/start_new_conversation_button").click()
# 定位收件人，输入用户号码
driver.find_element_by_id("com.android.messaging:id/recipient_text_view").send_keys("13488834010")
driver.keyevent(66)

# 发送三次短信
data_lis = ["123456","sd456","你好"]
for i in data_lis:
      driver.find_element_by_id("com.android.messaging:id/compose_message_text").send_keys(i)
      # 点击发送按钮
      driver.find_element_by_id("com.android.messaging:id/self_send_icon").click()
      print("%s短信发送成功" % i)
      time.sleep(2)


# 手机截图
driver.get_screenshot_as_file("./screenshot_page/sendMessage.png")
print("截图成功")


# 退出驱动对象
driver.quit()