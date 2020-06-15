import pytest

@pytest.fixture(autouse=True)               # 设置为True自动运行，优先于测试类运行
def before():
    print("------->before")

class Test_ABC:
    def setup(self):
        print("------->setup")
    def test_a(self):
        print("------->test_a")
        assert 1

if __name__ == '__main__':
    pytest.main(["-s","test_fixture_03_默认设置为运行.py"])