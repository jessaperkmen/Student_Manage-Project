#-*— coding：utf-8 -*-
from module import show_menu
from module import add
from module import all
from module import find
from module import del_name
from module import sort_all
import sys
import time

print('学生管理系统启动中...')
time.sleep(2)
print('您好，欢迎来到本系统')
operator = {'1':all.all_print,'2':find.find_info,'3':add.add_info,'4':del_name.del_info,'5':sort_all.sort_student,'6':sys.exit}
def start():
    while True:
        show_menu.show_menu()
        try:
            a = input('请选择操作,输入序号即可:')
            ope = operator[a]
            ope()
        except KeyError:
            print('您的输入有误！请重新输入')
            time.sleep(1)
            start()
start()








