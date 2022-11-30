
import time
import pyautogui
import sys_users
from sys_users import manage as maa

func_dic = {
    '0':'退出登录',
    '1':'修改密码',
    '2':'查询学籍',
    '3':'查询课程',
    '4':'查询成绩'
}

# 学生界面
def stu_interface(name, gender, dept):
    while True:
        # 初始化界面
        print('亲爱的同学，欢迎回来！'.center(50,'*'))
        for k,v in func_dic.items():   # 打印待选功能
            print(k, v)
        print('北京工业大学教务管理系统'.center(50, '*'))

        # 选择功能
        func_num = input('请选择您想要的功能:').strip()

        # 判断用户选择的功能是否合法，若合法则运行，不合法则跳出程序
        if func_num not in ['0','1','2','3','4']:
            pyautogui.hotkey("Alt", "c")
            print('亲爱的同学，欢迎回来！'.center(50,'*'))
            print('暂不支持此功能')
            print('北京工业大学教务管理系统'.center(50, '*'))
            time.sleep(3)
            pyautogui.hotkey("Alt", "c")
            break

        # 选择功能0，则退出系统
        if func_num == '0':
            print('请稍等，正在返回上级页面')
            time.sleep(3)
            pyautogui.hotkey("Alt", "c")
            break

        # 选择功能1，则通过调用学生类里的方法来修改密码
        if func_num == '1':
            cur_user = sys_users.Student(name, gender, dept)
            print('正在跳转，请稍等')
            time.sleep(3)
            pyautogui.hotkey("Alt", "c")
            cur_user.change_pass()

        # 选择功能2，则通过调用学生类里的方法来查看自己的学籍
        if func_num == '2':
            cur_user = sys_users.Student(name, gender, dept)
            print('系统加载中，请稍等')
            time.sleep(3)
            cur_user.select_myself()

        # 选择功能3，则通过调用学生类里的方法来查看课程信息
        if func_num == '3':
            print('系统加载中，请稍等')
            time.sleep(3)
            pyautogui.hotkey("Alt", "c")
            maa.select(2)

        # 选择功能4，则通过调用学生类里的方法来查看自己的成绩
        if func_num == '4':
            cur_user = sys_users.Student(name, gender, dept)
            print('系统加载中，请稍等')
            time.sleep(3)
            cur_user.select_my_score()