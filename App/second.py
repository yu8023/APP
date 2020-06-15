from App.init_driver.init_Driver import init_driver

# 函数定义：open_setting
def open_setting():

    # 函数调用 手机驱动对象返回给函数的调用者
    driver = init_driver()
    driver.quit()

if __name__ == '__main__':
    # 函数调用
    open_setting()