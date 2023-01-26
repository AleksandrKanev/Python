from interface import action, view_contact
from logger import contact_input, save_contact, print_contact

def start():
    while (True):
        select = action()
        if select == 1:
            data = contact_input()
            save_contact(data)
        if select == 2:
            show = view_contact()
            print_contact(show)
        if select == 3:
            break
        