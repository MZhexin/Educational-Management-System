
import os
import time
import pyautogui
import sys_users
import sys_users.student as student
import sys_users.teacher as teacher
import sys_users.admin as admin

def register():
    type_dic = {
        '0': '管理员',
        '1': '学生',
        '2': '教师'
    }
    print('欢迎注册'.center(50, '*'))
    for k, v in type_dic.items():
        print(k, v)
    user_type = input('请选择您需要注册的类型：')

    if user_type not in ['0', '1', '2']:
        print('暂无此类用户')
        time.sleep(3)
        register()
    else:
        if user_type == '1':
            with open('stu_data.txt', 'r', encoding='utf-8') as f1:
                stu_info = f1.readlines()
                username = input('请输入您的姓名:')
                for stu in stu_info:
                    while username == stu.strip().split(',')[0]:
                        print('用户已存在')
                        username = input('请重新输入您的姓名：')
                else:
                    password = input('请输入您的密码(P.S.请不要在密码中使用逗号，感谢):')
                    if ',' in password:
                        print('密码不合法，注册失败')
                        print('正在转到注册界面')
                        time.sleep(3)
                        pyautogui.hotkey("Alt", "c")
                        register()
                    else:
                        with open('stu_data.txt', 'a', encoding='utf-8') as f2:
                            f2.write('\n' + username + ',' + password)
                            info_list = ['性别', '学部']
                            for i in range(0, len(info_list)):
                                info = input("请输入您的{0}".format(info_list[i]))
                                f2.write(',' + info)
                            print('注册成功，正在返回主页')
                            time.sleep(3)
                            pyautogui.hotkey("Alt", "c")

        elif user_type == '2':
            with open('tea_data.txt', 'r', encoding='utf-8') as f1:
                tea_info = f1.readlines()
                username = input('请输入您的姓名:')
                for tea in tea_info:
                    while username == tea.strip().split(',')[0]:
                        print('用户已存在')
                        username = input('请重新输入您的姓名：')
                else:
                    password = input('请输入您的密码(P.S.请不要在密码中使用逗号，感谢):')
                    if ',' in password:
                        print('密码不合法，注册失败')
                        print('正在转到注册界面')
                        time.sleep(3)
                        pyautogui.hotkey("Alt", "c")
                        register()
                    else:
                        with open('tea_data.txt', 'a', encoding='utf-8') as f2:
                            f2.write('\n' + username + ',' + password)
                            info_list = ['性别', '学部']
                            for i in range(0, len(info_list)):
                                info = input("请输入您的{0}".format(info_list[i]))
                                f2.write(',' + info)
                            print('注册成功，正在返回主页')
                            time.sleep(3)
                            pyautogui.hotkey("Alt", "c")

        elif user_type == '0':
            with open('admin_data.txt', 'r', encoding='utf-8') as f1:
                admin_info = f1.readlines()
                username = input('请输入您的姓名:')
                for admin in admin_info:
                    while username == admin.strip().split(',')[0]:
                        print('用户已存在')
                        username = input('请重新输入您的姓名：')
                    f1.close()
                else:
                    password = input('请输入您的密码(P.S.请不要在密码中使用逗号，感谢):')
                    if ',' in password:
                        print('密码不合法，注册失败')
                        print('正在转到注册界面')
                        time.sleep(3)
                        pyautogui.hotkey("Alt", "c")
                        register()
                    else:
                        with open('admin_data.txt', 'a', encoding='utf-8') as f2:
                            f2.write('\n' + username + ',' + password)
                            print('注册成功，正在返回主页')
                            time.sleep(3)
                            pyautogui.hotkey("Alt", "c")



def login(func_num):
    file_list = ['stu_data.txt', 'tea_data.txt', 'admin_data.txt']
    print('欢迎登录'.center(50, '*'))
    user_name = input('请输入您的姓名：').strip()
    with open(file_list[int(func_num) - 1], 'r', encoding='utf-8') as f:
        user_info = f.readlines()
    for user in user_info:
        if user_name == user.strip().split(',')[0]:
            user_password = input('请输入您的密码：').strip()
            print('正在登录'.center(50, '*'))
            while user_password != user.strip().split(',')[1]:
                print('密码错误，请重新输入')
                user_password = input('请输入您的密码：').strip()
                print('正在登录'.center(50, '*'))
            if user_password == user.strip().split(',')[1]:
                print('登录成功，请等待系统初始化')
                time.sleep(3)
                pyautogui.hotkey("Alt", "c")
                if func_num == '1':
                    gender = user.strip().split(',')[2]
                    dept = user.strip().split(',')[3]
                    student.stu_interface(user_name, gender, dept)
                    return
                elif func_num == '2':
                    gender = user.strip().split(',')[2]
                    dept = user.strip().split(',')[3]
                    teacher.tea_interface(user_name, gender, dept)
                    return
                elif func_num == '3':
                    admin.admin_interface(user_name)
                    return
    else:
        print('用户不存在，请先注册')
        print('正在转到注册界面')
        time.sleep(3)
        pyautogui.hotkey("Alt", "c")
        register()




