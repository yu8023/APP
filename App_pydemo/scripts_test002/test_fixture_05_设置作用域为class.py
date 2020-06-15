import pytest

@pytest.fixture(scope='class',autouse=True)             # 作用域设置为class：作用于整个类，只运行一次，自动运行
def before():
    print("------->before")

class Test_ABC:

    def setup(self):
        print("------->setup")

    def test_a(self):
        print("------->test_a")
        assert 1

    def test_b(self):
        print("------->test_b")
        assert 1

if __name__ == '__main__':
    pytest.main(["-s","test_fixture_05_设置作用域为class.py"])