dictionary_list_Tab = []  # this list is to maintain each tab in a dictionary


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
        print(OpenTab(dictionary_list_Tab, title, url))


def OpenTab(dic_list, title, url):
    dic = {'title': title, 'url': url}
    dic_list.append(dic)
    return dic_list


while True:
    main()
