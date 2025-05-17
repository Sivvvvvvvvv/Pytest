def add(a, b):
    return a + b


def add_1(a, b):
    """两位数加法计算器"""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        # isinstance判断是否是a是否为int，float这两个类型之一 判断是否为数字
        return 'error,非数字'
    if -99 < a < 99 and -99 < b < 99:
        return a + b
    else:
        return 'error,数据的范围必须大于等于 -99 并且小于等于99'
