example = str("ala ma 137 kotów")

arr_of_example = example.split(" ")
answer = None
for i in range(len(arr_of_example)):
    if arr_of_example[i].isnumeric():
        answer = int(arr_of_example[i])

print(answer)