import pytest

@pytest.fixture(params=[1, 2, 3])
def need_data(request):                 # 传入参数request  系统封装参数
    return request.param                 # 取列表中单个值，默认的取值方式

class Test_ABC:

    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    # @pytest.mark.usefixtures("init_data")     # 函数引用
    def test_a(self,init_data):             # 参数引用
        # print(need_data)
        print("------->test_a")
        assert init_data == 3             # 断言need_data不等于3

if __name__ == '__main__':
    pytest.main(["-s","test_fixture_06_params.py"])