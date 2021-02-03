import random

def get_num():
    num = input("Input number: ")
    if num.isnumeric():
        return num
    else:
        print("E R R O R   K U R W A ! ! !")


def randomize_btwn_numbers(num1, num2):
    random_value = random.randint(int(num1), int(num2))
    return random_value


def comp_num(random_value):
    print("-------------------------\nG U E S S")
    i = 0
    while i == 0:
        guess = int(get_num())
        if guess == random_value:
            print("You guessed")
            return
        elif guess > random_value:
            print("Too much")
        elif guess < random_value:
            print("Too less")


def main():
    num1 = get_num()
    num2 = get_num()
    random_value = randomize_btwn_numbers(num1, num2)
    comp_num(random_value)
    print("C O N G R A T U L A T I O N S ! ! ! ! !")

main()