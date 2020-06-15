from App.init_driver.init_Driver import init_driver
import time

# 函数调用  将运行结果(手机驱动对象)返回给函数的调用者driver
driver = init_driver()
print("driver：", driver)
time.sleep(5)

# # 关闭app
# driver.close_app()
#
# # 脚本内启动其他app
# driver.start_activity("com.android.dialer",".app.DialtactsActivity")

# # 安装apk
# driver.install_app(r"F:\QMDownload\SoftMgr\jinritoutiao.apk")
# print("安装成功")
# """
# import os
# os.system("adb install F:\QMDownload\SoftMgr\qq_email.apk")
# """
# #卸载app
# driver.remove_app("com.tencent.androidqqmail")
# """
# import os
# os.system("adb uninstall com.tencent.androidqqmail")
# """
# 判断app是否安装
# print("QQ邮箱：",driver.is_app_installed("com.tencent.androidqqmail"))
# print("电话：",driver.is_app_installed("com.android.dialer"))
# print("和客户:",driver.is_app_installed("com.freelynet.moiblecrm"))

# if driver.is_app_installed("com.tencent.androidqqmail"):
#     print("我存在")
#     driver.remove_app("com.tencent.androidqqmail")
#     print("卸载完成")
# else:
#     print("我不存在")
#     driver.install_app("F:\QMDownload\SoftMgr\qq_email.apk")
#     print("安装完成")

# 发送文件到手机
# import base64
# data2 = str(base64.b64encode("丁丁".encode('utf-8')),'gbk')  # 5LiB5LiB
# data3 = str(base64.b64encode("丁丁".encode('utf-8')))        # b'5LiB5LiB'
# data4 = base64.b64encode("丁丁".encode('utf-8'))             # b'5LiB5LiB'

# base64编码
# data1 = str(base64.b64encode("丁丁".encode('utf-8')),'utf-8')  # 5LiB5LiB
# print(data1)
# driver.push_file("/sdcard/push.txt",data1)

# 从手机中拉取文件
import base64
data5 = driver.pull_file('/sdcard/push.txt') # 返回数据为base64编码  5LiB5LiB
# 解码
b_data5 = str(base64.b64decode(data5),'utf-8')
print(b_data5)                      # dingding
print(type(b_data5))                # <class 'str'>
# 以二进制类型写入文件
"""
   str类型数据转换成bytes类型(二进制类型)
   data = b_data.encode()
   b_data = data.decode()
"""
with open('./phone.txt','wb') as f:
    f.write(b_data5.encode())

# 打印当前页面文档结构
print(driver.page_source)
current_page_data = driver.page_source

for i in ("WLAN","显示"):        # 元组中只有一个元素时, 需在最尾部添加一个逗号
    if i in current_page_data:
        print(True)
    else:
        print(False)

# 退出手机驱动对象
driver.quit()