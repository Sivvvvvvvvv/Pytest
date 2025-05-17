import pytest

from common.read_data import build_data
from tools import add


# pytet.int 放在最外层,pytest配置文件
# 测试数据 单独一个目录data
# 读取测试数据 一般放在common包中，或者最外层
# 用例代码（脚本）一般script（case）包中
# 测试报告的目录 report目录


class TestAdd:
    @pytest.mark.parametrize('a, b, expect', build_data())
    def test_add(self, a, b, expect):
        # 判断预期结果和实际结果是否相等
        print(f'{a}, {b}, {expect} 用例通过')
        assert expect == add(a, b)
