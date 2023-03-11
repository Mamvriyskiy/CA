"""
    Функции общего пользования
"""

def search_index(data, x):
    k = 0
    for el in data:
        if (float(el[0]) > x):
            break
        k += 1
    
    return k

def create_border(data, n, x):
    k = search_index(data, x)
        
    n += 1

    border_one = k - n // 2 - n % 2
    border_two = k + n // 2

    if (border_two > len(data)):
        border_one -= (border_two - len(data))
        border_two -= (border_two - len(data))
    elif (border_one < 0):
        border_two += abs(border_one)
        border_one = 0

    return border_one, border_two


def sort_table(data):
    lenl = len(data)
    for i in range(lenl - 1):
        for j in range(0, lenl - i - 1):
            if (data[j][0] > data[j + 1][0]):
                data[j], data[j + 1] = data[j + 1], data[j]


def calculate_polinom(result, x):
    a = result[0][1]
    l = 1
    for i in range(2, len(result[0])):
        b = result[0][i]
        for j in range(l):
            b *= (x - result[j][0])
        l += 1
        a += b
    
    return a

