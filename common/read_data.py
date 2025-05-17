import json

from config import BASE_DIR


def build_data():
    # 读取数据文件
    with open(BASE_DIR + '/data/add.json', encoding='utf-8') as f:
        data = json.load(f)  # [[], []]

    return data

def build_data_1():
    # 读取数据文件
    with open(BASE_DIR + '/data/add_1.json', encoding='utf-8') as f:
        data = json.load(f)  # [[], []]

    return data

if __name__ == '__main__':
    print(build_data())
    print(build_data_1())

# pytet.int 放在最外层,pytest配置文件
# 测试数据 单独一个目录data
# 读取测试数据 一般放在common包中，或者最外层
# 用例代码（脚本）一般script（case）包中
# 测试报告的目录 report目录
