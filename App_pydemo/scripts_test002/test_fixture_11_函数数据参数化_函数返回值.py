import pytest

# [(),()]
def re_data_list():
    lis_data=[]
    with open("./data.txt","r") as f:
        for i in f.readlines():
            # print(i)    ding=(123,456)
            # strip 函数默认去除字符串两侧的空格   i.strip()
            # 根据 = 将字符串截取为多个部分
            print(i.strip().split("=")[1])               # (123,456)   (23,45)      # print(i.strip.find('='))   4
            lis_data.append(eval(i.split("=")[1]))       # <class 'str'> eval()方法转换为元组 <class 'tuple'>

        return lis_data          # print(lis_data)  # [(123, 456), (23, 45)]


class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.parametrize("ding,wang",re_data_list())       # 使用函数返回值的形式传入参数值
    def test_a(self,ding,wang):                            # 参数必须和parametrize里面的参数一致
        print("test data:ding=%s,wang=%s"%(ding,wang))
        assert ding+wang == 68
