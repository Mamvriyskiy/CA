"""
    Работа с полиномом Хермита
"""

import input_output
import general_func

def create_result_array_hermit(newton_data, border_one, data):
    hermit_array = []
    l = border_one
    k = 0

    for i in range(len(newton_data) - 1):
        a = float(newton_data[i][0])
        b = float(newton_data[i][1])
        hermit_array.append([a, b, float(data[l][2])])
        hermit_array.append([a, b, float(newton_data[k][2])])
        l += 1
        k += 1

    hermit_array.append([float(newton_data[i + 1][0]), float(newton_data[i + 1][1]), float(data[l][2])])
    hermit_array.append([float(newton_data[i + 1][0]), float(newton_data[i + 1][1])])

    return hermit_array

#Построение интерполяционного полинома (y0 - y(x0, x1)) / (x0 - x1)
def HermitMethod(hermit_array, n) :
    l = (n + 1) * 2 - 2
    k = 2
    for i in range(n * 2):
        for j in range(l):
            hermit_array[j].append((hermit_array[j][k] - hermit_array[j + 1][k]) / (hermit_array[j][0] - hermit_array[j + k][0]))
        l -= 1
        k += 1
        
def rootByHermit(hermit_data):
    l = hermit_data[-1][0]
    r = hermit_data[0][0]
    while r - l > 1e-8:
        m = (r + l) / 2
        y = general_func.calculate_polinom(hermit_data, m)
        if y < 0:
            l = m
        else:
            r = m
    return l

def hermit_method_ex(data, border_one, border_two, n, x, newton_data):

    hermit_data = create_result_array_hermit(newton_data, border_one, data) #Построение первоначальной таблицы Хермита

    HermitMethod(hermit_data, n) #Интерполяция полинома Хермита

    input_output.create_table(hermit_data)

    print("Hermit: ")
    result = general_func.calculate_polinom(hermit_data, x) #Подсчет полинома Ньютона 
    print("{:.6f}".format(result))

    x = rootByHermit(hermit_data)
    print("Root by Hermit: ", x)


