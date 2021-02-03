def ask_number():
    num = input("Input number: ")
    if num.isnumeric():
        return num
    else:
        print("E R R O R   K U R W A ! ! !")


def cout_up(num, n=1):
    while n <= num:
        print(n)
        n += 1


def main():
    num = ask_number()
    cout_up(num)


main()
