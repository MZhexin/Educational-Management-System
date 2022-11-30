'''
    类
'''

# 导入库以及本项目中的其他文件
import os
import time
import pyautogui

# 父类：用户
class User(object):
    def __init__(self, name, gender, type, dept):
        self.name = name          # 姓名信息
        self.gender = gender      # 性别信息
        self.type = type          # 身份信息
        self.dept = dept          # 学部信息
        self.dic = {}             # 注册信息

    # 密码修改 ————> change password
    def change_pass(self):
        print('某某大学用户密码更改界面'.center(50, '*'))
        file_list = ['stu_data.txt', 'tea_data.txt', 'admin_data.txt']  # 文件列表
        if self.type == 'student':  # 当对象的身份信息为student时
            file_num = 0  # 文件对应列表中的索引为0
        elif self.type == 'teacher':  # 当对象的身份信息为teacher时
            file_num = 1  # 文件对应列表中的索引为1
        else:  # 否则的话
            file_num = 2  # 文件对应列表中的索引为2
        old_passward = input("请输入您原来的密码：").strip()  # 输入旧密码
        file_data = "" # 用来改写文件信息的临时字符串
        with open(file_list[int(file_num)], 'r+', encoding='utf-8') as f1:  # 利用文件列表和文件索引打开对应的文件，打开方式是读r
            user_info = f1.readlines()  # 按行读取文件信息
        for user in user_info: # 迭代文件中的每一行
            if self.name == user.strip().split(',')[0]:  # 当文件中匹配到指定姓名后
                while old_passward != user.strip().split(',')[1]:  # 如果密码不匹配就让用户重新输入
                    print('密码错误，请重新输入')
                    old_passward = input("请输入您原来的密码：").strip()
                if old_passward == user.strip().split(',')[1]:  # 如果密码匹配
                    new_passward = input("请输入新的密码：")  # 输入新密码
                    user = user.replace(old_passward, new_passward)  # 替换新旧密码
                    # 因为这里需要修改文件信息，必须逐行把剩下的内容读取完并保存在临时字符串中，因此不能break跳出循环
            file_data += user  # 把新处理好的每一行数据保存在文件中
        with open(file_list[int(file_num)], 'w', encoding='utf-8') as f2: # 打开文件，方式是写w
            f2.write(file_data)  # 重写文件
        print('密码修改成功')
        print('正在返回上级界面')
        time.sleep(3)  # 界面暂停3秒
        pyautogui.hotkey("Alt", "c") # 清屏


# 子类：管理员
class Administrator(User):
    def __init__(self, name):  # 按需继承父类的属性
        super().__init__(name, "" ,'admin', "")

    def change_pass(self):  # 继承密码修改方法
        super().change_pass()


# 子类：学生
class Student(User):
    def __init__(self, name, gender, dept):  # 按需继承父类的属性
        super().__init__(name, gender, 'student', dept)

    def change_pass(self): # 继承密码修改方法
        super().change_pass()

    # 学籍自查方法
    def select_myself(self):
        pyautogui.hotkey("Alt", "c") # 清屏
        print('某某大学学生学籍自查界面'.center(50, '*'))
        with open('stu_data.txt', 'r', encoding='utf-8') as f1: # 打开文件，方法是读r
            stu_info = f1.readlines() # 按行读取文件信息
            for stu in stu_info:  # 迭代文件的每一行
                if self.name == stu.strip().split(',')[0]:  # 当匹配到自己的姓名时
                    # 打印学籍信息
                    print('您的学籍信息如下：')
                    print('姓名：' + stu.strip().split(',')[0] + '\t'
                          + '性别：' + stu.strip().split(',')[2] + '\t'
                          + '所属学部：' + stu.strip().split(',')[3] + '\t')
                    break # 这里不需要修改文件信息，读取到就可以直接跳出循环了
        # 返回上级界面的操作
        if_return = input('按0和回车返回上级界面')
        if if_return == '0':
            pyautogui.hotkey("Alt", "c") # 清屏
        else: # 若2分钟不操作，停顿3秒后自动返回上级界面
            time.sleep(120)
            print('长时间不操作，正在返回上级界面')
            time.sleep(3)

    # 成绩自查方法
    def select_my_score(self):
        pyautogui.hotkey("Alt", "c") # 清屏
        print('某某大学学生成绩查询界面'.center(50, '*'))
        with open('stu_data.txt', 'r', encoding='utf-8') as f1:  # 打开学生信息文件以获取课程名称
            with open('stu_score.txt', 'r', encoding='utf-8') as f2:  # 打开学生成绩文件以获取学生成绩
                stu_info = f1.readlines()  # 按行读取
                score_info = f2.readlines() # 按行读取
                for stu in stu_info: # 逐行迭代
                    if self.name == stu.strip().split(',')[0]:
                        stu_cour_info = stu.strip().split(',')  # 将学籍信息保存入stu_cour_info
                        break # 退出循环
                for score in score_info: # 逐行迭代
                    if self.name == score.strip().split(',')[0]:  # 匹配到自己的名字后
                        score_data = score.strip().split(',')  # 将成绩信息保存入stu_cour_info
                        print('您所修的课程及成绩如下：') # 开始打印成绩
                        for i in range(len(score.strip().split(',')) - 1): # 成绩文件中，去掉姓名之外，剩下的元素个数就是自己选修的学科数目
                            print(stu_cour_info[i + 4] + ':' + score_data[i + 1])  # 通过索引，依次打印所修课程与成绩
                        break  # 退出循环
        # 返回上级界面
        if_return = input('按0和回车返回上级界面')
        if if_return == '0':
            pyautogui.hotkey("Alt", "c")
        else:  # 若2分钟不操作，停顿3秒后自动返回上级界面
            time.sleep(120)
            print('长时间不操作，正在返回上级界面')
            time.sleep(3)

# 子类：教师
class Teacher(User):
    def __init__(self, name, gender, dept): # 按需继承父类的属性
        super().__init__(name, gender, 'teacher', dept)

    def change_pass(self): # 继承密码修改方法
        super().change_pass()

    # 教师信息自查
    def select_myself(self):
        pyautogui.hotkey("Alt", "c")  # 清屏
        print('某某大学教师信息自查界面'.center(50, '*'))
        with open('tea_data.txt', 'r', encoding='utf-8') as f1:  # 打开文件，方法是读r
            tea_info = f1.readlines()  # 按行读取文件信息
            for tea in tea_info:  # 迭代文件的每一行
                if self.name == tea.strip().split(',')[0]:  # 当匹配到自己的姓名时
                    tea_cour_info = tea.strip().split(',')
                    # 打印学籍信息
                    print('您的学籍信息如下：')
                    print('姓名：' + tea.strip().split(',')[0] + '\t'
                          + '性别：' + tea.strip().split(',')[2] + '\t'
                          + '所属学部：' + tea.strip().split(',')[3] + '\t')
                    print('该教师所授课程如下：')
                    for i in range(len(tea.strip().split(',')) - 4):
                        print(tea_cour_info[i + 4])
                    break  # 这里不需要修改文件信息，读取到就可以直接跳出循环了
        # 返回上级界面的操作
        if_return = input('按0和回车返回上级界面')
        if if_return == '0':
            pyautogui.hotkey("Alt", "c")  # 清屏
        else:  # 若2分钟不操作，停顿3秒后自动返回上级界面
            time.sleep(120)
            print('长时间不操作，正在返回上级界面')
            time.sleep(3)

# 单独一个新的类：课程
class Course(object):
    def __init__(self, name, dept, teacher):
        self.name = name
        self.dept = dept
        self.teacher = teacher
