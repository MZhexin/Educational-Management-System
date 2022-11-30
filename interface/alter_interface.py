'''
    信息修改界面
'''

# 导入库以及本项目中的其他文件
from sys_users import alter as al
import pyautogui
import time

# 存放学生功能的字典
stu_func_dic = {
    '0':'返回管理界面',
    '1':'学生姓名修改',
    '2':'学生性别修改',
    '3':'所属学部修改',
    '4':'学生课程修改',
    '5':'学生成绩修改'
}

# 存放教师功能的字典
tea_func_dic = {
    '0':'返回管理界面',
    '1':'教师姓名修改',
    '2':'教师性别修改',
    '3':'所属学部修改',
    '4':'教师授课修改',
}

# 存放课程功能的字典
cour_func_dic = {
    '0':'返回管理界面',
    '1':'课程名称修改',
    '2':'所属学部修改',
    '3':'授课教师修改',
}


# 信息修改函数
def alter_interface(object_num):
    alter_object_name_list = ['学生', '教师', '课程']  # 存放三种不同抬头的列表
    alter_object_dic_list = [stu_func_dic, tea_func_dic, cour_func_dic]  # 存放三种不同功能字典的列表
    while True:
        # 初始化界面
        print('{0}信息修改界面'.format(alter_object_name_list[object_num]).center(50,'*'))  # 利用抬头列表打印不同抬头
        for k,v in alter_object_dic_list[object_num].items():    # 利用功能字典列表分别打印待选功能的键值对
            print(k, v)
        print('某某大学教务管理系统'.center(50, '*'))  # 页面底部的标语

        # 选择功能
        func_num = input('请输入您想要的功能:').strip()

        # 判断用户选择的功能是否合法，若合法则运行，不合法则跳出程序
        if object_num == 0:  # 当传入参数为0（表示学生）时
            if func_num not in ['0', '1', '2', '3', '4', '5']:  # 当输入的功能序号不在范围内
                pyautogui.hotkey("Alt", "c")   # 清屏
                # 打印暂无功能界面
                print('{0}信息修改界面'.format(alter_object_name_list[object_num]).center(50,'*'))  # 利用抬头列表打印不同抬头
                print('暂不支持此功能')
                print('某某大学教务管理系统'.center(50, '*'))  # 页面底部的标语
                time.sleep(3)  # 页面暂停3秒
                pyautogui.hotkey("Alt", "c")  # 清屏
                break  # 退出while循环

        if object_num == 1: # 当传入参数为1（表示教师）时
            if func_num not in ['0', '1', '2', '3', '4']:  # 当输入的功能序号不在范围内
                pyautogui.hotkey("Alt", "c") # 清屏
                # 打印暂无功能界面
                print('{0}信息修改界面'.format(alter_object_name_list[object_num]).center(50, '*'))  # 利用抬头列表打印不同抬头
                print('暂不支持此功能')
                print('某某大学教务管理系统'.center(50, '*'))  # 页面底部的标语
                time.sleep(3)  # 页面暂停3秒
                pyautogui.hotkey("Alt", "c")  # 清屏
                break  # 退出while循环

        if object_num == 2:  # 当传入参数为2（表示课程）时
            if func_num not in ['0', '1', '2', '3']:  # 当输入的功能序号不在范围内
                pyautogui.hotkey("Alt", "c") # 清屏
                # 打印暂无功能界面
                print('{0}信息修改界面'.format(alter_object_name_list[object_num]).center(50, '*'))  # 利用抬头列表打印不同抬头
                print('暂不支持此功能')
                print('某某大学教务管理系统'.center(50, '*'))  # 页面底部的标语
                time.sleep(3)  # 页面暂停3秒
                pyautogui.hotkey("Alt", "c")  # 清屏
                break  # 退出while循环

        # 应对不同功能函数的选择
        if func_num == '0':  # 选择功能0，则退出系统
            print('请稍等，正在返回上级页面')
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            break  # 退出while循环

        if object_num == 0:  # 当传入参数为0时，跳转到学生信息修改界面
            print('正在转到信息修改界面')
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            al.stu_alter(func_num)  # 跳转并传递功能参数

        if object_num == 1:  # 当传入参数为1时，跳转到教师信息修改界面
            print('正在转到信息修改界面')
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            al.tea_alter(func_num)  # 跳转并传递功能参数

        if object_num == 2:  # 当传入参数为2时，跳转到课程信息修改界面
            print('正在转到信息修改界面')
            time.sleep(3)  # 页面暂停3秒
            pyautogui.hotkey("Alt", "c")  # 清屏
            al.cour_alter(func_num)  # 跳转并传递功能参数
