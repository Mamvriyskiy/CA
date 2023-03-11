"""
    Работа с полиномом Ньютона
"""

import input_output
import general_func

#Построение интерполяционного полинома
def NewtonMethod(result, n):
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

#Создание результируещого массива
def create_result_array_newton(data, border_one, border_two):
    newton_data = []
    for i in range(border_one, border_two):
        a = float(data[i][0])
        b = float(data[i][1])
        newton_data.append([a, b])
    
    return newton_data

def rootByNewton(newton_data):
    l = newton_data[-1][0]
    r = newton_data[0][0]
    while r - l > 1e-8:
        m = (r + l) / 2
        y = general_func.calculate_polinom(newton_data, m)
        if y < 0:
            l = m
        else:
            r = m
    return l
    
def newton_method_ex(data, border_one, border_two, n, x):

    newton_data = create_result_array_newton(data, border_one, border_two) #Построение первоначальной таблицы Ньютона

    NewtonMethod(newton_data, n) #Интерполяция полинома Ньютона

    input_output.create_table(newton_data)

    print("Newton: ")
    result = general_func.calculate_polinom(newton_data, x) #Подсчет полинома Ньютона 
    print("{:.6f}".format(result))

    x = rootByNewton(newton_data)
    print("Root by Newton: ", x)

    print()

    return newton_data
