import pytest

from tools import add_1
from common.read_data import build_data_1


class TestAdd:
    @pytest.mark.parametrize('a, b, expect', build_data_1())
    def test_add_1(self, a, b, expect):
        if isinstance(expect, str):
            # 判断预期结果和实际结果是否相等
            assert expect in add_1(a, b)
        else:
            assert expect == add_1(a, b)
