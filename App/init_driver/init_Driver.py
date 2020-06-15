from appium import webdriver
import os


# 函数定义：函数名init_driver
def init_driver():

    # server 启动参数
    desired_caps = {}
    # 系统
    desired_caps['platformName'] = 'Android'
    # 版本
    desired_caps['platformVersion'] = '6.0'
    # 设备号
    os.system("adb devices")
    desired_caps['deviceName'] = '192.168.140.101:5555' # os.system("adb devices") 替换

    os.system("adb shell dumpsys window windows | findstr mFocusedApp")
    # 包名
    # desired_caps['appPackage'] = 'com.android.settings'    # 设置
    # desired_caps['appPackage'] = 'com.android.contacts'    # 通讯录
    desired_caps['appPackage'] = 'com.android.messaging'    # 短信
    # desired_caps['appPackage'] = 'io.manong.developerdaily'  # 头条
    # desired_caps['appPackage'] = 'com.amaze.filemanager'     # 文件管理器

    # 启动名
    # desired_caps['appActivity'] = '.Settings'              # 设置
    # desired_caps['appActivity'] = '.activities.PeopleActivity'  # 通讯录
    desired_caps['appActivity'] = '.ui.conversationlist.ConversationListActivity'    # 短信
    # desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'      # 头条
    # desired_caps['appActivity'] = '.activities.MainActivity'  # 文件管理器

    # unicode设置(允许中文输入)
    desired_caps['unicodeKeyboard'] = True
    # 键盘设置(允许中文输入)
    desired_caps['resetKeyboard'] = True

    # 声明手机驱动对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)   # 127.0.0.1:4723

    # 使用return 语句将函数的运行结果返回给函数的调用者
    return driver


if __name__ == '__main__':

    driver = init_driver()