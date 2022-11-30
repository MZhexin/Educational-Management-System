
import os
import time
import pyautogui
import sys_users
import sys_users.student as student
import sys_users.teacher as teacher
import sys_users.admin as admin

managed_object_name_list = ['学生', '教师', '课程']

def insert(object_num):
    pyautogui.hotkey("Alt", "c")
    print('某某大学信息录入界面'.center(50, '*'))
    # 插入学生
    file_data1 = ''
    file_data2 = ''
    if object_num == 0:
        new_course = []
        course_exist = 0
        new_name = input('请输入学生的姓名').strip()
        with open('stu_data.txt', 'r', encoding='utf-8') as f:
            stu_info = f.readlines()
            for stu in stu_info:
                while new_name == stu.strip().split(',')[0]:
                    print('学生已存在')
                    new_name = input('请重新输入学生的姓名：')
            else:
                new_gender = input('请输入学生的性别').strip()
                new_dept = input('请输入学生所属学部').strip()
                with open('stu_data.txt', 'a', encoding='utf-8') as f1:
                    file_data1 = '\n' + new_name + ',' + '114514' + ',' + new_gender + ',' + new_dept
                    with open('cour_data.txt', 'r', encoding='utf-8') as f2:
                        course_info = f2.readlines()
                        new_course_num = int(input('请输入学生所修课程的数目').strip())
                        for i in range(1, new_course_num + 1):
                            course_exist = 0
                            while course_exist == 0:
                                course = input('请输入学生所修的第{0}门课程名'.format(i))
                                for cour in course_info:
                                    if course == cour.strip().split(',')[0]:
                                        new_course.append(course)
                                        file_data1 = file_data1 + ',' + course
                                        course_exist = 1
                                        break
                                else:
                                    if course_exist == 0:
                                        print("课程不存在，请重新输入")
                    f1.write(file_data1)
        with open('stu_score.txt','a', encoding='utf-8') as f3:
            file_data2 = '\n' + new_name
            for i in range(0, new_course_num):
                score = input('请输入学生所修{0}课程的成绩'.format(new_course[i]))
                file_data2 = file_data2 + ',' + score
            f3.write(file_data2)
            print('插入成功\t初始密码为114514')
            print('正在返回上级界面')
            time.sleep(3)
            pyautogui.hotkey("Alt", "c")

    # 插入教师
    if object_num == 1:
        file_data1 = ''
        file_data2 = ''
        if object_num == 1:
            course_exist = 0
            new_name = input('请输入教师的姓名').strip()
            with open('tea_data.txt', 'r', encoding='utf-8') as f:
                tea_info = f.readlines()
                for tea in tea_info:
                    while new_name == tea.strip().split(',')[0]:
                        print('教师已存在')
                        new_name = input('请重新输入教师的姓名：')
                else:
                    new_gender = input('请输入教师的性别').strip()
                    new_dept = input('请输入教师所属学部').strip()
                    file_data1 = '\n' + new_name + ',' + '1919810' + ',' + new_gender + ',' + new_dept
                    with open('tea_data.txt', 'a', encoding='utf-8') as f1:
                        with open('cour_data.txt', 'r', encoding='utf-8') as f2:
                            course_info = f2.readlines()
                            new_course_num = int(input('请输入教师所授课程的数目').strip())
                            for i in range(1, new_course_num + 1):
                                while course_exist == 0:
                                    course = input('请输入教师所授的第{0}门课程名'.format(i))
                                    for cour in course_info:
                                        if course == cour.strip().split(',')[0]:
                                            file_data1 = file_data1 + ',' + course
                                            course_exist = 1
                                            break
                                    else:
                                        if course_exist == 1:
                                            break
                                        print('该课程不存在，请重新输入')
                            for cour in course_info:
                                if  course == cour.strip().split(',')[0]:
                                    file_data2 = file_data2 + cour.replace('\n', ',' + new_name) + '\n'
                                else:
                                    file_data2 = file_data2 + cour
                            f1.write(file_data1)
                            with open('cour_data.txt', 'w', encoding='utf-8') as f2:
                                f2.write(file_data2)
                print('插入成功\t初始密码为1919810')
                print('正在返回上级界面')
                time.sleep(3)
                pyautogui.hotkey("Alt", "c")

    # 插入课程
    if object_num == 2:
        file_data1 = ''
        file_data2 = ''
        teacher_exist = 0
        new_name = input('请输入课程名').strip()
        with open('cour_data.txt', 'r', encoding='utf-8') as f:
            cour_info = f.readlines()
            for cour in cour_info:
                while new_name == cour.strip().split(',')[0]:
                    print('课程已存在')
                    new_name = input('请重新输入课程名：')
            else:
                new_dept = input('请输入课程所属学部').strip()
                with open('cour_data.txt', 'a', encoding='utf-8') as f1:
                    file_data1 = '\n' + new_name + ',' + new_dept
                    with open('tea_data.txt', 'r', encoding='utf-8') as f2:
                        tea_info = f2.readlines()
                        while teacher_exist == 0:
                            new_tea = input('请输入授课教师姓名').strip()
                            for tea in tea_info:
                                if new_tea == tea.strip().split(',')[0]:
                                    file_data1 = file_data1 + ',' + new_tea
                                    teacher_exist = 1
                                    break
                            else:
                                if teacher_exist == 1:
                                    break
                                print('该教师不存在，请重新输入')
                        for tea in tea_info:
                            if new_tea == tea.strip().split(',')[0]:
                                tea = tea.replace('\n', ',' + new_name) + '\n'
                            file_data2 = file_data2 + tea
                        f1.write(file_data1)
                        with open('tea_data.txt', 'w', encoding='utf-8') as f2:
                            f2.write(file_data2)
                        print('插入成功')
                        print('正在返回上级界面')
                        time.sleep(3)
                        pyautogui.hotkey("Alt", "c")


def delete(object_num):
    pyautogui.hotkey("Alt", "c")
    print('某某大学信息删除界面'.center(50, '*'))
    # 删除学生
    if object_num == 0:
        line_count = 0
        is_existed = 0
        name = input('请输入需要删除的学生信息：').strip()
        with open('stu_data.txt', 'r', encoding='utf-8') as f1:
            stu_info = f1.readlines()
            for stu in stu_info:
                if name == stu.strip().split(',')[0]:
                    del stu_info[line_count]
                    with open('stu_data.txt', 'w', encoding='utf-8') as f2:
                        f2.write(''.join(stu_info))
                    is_existed = 1
                else:
                    line_count += 1
            if is_existed == 0:
                print('该学生不存在')
            else:
                print('删除成功！')
                print('正在返回上级界面')
                time.sleep(3)
                pyautogui.hotkey("Alt", "c")

    # 删除教师
    if object_num == 1:
        line_count = 0
        is_existed = 0
        file_data = ''
        name = input('请输入需要删除的教师信息：').strip()
        with open('tea_data.txt', 'r', encoding='utf-8') as f1:
            tea_info = f1.readlines()
            for tea in tea_info:
                if name == tea.strip().split(',')[0]:
                    del tea_info[line_count]
                    with open('tea_data.txt', 'w', encoding='utf-8') as f2:
                        f2.write(''.join(tea_info))
                    is_existed = 1
                else:
                    line_count += 1
            if is_existed == 0:
                print('该教师不存在')
            else:
                with open('cour_data.txt', 'r', encoding='utf-8') as f3:
                    cour_info = f3.readlines()
                    for cour in cour_info:
                        if name == cour.strip().split(',')[2]:
                            cour = cour.replace(name, '该教师正在卢比扬卡享受人生')
                        file_data += cour
                        with open('cour_data.txt', 'w', encoding='utf-8') as f4:
                            f4.write(file_data)
                    print('删除成功！')
                    print('正在返回上级界面')
                    time.sleep(3)
                    pyautogui.hotkey("Alt", "c")

    # 删除课程
    if object_num == 2:
        line_count = 0
        is_existed = 0
        name = input('请输入需要删除的课程名称：').strip()
        with open('cour_data.txt', 'r', encoding='utf-8') as f1:
            cour_info = f1.readlines()
            for cour in cour_info:
                if name == cour.strip().split(',')[0]:
                    del cour_info[line_count]
                    with open('cour_data.txt', 'w', encoding='utf-8') as f2:
                        f2.write(''.join(cour_info))
                    is_existed = 1
                else:
                    line_count += 1
            if is_existed == 0:
                print('该课程不存在')
            else:
                file_data = ''
                with open('stu_data.txt', 'r', encoding='utf-8') as f3:
                    stu_info = f3.readlines()
                    for stu in stu_info:
                        if name in stu.strip().split(',')[4:]:
                            stu = stu.replace(name, '该课程已被删除')
                        file_data += stu
                        with open('stu_data.txt', 'w', encoding='utf-8') as f4:
                            f4.write(file_data)
                with open('tea_data.txt', 'r', encoding='utf-8') as f5:
                    tea_info = f5.readlines()
                    tea_file_data = ''
                    for i in range(0, len(tea_info)):
                        if name in tea_info[i].strip().split(',')[4:]:
                            tea_info[i] = tea_info[i].replace(name, '该课程已被删除')
                    for i in range(0, len(tea_info)):
                        tea_file_data += tea_info[i]
                    with open('tea_data.txt', 'w', encoding='utf-8') as f6:
                        f6.write(tea_file_data)
                print('删除成功！')
                print('正在返回上级界面')
                time.sleep(3)
                pyautogui.hotkey("Alt", "c")


def select(object_num):
    pyautogui.hotkey("Alt", "c")
    print('某某大学信息查询界面'.center(50, '*'))
    if object_num == 0:
        stu_exist = 0
        with open('stu_data.txt', 'r', encoding='utf-8') as f1:
            with open('stu_score.txt', 'r', encoding='utf-8') as f2:
                stu_info = f1.readlines()
                score_info = f2.readlines()
                name = input("请输入需要查询的学生姓名：")
                for stu in stu_info:
                    if name == stu.strip().split(',')[0]:
                        print('您要查询的学生信息如下：')
                        print('姓名：' + stu.strip().split(',')[0] + '\t'
                            + '性别：' + stu.strip().split(',')[2] + '\t'
                            + '所属学部：' + stu.strip().split(',')[3] + '\t')
                        break
                for score in score_info:
                    if name == score.strip().split(',')[0]:
                        stu_exist = 1
                        print('该生所修课程及成绩如下：')
                        for i in range(len(score.strip().split(',')) - 1):
                            stu_cour_info = stu.strip().split(',')
                            score_data = score.strip().split(',')
                            print(stu_cour_info[i + 4] + ':' + score_data[i + 1])
                        break
                if stu_exist == 0:
                    print('该学生不存在')

    if object_num == 1:
        with open('tea_data.txt', 'r', encoding='utf-8') as f1:
            tea_info = f1.readlines()
            tea_exist = 0
            name = input("请输入需要查询的教师姓名：")
            for tea in tea_info:
                if name == tea.strip().split(',')[0]:
                    tea_exist = 1
                    print('您要查询的教师信息如下：')
                    print('姓名：' + tea.strip().split(',')[0] + '\t'
                        + '性别：' + tea.strip().split(',')[2] + '\t'
                        + '所属学部：' + tea.strip().split(',')[3] + '\t')
                    print('该教师所授课程如下：')
                    for i in range(len(tea.strip().split(',')) - 4):
                        tea_cour_info = tea.strip().split(',')
                        print(tea_cour_info[i + 4])
            if tea_exist == 0:
                print('该教师不存在')

    if object_num == 2:
        cour_exist = 0
        with open('cour_data.txt', 'r', encoding='utf-8') as f1:
            cour_info = f1.readlines()
            name = input("请输入需要查询的课程名称：")
            for cour in cour_info:
                if name == cour.strip().split(',')[0]:
                    cour_exist = 1
                    print('课程名称：' + cour.strip().split(',')[0] + '\t'
                        + '所属学部：' + cour.strip().split(',')[1] + '\t'
                        + '授课教师：' + cour.strip().split(',')[2] + '\t')
                    break
            if cour_exist == 0:
                print('该课程不存在')

    func_dic = {
        '0': '返回管理界面',
        '1': '继续查询信息',
    }

    managed_object_name_list = ['学生', '教师', '课程']

    print('{0}信息查询界面'.format(managed_object_name_list[object_num]).center(50, '*'))
    for k, v in func_dic.items():  # 打印待选功能
        print(k, v)
    print('某某大学教务管理系统'.center(50, '*'))

    # 选择功能
    func_num = input('是否继续查询:').strip()

    if func_num == '0':
        print('正在退出信息查询界面')
        time.sleep(3)
        pyautogui.hotkey("Alt", "c")
    elif func_num == '1':
        print('正在重新加载信息查询界面')
        time.sleep(3)
        pyautogui.hotkey("Alt", "c")
        select(object_num)
    else:
        print('暂无此功能')
        print('正在退出信息查询界面')
        time.sleep(3)
        pyautogui.hotkey("Alt", "c")
