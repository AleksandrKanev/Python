from interface import action
from logger_master import print_rating, vary_journal, lesson

def start():
    while (True):
        select = action()
        if select == 1:
            s_name = input('Введите фамилию ученика: ')
            print()
            vary_journal(s_name)
        if select == 2:
            s_name = input('Введите фамилию ученика: ')
            print()
            print_rating(s_name)
        if select == 3:
            break
        