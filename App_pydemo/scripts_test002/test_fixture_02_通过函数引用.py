import pytest

@pytest.fixture()
def init_xx():
    print("------->before")
    with open("./data.txt","w") as f:
        f.write('2')

# 函数引用
@pytest.mark.usefixtures("init_xx")
class Test_ABC:

    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    def test_b(self):
        with open("./data.txt","r") as f:
            # print("..读数据：",f.read())                # 1
            # print("..读数据类型：",type(f.read()))      #  <class 'str'>
            data = f.read()
        assert data == '1','断言失败'

    def test_a(self):
        print("......test_a")
        assert True

if __name__ == '__main__':
    pytest.main(["-s","test_fixture_02_通过函数引用.py"])
