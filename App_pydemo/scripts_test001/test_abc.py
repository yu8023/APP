# 引入pytest包
import pytest

# 函数定义：test开头的测试函数
def test_a():
    print("执行用例01...")
    assert 1

def test_b():
    print("执行用例02...")
    assert 0

def custom_case03():
    print('执行用例03.......')
    assert 1  # 断言成功

if __name__ == '__main__':
    # pytest main运行方式
    pytest.main(["-s","test_abc.py"])      # 传参需要是一个元组()或者列表[]