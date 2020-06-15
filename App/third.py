from App.init_driver.init_Driver import init_driver
import os
import base64

# 函数定义：push
def push(tag,pc_path,app_path,driver=None):
    # tag 1: adb   2: appium
    if tag==1:
        os.system("adb push %s %s" % (pc_path,app_path))
    if tag==2:
        # 以只读的方式打开pc路径下的某文件   with open 不用关闭文件
        with open(pc_path,'r') as f:
            # base64编码
            data = str(base64.b64encode(f.read().encode('utf-8')),'utf-8')
            # 将读到的内容发送到手机路径下
            driver.push_file(app_path,data)


if __name__ == '__main__':

    # 声明对象
    driver = init_driver()   # 函数调用 手机驱动对象返回给函数的调用者
    # appium校验
    push(tag=2,pc_path=r'D:\LearningTest\pycharm\WebDriver\App\hello.txt',app_path='/sdcard',driver=driver)
    print('发送成功')

    # adb方式校验
    # push(tag=1,pc_path=r'C:\Users\dby\Desktop\hello.txt',app_path='/sdcard')
