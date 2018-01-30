from . import add
from . import show_menu
import time


name_list = []
def del_info():
    del_item = input('请输入要删除的学生姓名：')
    n = 0
    print('+' + '-' * 7 + '以下为删除掉的信息，不可找回' + '-' * 7 + '+')
    print('+' + ' ' * 4 + 'Name' + ' ' * 4 + '|' + ' ' * 4 + 'Age' + ' ' * 4 + '|' + ' ' * 4 + 'Grade' + ' ' * 4 + '+')
    for info in add.student_info:
        i = info['Name']
        name_list.append(i)
        if del_item == i :
            print('+' + info['Name'].center(12) + '|' + info['Age'].center(11) + '|' + info['Grade'].center(13) + '+')
            n += 1
            name_index = add.student_info.index(info)
            add.student_info.pop(name_index)
    a = input('已删除完成，共删除%d条信息，按<回车>返回'%n)
    show_menu.show_menu()
