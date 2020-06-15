import pytest

def add():
    with open('./data.txt','r') as f:
        if '5' in f.read():
            return True
        else:
            return False

class Test_Pas:

    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.xfail(condition=add(), reason='test')
    def test_a(self):
        print("------->test_a")
        return True

    @pytest.mark.skipif(condition=add(),reason='test')      # 两个参数必填，条件为真，则跳过测试函数
    def test_b(self):
        print("------->test_b")
        return False

