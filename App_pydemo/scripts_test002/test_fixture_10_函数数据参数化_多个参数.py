
import pytest

class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.parametrize("ding,wang",[(123,456),(23,45)])     # 参数a,b均被赋予两个值，函数会运行两遍
    def test_a(self,ding,wang):                                         # 参数必须和parametrize里面的参数一致
        print("test data:ding=%d,wang=%d"%(ding,wang))
        assert ding+wang == 68

    # @pytest.fixture(params=[123,456])
    # def xx(self,request):           # 传入参数request  系统封装参数
    #     return  request.param            # 取列表中单个值，默认的取值方式
