import random


def display_options():
    print("1) Addition \n "
          "2) Subtraction \n "
          "Enter 1 or 2:")


def get_num():
    num = input("Input number: ")
    if num.isnumeric():
        return int(num)
    else:
        print("E R R O R   K U R W A ! ! !")


# def get_answer_by_user_choose():


def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    # ans
    return num1 + num2


def subtraction():
    num1 = random.randint(25, 50)
    num2 = random.randint(5, 20)
    return num1 - num2


def main():
    display_options()
    display_option_by_user = get_num()


main()

