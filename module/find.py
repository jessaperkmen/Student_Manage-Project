from . import add
from . import show_menu
import time

name_list = []
def  find_info():
    find_item = input('请输入要查找的学生姓名：')
    n = 0
    print('+' + ' ' * 4 + 'Name' + ' ' * 4 + '|' + ' ' * 4 + 'Age' + ' ' * 4 + '|' + ' ' * 4 + 'Grade' + ' ' * 4 + '+')
    for info in add.student_info:
        i = info['Name']
        name_list.append(i)
        if find_item == i :
            print('+' + info['Name'].center(12) + '|' + info['Age'].center(11) + '|' + info['Grade'].center(13) + '+')
            n += 1
    a = input('已查询完成，共%d条信息，按<回车>返回'%n)
    show_menu.show_menu()

