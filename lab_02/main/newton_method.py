from scipy.misc import derivative
import input_output
import main

def search_index(data, x):
    k = 0
    for el in data:
        if (el[0] > x):
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

def NewtonMethod(result, n):
    k = 1
    z = 1
    for _ in range(n + 1):
        l = 0
        c = 0
        while (l != n + 1 - k):
            result[c].append((result[l + 1][k] - result[l][k]) / (result[l + z][0] - result[l][0]))
            c += 1
            l += 1
        z += 1
        k += 1

        
def calculate_polinom(result, x):
    a = result[0][1]
    l = 1
    for i in range(2, len(result[0])):
        b = result[0][i]
        for j in range(l):
            # print(result[j][0], j ,l)
            b *= (x - result[j][0])
        l += 1
        a += b
    
    
    return a

def newton_method_ex(data, n, x):
    a, b = create_border(data, n, x)

    newton_data = data[a : b]

    NewtonMethod(newton_data, n) #Интерполяция полинома Ньютона

    return calculate_polinom(newton_data, x)


def SearchDeritivePolinom(data, n, x):
    a, b = create_border(data, n, x)

    newton_data = data[a : b]

    NewtonMethod(newton_data, n)



    def aprox_func(x):
        res = 0
        for i in range(len(newton_data[0])):
            res += newton_data[0][i] * x ** i
        return res

    y_derivative_n_2 = derivative(aprox_func, x, n = 2, dx = 1e-6)
    return y_derivative_n_2
