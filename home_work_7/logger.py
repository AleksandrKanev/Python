def contact_input():
    fam = input('Введите Фамилию: ')
    nam = input('Введите Имя: ')
    phone = input('Введите номер телфона: ')
    commit = input('Введите Примечание: ')
    print()
    data = [fam, nam, phone, commit]
    return data


def save_contact(data):
    file = 'home_work_7\contact_colum.txt'
    with open(file, 'a') as c:
        c.write(
            f'Фамилия: {data[0]}; Имя: {data[1]}; Телефон: {data[2]}; Описание: {data[3]} \n\n')

    file = 'home_work_7\contact_str.txt'
    with open(file, 'a') as c:
        c.write(
            f'Фамилия: {data[0]}\n Имя: {data[1]}\n  Телефон: {data[2]}\n Описание: {data[3]} \n\n')


def print_contact(choise):
    if choise == 1:
        with open('home_work_7\contact_colum.txt', 'r') as file:
            for i in file:
                print(i, end='')
    if choise == 2:
        with open('home_work_7\contact_str.txt', 'r') as file:
            for i in file:
                print(i, end='')