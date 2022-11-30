
import time
import pyautogui
import sys_users
from interface import manage_interface as ma
import sys_users.manage as maa
import sys_users.alter as al

func_dic = {
    '0':'退出登录',
    '1':'修改密码',
    '2':'查询个人信息和授课课程',
    '3':'学生管理',
    '4':'课程管理',
    '5':'修改学生成绩',
}

# 教师界面
def tea_interface(name, gender, dept):
    while True:
        # 初始化界面
        print('亲爱的教职工，欢迎回来！'.center(50,'*'))
        for k,v in func_dic.items():    # 打印待选功能
            print(k, v)
        print('北京工业大学教务管理系统'.center(50, '*'))

        # 选择功能
        func_num = input('请选择您想要的功能:').strip()

        # 判断用户选择的功能是否合法，若合法则运行，不合法则跳出程序
        if func_num not in ['0', '1', '2', '3', '4', '5']:
            pyautogui.hotkey("Alt", "c")
            print('亲爱的教职工，欢迎回来！'.center(50, '*'))
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

        # 选择功能1，则通过调用教师类里的方法来修改密码
        if func_num == '1':
            cur_user = sys_users.Teacher(name, gender, dept)
            print('正在跳转，请稍等')
            time.sleep(3)
            pyautogui.hotkey("Alt", "c")
            cur_user.change_pass()

        # 选择功能2，调用教师类里的方法来自查信息
        if func_num=='2':
            cur_user = sys_users.Teacher(name, gender, dept)
            print('正在跳转，请稍等')
            time.sleep(3)
            pyautogui.hotkey("Alt", "c")
            cur_user.select_myself()

        # 选择功能3、4，则跳转至相应的管理界面
        # 学生管理界面
        if func_num == '3':
            print('正在跳转，请稍等')
            time.sleep(3)
            pyautogui.hotkey("Alt", "c")
            ma.manage_func(0)

        # 课程管理界面
        if func_num == '4':
            print('正在跳转，请稍等')
            time.sleep(3)
            pyautogui.hotkey("Alt", "c")
            ma.manage_func(2)

        # 选择功能5
        if func_num == '5':
            print('正在跳转，请稍等')
            time.sleep(3)
            pyautogui.hotkey("Alt", "c")
            al.stu_alter('5')




