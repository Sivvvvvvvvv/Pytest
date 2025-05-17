# 在测试方法中,使用数据的地方,使用参数来代替,然后在运行的时候 传递实参值.
# 1. 将用例中的数据 变为参数书写
# 2. 组织测试数据 ---> [(), (), ()] 或者 [[], []], 内部的元组或者列表 就是一组测试数据
# 3. 使用装饰器完成参数化
# @pytest.mark.parametrize('参数1, 参数2, ...', 测试数据)
import pytest

from tools import add

data_list = [(0, 10, 10), (1, 5, 6), (9, 7, 16), (10, 10, 20)]


class TestAdd:
    @pytest.mark.parametrize('a, b, expect', data_list)
    def test_add(self, a, b, expect):
        # 判断预期结果和实际结果是否相等
        print(f'{a}, {b}, {expect} 用例通过')
        assert expect == add(a, b)
