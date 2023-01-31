lesson = 'Мат- ;Инф- ;Рус- ;Физик- ;Физра- '

def read():
    with open("home_work_8\journal.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
    z =[]    
    for item in data:
        z.append(item.replace('\n', ''))
    data = list(filter(lambda x: not x == '', z))
    return data


# s_name = input('Введите фамилию ученика: ')

def student_input():
    name = input('Ученик не найден! Введите Фамилию и Имя ученика: ')
    with open("home_work_8\journal.txt", "a", encoding="utf-8") as f:
        f.write(f'{name}:{lesson}')

def write_jornal(data):
    with open("home_work_8\journal.txt", "w", encoding="utf-8") as f:
        for lis in data:
            f.write(lis + '\n')


def vary_journal(s_name):
    flag = 0
    while flag == 0:
        data = read()
        if data == []:
            name_new = input('Журнал пуст! Введите Фамилию и Имя ученика: ')
            data = [f'{name_new}:{lesson}']
        for i in range(len(data)):
            if s_name in data[i]:
                flag = 1
                d = ''.join(data[i].split(':')[-1:]).split(';')
                break
        if flag == 1:
            les = input(f'{d}\nНапишите название предмета из списка: ')
            rat = input('Какую оценку выставить?: ')
            for j in range(len(d)):
                if les in d[j]:
                    d[j] += f'{rat} '
                    break
            d = ''.join(data[i].split(':')[:-1]) +':'+ ';'.join(d)
            data[i] = d
            write_jornal(data)
        elif flag==0: student_input()

def print_rating(s_name):
    data = read()
    if data == []:
        print('Журнал пуст! Обратитесь к учителю')
    else:
        flag = 0
        for i in range(len(data)):
            if s_name in data[i]:
               print(data[i])
               flag = 1
               break            
        if flag == 0:
            print('Ученик не найден! Обратитесь к учителю')
    print()
