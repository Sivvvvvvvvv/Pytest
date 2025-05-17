from tools import add


# 断言: 让程序代码自动判断预期结果和实际结果是否相符.
#
# 如果相符,则断言成功,用例通过.
# 如果不相符, 则断言失败,用例不通过,抛出异常
#
# pytest 中的 断言使用的是 assert 关键字
# 语法:
# assert 条件   # if 语句中的条件,都可以用在这里
# - 如果条件为 True, 断言成功,用例通过
# - 如果条件为 False, 断言失败,用例不通过,抛出异常
#
# 常用：
# 断言是否相等：
# assert 预期结果 == 实际结果   # 是否相等
#
# 断言是否包含
# assert 预期结果 in 实际结果   # 预期结果是否包含在实际结果中

class TestAdd:

    def test_1(self):
        print('0, 10, 10 ')
        assert 10 == add(0, 10)

    def test_2(self):
        # 判断预期结果和实际结果是否相等
        print('1, 5, 6 用例通过')
        assert 6 == add(1, 5)

    def test_3(self):
        print('9, 7, 16 用例通过')
        assert 17 == add(9, 7)
