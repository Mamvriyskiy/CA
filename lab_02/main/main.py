import input_output
import newton_method
import spline 
import numpy as np
from matplotlib import pyplot as plt

def copy_array(data):
    data_1 = []
    for i in range(len(data)):
        data_1.append([data[i][0], data[i][1]])

    return data_1

def application():
    data = input_output.read_file(name_file = "../data/data_1.txt")
    
    input_output.create_table(data)

    a_1, b_1 = 0, 0
    a_2, b_2 = 0, 0
    a_3, b_3 = 0, 0

    n = 3
    x = float(input("Введите значение аргумента x: "))

    data_1 = copy_array(data)
    b_2 = newton_method.SearchDeritivePolinom(data_1, n, data_1[-1][0])

    a_3 = newton_method.SearchDeritivePolinom(data_1, n, data[0][0])


    b_3 = b_2

    data_2 = copy_array(data)
    values_y = [list(), list(), list(), list()]

    print("\nПолином Ньютона 3 степени: ", newton_method.newton_method_ex(data_2, n, x))


    data_3 = copy_array(data)

    print("Cплайн 0 and 0:             ", spline.spline(data_3, x, a_1, b_1))
    print("-----")
    
    print("Cплайн 0 and P''(xn):       ", spline.spline(data_3, x, a_2, b_2))
    print("-----")
    print("Cплайн P''(x0) and P''(xn): ", spline.spline(data_3, x, a_3, b_3))

    values_x = np.linspace(data[0][0], data[-1][0], 100)

    for xi in values_x:
        data_4 = copy_array(data)
        values_y[3].append(newton_method.newton_method_ex(data_4, n, xi))

    for xi in values_x:
        data_5 = copy_array(data)
        values_y[0].append(spline.spline(data_5, xi, a_1, b_1))

    for xi in values_x:
        data_6 = copy_array(data)
        values_y[1].append(spline.spline(data_6, xi, a_2, b_2))

    for xi in values_x:
        data_7 = copy_array(data)
        values_y[2].append(spline.spline(data_7, xi, a_3, b_3))


    plt.plot(values_x, values_y[0], '-', color = 'r', linewidth = 6)
    plt.plot(values_x, values_y[1], '-', color = 'b', linewidth = 4)
    plt.plot(values_x, values_y[2], '-', color = 'g', linewidth = 2)

    if n < len(data):
        plt.plot(values_x, values_y[3], ':', color = 'b', linewidth = 1, label = "Newton")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    application()
