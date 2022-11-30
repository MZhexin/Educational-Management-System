'''
    主页面
'''

# 导入库以及本项目中的其他文件
from sys_users import operations as op
import pyautogui
import time

# 功能字典
func_dic = {
    '0':'退出系统',
    '1':'学生登录',
    '2':'教师登录',
    '3':'管理员登录',
    '4':'新用户注册'
}

# ”运行“函数
def run():
    while True:
        # 初始化界面
        print('某某大学欢迎您！'.center(50,'*'))
        for k,v in func_dic.items():    # 打印待选功能的键值对
            print(k, v)
        print('某某大学教务管理系统'.center(50, '*'))

        # 选择功能
        func_num = input('请输入您想要的功能:').strip()

        # 判断用户选择的功能是否合法，若合法则运行，不合法则跳出程序
        if func_num not in ['0', '1', '2', '3', '4']: # 当输入的功能序号不在范围内
            pyautogui.hotkey("Alt", "c")   # 清屏
            # 打印暂无功能界面
            print('某某大学欢迎您！'.center(50, '*'))
            print('暂不支持此功能')
            print('某某大学教务管理系统'.center(50, '*'))
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            break  # 退出while循环

        # 应对不同功能函数的选择
        if func_num == '0':  # 选择功能0，则退出系统
            pyautogui.hotkey("Alt", "c")  # 清屏
            print('某某大学欢迎您！'.center(50, '*'))
            print('已退出系统')
            print('某某大学教务管理系统'.center(50, '*'))
            break  # 退出系统

        if func_num == '4':   # 选择功能4，注册新用户
            print('正在转到注册界面')
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            op.register() # 跳转至注册函数

        if func_num == '1' or func_num == '2' or func_num == '3':  # 选择功能1、2、3，登录系统
            print('正在转到登录界面')
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            op.login(func_num)  # 跳转至登录函数并传递功能参数