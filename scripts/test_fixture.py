# 1. 打开浏览器(类级别前置)
# 2. 打开登录页面(方法级别前置)
# 3. 输入用户名,密码,验证码,点击登录
# 4. 关闭退出登录页面(方法级别后置)
# 5. 关闭浏览器 (类级别后置)
# =========
# 1. 打开浏览器
# 2. 打开登录页面
# 3. 输入用户名,密码,验证码,点击登录
# 4. 关闭退出登录页面
# 2. 打开登录页面
# 3. 输入用户名,密码,验证码,点击登录
# 4. 关闭退出登录页面
# 2. 打开登录页面
# 3. 输入用户名,密码,验证码,点击登录
# 4. 关闭退出登录页面
# 5. 关闭浏览器
import pytest


class TestLogin:
    # 类级别的前置和后置
    @pytest.fixture(scope="class", autouse=True)
    def browser_setup_teardown(self):
        print('1. 打开浏览器')
        yield
        print('5. 关闭浏览器')

    # 方法级别的前置和后置
    @pytest.fixture(scope='function', autouse=True)
    def login_page_setup_teardown(self):
        print('2. 打开登录页面')
        yield
        print('4. 关闭退出登录页面')

    def test_login1(self):
        print(f'3.输入用户名1,密码1,验证码1,点击登录')

    def test_login2(self):
        print(f'3.输入用户名2,密码2,验证码2,点击登录')

    def test_login3(self):
        print(f'3.输入用户名3,密码3,验证码3,点击登录')
