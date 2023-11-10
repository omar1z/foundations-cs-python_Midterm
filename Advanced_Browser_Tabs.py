dictionary_list_Tab = []  # this list is to maintain each tab in a dictionary

order_count = []  # this list for indexes in case of closing tabs




def main():
    print()
    # Greeting
    print("Hello dear, you are welcome !! ;)")
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
        for i in range(len(dictionary_list_Tab)):  # this loop is for checking if tab index exist or not to append it
            if i in order_count:
                continue
            else:
                order_count.append(i)
        print(order_count)
        while True:
            try:
                index = int(input("Enter index of the page you want to close : "))
                if index in order_count:  # order_count is the number of dictionaries in the list
                    break
            except ValueError:
                print("Invalid input. Please enter a valid tab index")

        print(closeTab(index))


def openTab(dic_list, title, url):
    dic = {'title': title, 'url': url}
    dic_list.append(dic)
    return dic_list


def closeTab(index):
    return dictionary_list_Tab


while True:
    main()
