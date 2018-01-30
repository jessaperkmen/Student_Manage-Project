from . import add
from . import show_menu


def sort_student():
    student_info_sort = add.student_info[:]
    for i in student_info_sort:
        i['Age'] = int(i['Age'])
        i['Grade'] = int(i['Grade'])
    a = input('请选择排序的序列，回复数字即可：1.年龄；2.成绩')
    if a == '1':
        b = input('请选择排序方向，回复数字即可：1.升序；2.降序')
        if b == '1':
            student_info_sort.sort(key=lambda student : student['Age'])
        elif b == '2':
            student_info_sort.sort(key=lambda student: student['Age'],reverse=True)
        else:
            print('您输入的数字有误，请重新输入')
            sort_student()
    elif a == '2':
        b = input('请选择排序方向，回复数字即可：1.升序；2.降序')
        if b == '1':
            student_info_sort.sort(key=lambda student : student['Grade'])
        elif b == '2':
            student_info_sort.sort(key=lambda student: student['Grade'],reverse=True)
        else:
            print('您输入的数字有误，请重新输入')
            sort_student()
    else:
        print('您输入的数字有误，请重新输入')
        sort_student()
    for i in student_info_sort:
        i['Age'] = str(i['Age'])
        i['Grade'] = str(i['Grade'])
    print('+' + '-' * 38 + '+')
    print('+' + ' ' * 4 + 'Name' + ' ' * 4 + '|' + ' ' * 4 + 'Age' + ' ' * 4 + '|' + ' ' * 4 + 'Grade' + ' ' * 4 + '+')
    for i in student_info_sort:
        print('+' + i['Name'].center(12) + '|' + i['Age'].center(11) + '|' + i['Grade'].center(13) + '+')
    a = input('已显示完成，按<回车>返回')
    show_menu.show_menu()
