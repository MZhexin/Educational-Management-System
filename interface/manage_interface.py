'''
    信息管理界面
'''

# 导入库以及本项目中的其他文件
import time
from sys_users import manage as ma
from interface import alter_interface as al
import pyautogui

# 存放学生功能的字典
stu_func_dic = {
    '0':'返回用户界面',
    '1':'学生信息添加',
    '2':'学生信息删除',
    '3':'学生信息修改',
    '4':'学生信息查询'
}

# 存放教师功能的字典
tea_func_dic = {
    '0':'返回用户界面',
    '1':'教师信息添加',
    '2':'教师信息删除',
    '3':'教师信息修改',
    '4':'教师信息查询'
}

# 存放课程功能的字典
cour_func_dic = {
    '0':'返回用户界面',
    '1':'课程信息添加',
    '2':'课程信息删除',
    '3':'课程信息修改',
    '4':'课程信息查询'
}


# 信息管理函数
def manage_func(object_num):
    managed_object_name_list = ['学生', '教师', '课程']   # 存放三种不同抬头的列表
    managed_object_dic_list = [stu_func_dic, tea_func_dic, cour_func_dic]  # 存放三种不同功能字典的列表
    while True:
        # 初始化界面
        print('{0}信息管理界面'.format(managed_object_name_list[object_num]).center(50,'*'))  # 利用抬头列表打印不同抬头
        for k,v in managed_object_dic_list[object_num].items():    # 利用功能字典列表分别打印待选功能的键值对
            print(k, v)
        print('某某大学教务管理系统'.center(50, '*')) # 页面底部的标语

        # 选择功能
        func_num = input('请输入您想要的功能:').strip()

        # 判断用户选择的功能是否合法，若合法则运行，不合法则跳出程序
        if func_num not in ['0', '1', '2', '3', '4']: # 当输入的功能序号不在范围内
            pyautogui.hotkey("Alt", "c") # 清屏
            # 打印暂无功能界面
            print('{0}信息管理界面'.format(managed_object_name_list[object_num]).center(50,'*')) # 利用抬头列表打印不同抬头
            print('暂不支持此功能')
            print('某某大学教务管理系统'.center(50, '*')) # 页面底部的标语
            time.sleep(3) # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            break  # 退出while循环

        # 应对不同功能函数的选择
        if func_num == '0':  # 选择功能0，则退出系统
            print('请稍等，正在返回上级页面')
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            break  # 退出while循环

        if func_num == '1':  # 选择功能1，增加信息
            print('正在转到信息录入界面')
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            ma.insert(object_num)  # 跳转并传递角色参数

        if func_num == '2':  # 选择功能2，删除信息
            print('正在转到信息删除界面')
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            ma.delete(object_num)   # 跳转并传递角色参数

        if func_num == '3':  # 选择功能3,修改信息
            print('正在转到信息修改界面')
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            al.alter_interface(object_num)  # 跳转并传递功能参数

        if func_num == '4':  # 选择功能4，查询信息
            print('正在转到信息查询界面')
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            ma.select(object_num)  # 跳转并传递功能参数