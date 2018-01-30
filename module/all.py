from . import add
from . import show_menu
import time

def all_print(student_info = add.student_info):
    print('+'+'-'*38+'+')
    print('+'+' '*4+'Name'+' '*4+'|'+' '*4+'Age'+' '*4+'|'+' '*4+'Grade'+' '*4+'+')
    for i in student_info:
        print('+'+i['Name'].center(12)+'|'+i['Age'].center(11)+'|'+i['Grade'].center(13)+'+')
    a = input('已全部显示，按<回车>返回')
    show_menu.show_menu()

