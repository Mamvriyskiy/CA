from tabulate import *

newton_data = []

#создание таблицы функций и ее производных
data = []
file = open("data.txt", "r")
n = 0
for i in file:
    m = i.split()
    data.append([n] + m)
    newton_data.append(m[0 : 2])
    n += 1

file.close()

col_names = ["№", "x", "y", "y'"]

print(tabulate(data, headers = col_names,  tablefmt = "fancy_grid"))
print()

#Чтение целых чисел
def input_int_num():
    try:
        n = int(input("Введите n: "))
        return n, n <= 0
    except ValueError:
        return -1, -1

#Чтение чисел с плавающей точкой
def input_float_num():
    try:
        x = float(input("Введите x: "))
        return x, 0
    except ValueError:
        return 0, 1

def create_border(n):
    k = 0
    for el in newton_data:
        if (float(el[0]) > x):
            break
        k += 1
    n += 1

    border_one = k - n // 2 - n % 2
    border_two = k + n // 2

    if (border_two > len(newton_data)):
        border_one -= (border_two - len(newton_data))
        border_two -= (border_two - len(newton_data))
    elif (border_one < 0):
        border_two += abs(border_one)
        border_one = 0

    return border_one, border_two

def create_table(result):
    for i in result:
        for j in i:
            print(j, end = " ")
        print()


#Основаная прогамма
while True:
    x, flag = input_float_num()
    if (flag):
        print("Данные введены неверно")
        continue

    n, flag = input_int_num()
    if (flag == -1):
        print("Данные введены неверно")
        continue
    
    # print(newton_data)    

    border_one, border_two = create_border(n)

    result = []

    for i in range(border_one, border_two):
        a = float(newton_data[i][0])
        b = float(newton_data[i][1])
        result.append([a, b])

    k = 1
    z = 1
    for i in range(n + 1):
        l = 0
        c = 0
        while (l != n + 1 - k):
            result[c].append((result[l + 1][k] - result[l][k]) / (result[l + z][0] - result[l][0]))
            c += 1
            l += 1
        z += 1
        k += 1


    create_table(result)

    
    

