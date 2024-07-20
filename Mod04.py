def execute():
    return menu_options()

def menu_options():
    while True:
        bar = {"1":"https://www.drudgereport.com",
               "2":"https://www.nytimes.com",
               "3":"https://www.nasa.gov"
               }
        print(
            """
Menu of Options
---------------
1.  DRUDGE
2.  NYT
3.  NASA
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
                    import webbrowser
                    webbrowser.open(v)
        break

execute()