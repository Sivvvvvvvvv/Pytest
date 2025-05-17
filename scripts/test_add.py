from tools import add


class TestAdd:
    def test_1(self):
        # 判断预期结果和实际结果是否相等
        if 10 == add(0, 10):
            print('0, 10, 10 用例通过')
        else:
            print('0, 10, 10 用例不通过')

    def test_2(self):
        # 判断预期结果和实际结果是否相等
        if 6 == add(1, 5):
            print('1, 5, 6 用例通过')
        else:
            print('1, 5, 6  用例不通过')

    def test_3(self):
        # 判断预期结果和实际结果是否相等
        if 16 == add(9, 7):
            print('9, 7, 16 用例通过')
        else:
            print('9, 7, 16 用例不通过')

# 1, pytest.ini必须放在最外面，是一个整体的项目，对这个项目整体进行控制
# 2，pytest.ini中的参数不要写错，每个参数都有自己的含义
# 3，所有参数共同结合，决定你能不能找到测试用例，去执行
# 4，用例所在的目录设为（目录中包含一个__init__.py文件）
