import time

student_info = []
def add_info():
    global student_info
    print('开始录入学生信息...')
    info_perpare ={}
    info_perpare['Name'] = input('请输入学生姓名：')
    info_perpare['Age'] = input('请输入学生年龄：')
    info_perpare['Grade'] = input('请输入学生成绩：')
    print('录入结束...')
    print('您录入的信息为：')
    print('姓名:%(Name)s,年龄:%(Age)s,成绩:%(Grade)s'%info_perpare)
    time.sleep(1)
    i = input('请确认是否正确：y/n')
    if i == 'y':
        student_info.append(info_perpare)
    elif i =='n':
        print('已取消，重新录入！')
        time.sleep(1)
        add_info()
    else:
        print('您的输入有误，为避免信息错误，录入系统已重启，请重新录入。')
        time.sleep(1)
        add_info()





