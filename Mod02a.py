def execute():
    return menu_options()

def menu_options():
    while True:
        bar = {"1":"\n\nHello world.\n\n", 
               "2":"\n\nHappy trails!\n\n", 
               "3":"\n\n...Atlanta and Boston.\n\n"
               }
        print(
            """
Menu of Options
---------------
1.  Hello
2.  Goodbye
3.  My favorite baseball teams are...
            """
        )
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