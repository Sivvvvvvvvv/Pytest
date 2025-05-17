# Pytest ⽤例的书写
# pip list # 查看所有安装的内容
# pytest.ini 是⽤来管理测试⽤例(代码书写的⽤例)的.
# 书写⽤例的步骤:
# 1, 定义测试类(建议 类名以 Test开头)
# 2, 书写测试⽅法, 即真正的⽤例代码(建议 ⽅法名以 test 开
# 头)
# 3, 执⾏⽤例
# --------
# 要求: 测试⽤例的代码⽂件名 不要使⽤中⽂, 遵循标识符的规则
# ⽂件名 建议 以 test 开头 或者 结尾

import pytest


class TestDemo:

    def test_method_1(self):
        # print用来模拟测试用例的执行
        print('测试方法三')

    def test_method_2(self):
        print('测试方法四')


# 用得少
if __name__ == '__main__':
    pytest.main(['-s', 'test_dome_02.py'])
