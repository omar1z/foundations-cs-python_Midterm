import requests as re  # to access html content from browser

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
    # num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Saving the choices number in a list
    while True:
        try:  # Try-except notation (just the idea) https://www.w3schools.com/python/python_try_except.asp
            user_input = int(input("Enter your choice please : "))
            # if user_input in num_list:
            if 0 < user_input < 10:
                break
        except ValueError:
            print("Invalid input. Please enter a valid choice (between 1-9) : ")

    if user_input == 1:
        tabInfo(dictionary_list_Tab, user_input)

    elif user_input == 2:
        choosingIndex(2)
        # calling function of closeTab from inside choosing index

    elif user_input == 3:
        choosingIndex(3)
        # calling function of closeTab from inside choosing index

    elif user_input == 4:
        printTitles()

    elif user_input == 5:
        choosingIndex(5)


def tabInfo(dic_list, user_input):  # getting title and url (using it in part 1 and 5)
    title = input("Enter Tab Title : ")
    url = input("Enter a url ( make sure to start with https:// or http:// ) : ")
    url_verification = "https://"
    url_verification1 = "http://"
    if user_input == 1:
        if url_verification in url:
            print(openTab(dic_list, title, url))
        elif url_verification1 in url:
            print(openTab(dic_list, title, url))
        else:
            print("This is not a URL, try again")
    else:
        if url_verification in url:
            print(openTabN(dic_list, title, url))
        elif url_verification1 in url:
            print(openTabN(dic_list, title, url))
        else:
            print("This is not a URL, try again")


def openTab(dic_list, title, url):  # function of part 1
    dic = {'title': title, 'url': url}
    dic_list.append(dic)
    return dic_list


def openTabN(dic_list, title, url):
    dic = {'title': title, 'url': url}
    dic_list['nested'].append(dic)
    return dic_list


def closeTab(index, variable):  # function of part 2
    if variable == 1:
        dictionary_list_Tab.pop(index)
    else:
        if len(dictionary_list_Tab) != 0:
            dictionary_list_Tab.pop(-1)
        else:
            print("No TABS to be deleted")

    return dictionary_list_Tab, "those are the tabs remaining"


def getContent(index, variable):  # function of part 3
    if variable == 1:
        response = re.get(dictionary_list_Tab[index]['url'])
        html = response.text
        return html
    else:
        if len(dictionary_list_Tab) != 0:
            response = re.get(dictionary_list_Tab[-1]['url'])
            html = response.text
            return html
        else:
            return "No TABS to show content !"


def printTitles():
    for i in range(len(dictionary_list_Tab)):
        print(dictionary_list_Tab[i]['title'])


def createNesTab(index, variable):
    if len(dictionary_list_Tab[index]) <= 2:
        dictionary_list_Tab[index]['nested'] = []
    if variable == 1:
        tabInfo(dictionary_list_Tab[index], 5)
    else:
        if len(dictionary_list_Tab) != 0:
            tabInfo(dictionary_list_Tab[-1], 5)
        else:
            return "No TABS to open nested one inside !"


def choosingIndex(nbr):
    print(dictionary_list_Tab)
    variable = 1  # variable here is to determine if the input is empty or not
    if nbr == 2:
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

    elif nbr == 3:
        index = input("Enter Tab index you want to get content !(starting from 0->)! : ")
        if index == "":
            variable = 0
            print(getContent(index, variable))
        else:
            try:
                index = int(index)
                if index > len(dictionary_list_Tab):
                    print("This Tab is not found")
                else:
                    for i in range(len(dictionary_list_Tab)):
                        if i == index:
                            print(getContent(index, variable))
                            break
            except ValueError:
                print("Invalid input. Please enter a valid tab index")

    else:
        index = input("Enter Tab index you want to add nested tab !(starting from 0->)! : ")
        if index == "":
            variable = 0
            print(createNesTab(index, variable))
        else:
            try:
                index = int(index)
                if index > len(dictionary_list_Tab):
                    print("This Tab is not found")
                else:
                    for i in range(len(dictionary_list_Tab)):
                        if i == index:
                            print(createNesTab(index, variable))
                            break
            except ValueError:
                print("Invalid input. Please enter a valid tab index")


while True:
    main()
