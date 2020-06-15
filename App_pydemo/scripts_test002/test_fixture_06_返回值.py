import pytest

@pytest.fixture()
def need_data():
    return 2                                 # 返回数字2

class Test_ABC:

    # 参数引用
    def test_a(self,need_data):
        print("------->test_a")
        assert need_data != 3             # 拿到返回值做一次断言

if __name__ == '__main__':
    pytest.main(["-s","test_fixture_06_返回值.py"])