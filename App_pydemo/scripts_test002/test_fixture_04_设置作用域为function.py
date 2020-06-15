import pytest

@pytest.fixture(scope='function',autouse=True)         # 作用域设置为function：作用于每个测试方法，每个test都运行一次，True自动运行
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
    pytest.main(["-s","test_fixture_04_设置作用域为function.py"])