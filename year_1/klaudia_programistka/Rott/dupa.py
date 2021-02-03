import math
first_one = int(input("gib liczbu"))
to_do = str(input("co chcesz zrobić? dodawanie = +, odejmowanie = -, mnozenie *, dzielenie /, logarytm log"))
second_one = int(input("gib liczbu"))

if "+" in to_do:
    fin = first_one + second_one
elif "-" in to_do:
    fin = first_one - second_one
elif "*" in to_do:
    fin = first_one * second_one
elif "/" in to_do:
    fin = first_one / second_one
else:
    fin = "no chyba nie"
print(fin)