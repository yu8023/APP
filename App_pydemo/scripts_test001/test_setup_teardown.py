# 引入pytest包
import pytest

class Test_ST(object):

    # 函数级别 setup()／teardown() 运行一次测试函数会运行一次setup和teardown
    # def setup(self):
    #     print("start...")
    #
    # def teardown(self):
    #     print("end...")

    """
    类级别 setup_class() / teardown_class()
    在一个测试内只运行一次setup_class和teardown_class，不关心测试类内有多少个测试函数
    """
    def setup_class(self):
        print("start...")

    def teardown_class(self):
        print("end...")

    # 函数定义：test开头的测试函数
    @pytest.mark.run(order=-2)
    def test_a(self):
        print("执行用例01...")
        assert 1

    @pytest.mark.run(order=-1)
    def test_b(self):
        print("执行用例02...")
        assert 0


if __name__ == '__main__':
    pytest.main(["-s","test_setup_teardown.py"])      # 传参需要是一个元组()或者列表[]