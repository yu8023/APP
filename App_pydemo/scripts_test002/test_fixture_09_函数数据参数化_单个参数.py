import pytest

class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.parametrize("ding",[123,456])             # a参数被赋予两个值，函数会运行两遍
    def test_a(self,ding):                            # 参数必须和parametrize里面的参数一致
        print("test data:ding=%d"%ding)
        assert ding == 234