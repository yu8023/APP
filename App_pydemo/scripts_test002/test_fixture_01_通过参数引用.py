import pytest

class Test_ABC:

    @pytest.fixture()
    def before(self):
        print("------->before")

    # 参数引用
    def test_a(self,before):                 # ⚠️ test_a方法传入了被fixture标识的函数，以变量的形式
        print("------->test_a")
        assert True

if __name__ == '__main__':
    pytest.main(["-s","test_fixture_01_通过参数引用.py"])