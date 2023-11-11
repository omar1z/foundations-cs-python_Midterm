dictionary_list_Tab = []  # this list is to maintain each tab in a dictionary


def main():
    print()
    # Greeting
    print("Hello, you are welcome !! ;)")
    print()
    # Menu(user interface)
    print("1.Open Tab")
    print("2.Close Tab")
    print("3.Switch Tab")
    print("4.Display All Tabs")
    print("5.Open Nested Tab")
    print("6.Clear All Tabs")
    print("7.Save Tabs")
    print("8.Import Tabs")
    print("9.Exit")

    print()
    # User input validation
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Saving the choices number in a list
    while True:
        try:  # Try-except notation (just the idea) https://www.w3schools.com/python/python_try_except.asp
            user_input = int(input("Enter your choice please : "))
            if user_input in num_list:
                break
        except ValueError:
            print("Invalid input. Please enter a valid choice (between 1-9) : ")

    if user_input == 1:
        title = input("Enter Tab Title : ")
        url = input("Enter a url : ")
        url_verification = "https://www."
        url_verification1 = "http://www."
        if url_verification in url:
            print(openTab(dictionary_list_Tab, title, url))
        elif url_verification1 in url:
            print(openTab(dictionary_list_Tab, title, url))
        else:
            print("This is not a URL, try again")

    elif user_input == 2:
        print(dictionary_list_Tab)
        variable = 1    # variable here is to determine if the input is empty or not
        index = input("Enter Tab index to close the page !(starting from 0->)! : ")
        if index == "":
            variable = 0
            print(closeTab(index, variable))
            # first I took the input as a normal input from the user just to check if it's empty
        else:
            try:
                index = int(index)  # int() transforms the type of the object to integer in opposite to str()
                # (information from university)
                # the input is now of integer type to search the indexes
                if index > len(dictionary_list_Tab):
                    print("This Tab is not found")
                else:
                    for i in range(len(dictionary_list_Tab)):
                        if i == index:
                            print(closeTab(index, variable))
                            break
            except ValueError:
                print("Invalid input. Please enter a valid tab index")
            # this part might seem a little creepy, but I tried not to use Google or other sources of information


def openTab(dic_list, title, url):
    dic = {'title': title, 'url': url}
    dic_list.append(dic)
    return dic_list


def closeTab(index, variable):
    if variable == 1:
        dictionary_list_Tab.pop(index)
    else:
        if len(dictionary_list_Tab) != 0:
            dictionary_list_Tab.pop(-1)
        else:
            print("No TABS to be deleted")

    return dictionary_list_Tab, "those are the tabs remaining"


while True:
    main()
