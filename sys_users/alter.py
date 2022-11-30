
import time
import pyautogui

def stu_alter(func_num):
    pyautogui.hotkey("Alt", "c")
    print('某某大学信息修改界面'.center(50, '*'))
    with open('stu_data.txt', 'r', encoding='utf-8') as f1:
        stu_info = f1.readlines()
        # 改名字
        if func_num == '1':
            file_data1 = ''
            file_data2 = ''
            name = input('请输入需要修改姓名的学生的姓名：')
            try:
                for stu in stu_info:
                    if name == stu.strip().split(',')[0]:
                        new_name = input('请输入该学生的新名字：')
                        stu = stu.replace(stu.strip().split(',')[0], new_name)
                    file_data1 += stu
                with open('stu_score.txt', 'r', encoding='utf-8') as fs1:
                    score_info = fs1.readlines()
                    for score in score_info:
                        if name == score.strip().split(',')[0]:
                            score = score.replace(name, new_name)
                        file_data2 += score
                with open('stu_data.txt', 'w', encoding='utf-8') as f2:
                    f2.write(file_data1)
                with open('stu_score.txt', 'w', encoding='utf-8') as fs2:
                    fs2.write(file_data2)
                print('修改成功！')
            except:
                print('未知错误')

        # 变性手术
        if func_num == '2':
            file_data = ''
            name = input('请输入需要修改性别的学生的姓名：')
            try:
                for stu in stu_info:
                    if name == stu.strip().split(',')[0]:
                            new_gender = input('请输入该学生的新性别：')
                            stu = stu.replace(stu.strip().split(',')[2], new_gender)
                    file_data += stu
                with open('stu_data.txt', 'w', encoding='utf-8') as f2:
                    f2.write(file_data)
                print('修改成功！')
            except:
                print('该学生不存在')


        # 转专业
        if func_num == '3':
            file_data = ''
            name = input('请输入需要修改学部的学生的姓名：')
            try:
                for stu in stu_info:
                    if name == stu.strip().split(',')[0]:
                        new_dept = input('请输入该学生的新学部：')
                        stu = stu.replace(stu.strip().split(',')[3], new_dept)
                    file_data += stu
                with open('stu_data.txt', 'w', encoding='utf-8') as f2:
                    f2.write(file_data)
                print('修改成功！')
            except:
                print('该学生不存在')

        # 换课
        if func_num == '4':
            file_data = ''
            file_data2 = ''
            cour_exist = 0
            i = 0
            name = input('请输入需要修改课程的学生的姓名：')
            try:
                for stu in stu_info:
                    if name == stu.strip().split(',')[0]:
                        while cour_exist == 0:
                            old_cour = input('请输入该学生的旧课程：')
                            if old_cour in stu.strip().split(','):
                                new_cour = input('请输入该学生的新课程：')
                                stu = stu.replace(old_cour, new_cour)
                                i = stu.strip().split(',').index(new_cour) - 3
                                cour_exist = 1
                                break
                            else:
                                print('该学生未选修该课程')
                    file_data += stu
                with open('stu_score.txt', 'r', encoding='utf-8') as fs:
                    score_info = fs.readlines()
                    for score in score_info:
                        if name == score.strip().split(',')[0]:
                            score = score.replace(score.strip().split(',')[i], '此门课程暂无成绩')
                        file_data2 += score
                with open('stu_data.txt', 'w', encoding='utf-8') as f2:
                    f2.write(file_data)
                with open('stu_score.txt', 'w', encoding='utf-8') as fs2:
                    fs2.write(file_data2)
                print('修改成功！')
            except:
                print('未知错误')

        # 改成绩
        if func_num == '5':
            file_data = ''
            cour_exist = 0
            name = input('请输入需要修改成绩的学生的姓名：')
            for stu in stu_info:
                if name == stu.strip().split(',')[0]:
                    while cour_exist == 0:
                        cour_name = input('请输入该学生需要修改成绩的课程名称：')
                        if cour_name in stu.strip().split(','):
                            i = stu.strip().split(',').index(cour_name) - 3
                            cour_exist = 1
                            break
                        else:
                            print("该学生未选修该课程")
            with open('stu_score.txt', 'r', encoding='utf-8') as fs:
                score_info = fs.readlines()
                for score in score_info:
                    if name == score.strip().split(',')[0]:
                        new_score = input('请输入该学生该课程的新成绩：')
                        score = score.replace(score.strip().split(',')[i], new_score)
                    file_data += score
            with open('stu_score.txt', 'w', encoding='utf-8') as f2:
                f2.write(file_data)
            print('修改成功！')

    print('正在返回上级界面')
    time.sleep(3)
    pyautogui.hotkey("Alt", "c")

def tea_alter(func_num):
    pyautogui.hotkey("Alt", "c")
    print('某某大学信息查询界面'.center(50, '*'))
    with open('tea_data.txt', 'r', encoding='utf-8') as f1:
        tea_info = f1.readlines()
        # 改名字
        if func_num == '1':
            with open('cour_data.txt', 'r', encoding='utf-8') as f2:
                cour_info = f2.readlines()
                file_data1 = ''
                file_data2 = ''
                tea_exist = 0
                name = input('请输入需要修改姓名的教师的姓名：')
                try:
                    for tea in tea_info:
                         if name == tea.strip().split(',')[0]:
                            tea_exist = 1
                            new_name = input('请输入该教师的新名字：')
                            tea = tea.replace(name, new_name)
                         file_data1 += tea
                    for cour in cour_info:
                        if name == cour.strip().split(',')[2]:
                            cour = cour.replace(name, new_name)
                        file_data2 += cour
                    with open('tea_data.txt', 'w', encoding='utf-8') as f3:
                        f3.write(file_data1)
                    with open('cour_data.txt', 'w', encoding='utf-8') as f4:
                        f4.write(file_data2)
                    print('修改成功！')
                except:
                    print('该教师不存在')


        # 变性手术
        if func_num == '2':
            file_data = ''
            name = input('请输入需要修改性别的教师的姓名：')
            try:
                for tea in tea_info:
                    if name == tea.strip().split(',')[0]:
                        new_gender = input('请输入该教师的新性别：')
                        tea = tea.replace(tea.strip().split(',')[2], new_gender)
                    file_data += tea
                with open('tea_data.txt', 'w', encoding='utf-8') as f2:
                    f2.write(file_data)
                print('修改成功！')
            except:
                print('该教师不存在')


        # 转专业
        if func_num == '3':
            file_data = ''
            name = input('请输入需要修改学部的教师的姓名：')
            try:
                for tea in tea_info:
                    if name == tea.strip().split(',')[0]:
                        new_dept = input('请输入该教师的新学部：')
                        tea = tea.replace(tea.strip().split(',')[3], new_dept)
                    file_data += tea
                with open('tea_data.txt', 'w', encoding='utf-8') as f2:
                    f2.write(file_data)
                print('修改成功！')
            except:
                print('该教师不存在')


        # 换课
        if func_num == '4':
            change_success = 1
            with open('cour_data.txt', 'r', encoding='utf-8') as f2:
                cour_info = f2.readlines()
                file_data1 = ''
                file_data2 = ''
                teacher_exist = 0
                cour_exist = 0
                tea_exist = 0
                name = input('请输入需要修改课程的教师的姓名：')
                for tea in tea_info:
                    if name == tea.strip().split(',')[0]:
                        teacher_exist += 1
                if teacher_exist == 0:
                    print('教师不存在')
                    change_success = 0
                for tea in tea_info:
                    if name == tea.strip().split(',')[0]:
                        while cour_exist == 0:
                            old_cour = input('请输入该教师教授的旧课程：')
                            if old_cour in tea.strip().split(',')[4:]:
                                new_cour = input('请输入该教师教授的新课程：')
                                tea = tea.replace(old_cour, new_cour)
                                for cour in cour_info:
                                    if old_cour == cour.strip().split(',')[0]:
                                        while tea_exist == 0:
                                            if name in cour.strip().split(',')[2:]:
                                                cour = cour.replace(',' + name, '')
                                                tea_exist = 1
                                                break
                                            else:
                                                print('教师与课程不匹配')
                                    elif new_cour == cour.strip().split(',')[0]:
                                        cour = cour.strip() + ',' + name + '\n'
                                    file_data2 = file_data2 + cour
                                cour_exist = 1
                            else:
                                print('教师与课程不匹配')
                    file_data1 = file_data1 + tea
            with open('tea_data.txt', 'w', encoding='utf-8') as f3:
                f3.write(file_data1)
            with open('cour_data.txt', 'w', encoding='utf-8') as f4:
                f4.write(file_data2)
            if change_success == 1:
                print('修改成功！')
    print('正在返回上级界面')
    time.sleep(3)
    pyautogui.hotkey("Alt", "c")

def cour_alter(func_num):
    pyautogui.hotkey("Alt", "c")
    print('某某大学信息查询界面'.center(50, '*'))
    # 改名字
    with open('cour_data.txt', 'r', encoding='utf-8') as f1:
        cour_info = f1.readlines()
        if func_num == '1':
            with open('tea_data.txt', 'r', encoding='utf-8') as f2:
                with open('stu_data.txt', 'r', encoding='utf-8') as f3:
                    tea_info = f2.readlines()
                    stu_info = f3.readlines()
                    file_data1 = ''
                    file_data2 = ''
                    file_data3 = ''
                    name = input('请输入需要修改名称的课程的名称：')
                    try:
                        for cour in cour_info:
                            if name == cour.strip().split(',')[0]:
                                new_name = input('请输入该课程的新名称：')
                                cour = cour.replace(name, new_name)
                            file_data1 += cour
                        for tea in tea_info:
                            if name in tea.strip().split(',')[4:]:
                                tea = tea.replace(name, new_name)
                            file_data2 += tea
                        for stu in stu_info:
                            if name in stu.strip().split(',')[4:]:
                                stu = stu.replace(name, new_name)
                            file_data3 += stu
                        with open('cour_data.txt', 'w', encoding='utf-8') as f3:
                            f3.write(file_data1)
                        with open('tea_data.txt', 'w', encoding='utf-8') as f4:
                            f4.write(file_data2)
                        with open('stu_data.txt', 'w', encoding='utf-8') as f5:
                            f5.write(file_data3)
                        print('修改成功！')
                    except:
                        print('该课程不存在')


        # 转专业
    with open('cour_data.txt', 'r', encoding='utf-8') as f1:
        cour_info = f1.readlines()
        if func_num == '2':
            file_data = ''
            name = input('请输入需要修改学部的教师的姓名：')
            try:
                for cour in cour_info:
                    if name == cour.strip().split(',')[0]:
                        new_dept = input('请输入该课程所属的新学部：')
                        cour = cour.replace(cour.strip().split(',')[3], new_dept)
                    file_data += cour
                with open('cour_data.txt', 'w', encoding='utf-8') as f2:
                    f2.write(file_data)
                print('修改成功！')
            except:
                print('该课程不存在')


        # 更换授课教师
    with open('cour_data.txt', 'r', encoding='utf-8') as f1:
        cour_info = f1.readlines()
        if func_num == '3':
            with open('tea_data.txt', 'r', encoding='utf-8') as f2:
                tea_info = f2.readlines()
                file_data1 = ''
                file_data2 = ''
                tea_exist = 0
                course_exist = 0
                change_success = 1
                name = input('请输入需要修改授课教师的课程名称：')
                for cour in cour_info:
                    if name == cour.strip().split(',')[0]:
                        course_exist += 1
                if course_exist == 0:
                    print('课程不存在')
                    change_success = 0
                for cour in cour_info:
                    if name == cour.strip().split(',')[0]:
                        while tea_exist == 0:
                            old_tea = input('请输入该课程需要替换的授课教师姓名：')
                            if old_tea in cour.strip().split(',')[2:]:
                                new_tea = input('请输入该课程的新授课教师姓名：')
                                cour = cour.replace(old_tea, new_tea)
                                for tea in tea_info:
                                    if old_tea == tea.strip().split(',')[0]:
                                        while tea_exist == 0:
                                            if name in tea.strip().split(',')[4:]:
                                                tea = tea.replace(',' + name, '')
                                                tea_exist = 1
                                                break
                                            else:
                                                print('教师与课程不匹配')
                                                change_success = 0
                                    elif new_tea == tea.strip().split(',')[0]:
                                        tea = tea.replace('\n', ',' + name + '\n')
                                    file_data2 = file_data2 + tea
                                tea_exist = 1
                            else:
                                print('信息不匹配')
                                change_success = 0
                    file_data1 += cour
            with open('cour_data.txt', 'w', encoding='utf-8') as f3:
                f3.write(file_data1)
            with open('tea_data.txt', 'w', encoding='utf-8') as f4:
                f4.write(file_data2)
            if change_success == 1:
                print('修改成功！')

    print('正在返回上级界面')
    time.sleep(3)
    pyautogui.hotkey("Alt", "c")
