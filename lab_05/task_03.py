import sympy as sym
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

N = 100
eps = 0.000000001

def Newton(F, Jacobian, initValues):
    
	#Создается массив curValues, который инициализируется значениями из initValues и приводится к типу float.
    curValues = np.array(initValues, dtype = "float")

	#В результате, после выполнения этих двух строк, FCur будет содержать значения функций из системы уравнений с текущими значениями переменных
    FCur = F(*curValues)
    
	#JacobianCur будет содержать значения матрицы Якобиана для текущих значений переменных. 
    JacobianCur = Jacobian(*curValues)

	#Решается система линейных уравнений JacobianCur * delta = FCur, 
	# где delta - это неизвестные значения, которые мы хотим найти. Результат сохраняется в delta в виде одномерного массива.
    delta = solve(JacobianCur, FCur).reshape((N + 1, ))
    curValues += delta

	#Выполняется итерационный цикл, который продолжается до тех пор, пока норма delta 
	# (определенная с помощью np.linalg.norm) больше, чем eps
    while np.linalg.norm(delta) > eps:
        
        curValues -= delta

        FCur = F(*curValues)
        JacobianCur = Jacobian(*curValues)

        delta = solve(JacobianCur, FCur).reshape((N + 1, ))

    return curValues

start = [0, 1]
end = [1, 3]

step = (end[0] - start[0]) / N
xValues = np.array([i * step for i in range(N + 1)])

vars = [f'y{i}' for i in range(N + 1)]

funcs = [f'{vars[i - 1]} - 2 * {vars[i]} + {vars[i + 1]} - ({step} ** 2) * ({vars[i]} ** 3 + {xValues[i]} ** 2)' for i in range(1, N)]
funcs.extend(['y0 - 1', f'y{N} - 3'])

#Создание матрицы символьных выражений
F = sym.Matrix(funcs)

#Создание матрицы Якобиана. Vars - представляет список символьных переменных, соответствующих y0 до yN, созданных ранее.
Jacobian = sym.Matrix(funcs).jacobian(vars)

#Преобразуется матрица Якобиана в лямбда-функцию Jacobian. Это позволяет использовать матрицу Якобиана в численных вычислениях.
Jacobian = sym.lambdify(sym.symbols(vars), Jacobian)
F = sym.lambdify(sym.symbols(vars), F)

#Создаем начальные значения initValues для метода Ньютона, 
# которые представляют собой последовательность значений, инициализированных с помощью формулы
delta = (end[1] - start[1]) / (end[0] - start[0])
initValues = [start[1] + delta * i * step for i in range(N + 1)]

#Метод Ньютона для решения системы уравнений. Она принимает функцию F, матрицу Якобиана Jacobian и начальные значения initValues, 
# и возвращает массив значений y, которые являются решением системы уравнений.
yValues = Newton(F, Jacobian, initValues)

plt.grid()
plt.plot(xValues, initValues, label = "Init values")
plt.plot(xValues, yValues, label = "Result values")
plt.legend()
plt.show()
    
print(yValues[30:40])


