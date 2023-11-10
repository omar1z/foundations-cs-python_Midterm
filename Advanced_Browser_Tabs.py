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
        print(openTab(dictionary_list_Tab, title, url))

    elif user_input == 2:
        variable = 1
        index = input("enter index to delete the page : ")
        print(dictionary_list_Tab)
        if index == "":
            variable = 0
            print(closeTab(index, variable))
        else:
            try:
                index = int(index)
                if index > len(dictionary_list_Tab):
                    print("This Tab is not found")
                else:
                    for i in range(len(dictionary_list_Tab)):
                        if i == index:
                            print(closeTab(index, variable))
                            break
            except ValueError:
                print("Invalid input. Please enter a valid tab index")


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

    return dictionary_list_Tab, "those are the tabs remained"


while True:
    main()
