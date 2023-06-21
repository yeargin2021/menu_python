def menu_options():
    while True:
        print(
            """
Menu of Options
---------------
1.  Hello
2.  Goodbye
            
            """
        )
        foo =  input("Enter choice: ")
        if foo == "2":
            print("\n\nHappy trails!\n\n")
        elif foo == "1":
            print("\n\nHello world.\n\n")
        else:
            print("\n\nWRONG...try again!\n")
            menu_options()
        break

menu_options()