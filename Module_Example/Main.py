import Menu_Text
from Menu_Data import *

def execute():
    return menu_options()

def menu_options():
    while True:
        Menu_Text.menu_text()
        foo =  input("Enter choice: ")

        if foo not in bar:
            print("\n\nWRONG...try again!\n")
            execute()
        else:
            for k, v in bar.items():
                if foo != k:
                    pass
                elif foo == k:
                    print(v)
        break

execute()