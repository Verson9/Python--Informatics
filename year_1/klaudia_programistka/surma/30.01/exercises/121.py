def display_names_list():
    for i in range(len(names_list)):
        print(i+1, ".",names_list[i])


def add_name():
    name_to_add = input("Input name to add:\n")
    names_list.append(name_to_add)
    display_user_options()


def change_name():
    display_names_list()
    num_of_name_to_change = int(input("Which you want to change:\n")) - 1
    new_name = input("Input new name:\n")
    names_list[num_of_name_to_change] = new_name
    display_names_list()
    display_user_options()


def display_names():
    display_names_list()
    display_user_options()


def delete_name():
    display_names_list()
    num_of_name_to_delete = int(input("Which you want to delete:\n"))
    names_list.remove(num_of_name_to_delete)
    display_names_list()
    display_user_options()


def user_choice_options():
    user_choice = int(input("Yor choice:"))
    if user_choice == 1:
        add_name()
    elif user_choice == 2:
        change_name()
    elif user_choice == 3:
        display_names()
    elif user_choice == 4:
        delete_name()
    elif user_choice == 5:
        return
    else:
        print("Bad input")
        display_user_options()


def display_user_options():
    print("---DISPLAY MENU---:\n"
          "1.Add name\n"
          "2.Change name\n"
          "3.Display names\n"
          "4.Delete name\n"
          "5.Quit")
    user_choice_options()


def main():
    display_user_options()


names_list = []
main()